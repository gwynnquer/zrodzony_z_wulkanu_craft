# own libraries
import display_manager
import entity

# external libraries
import pygame


class MainPlayer(entity.Entity):

    PLAYERS = {
        'kwiat': {
            'image': r'01.ASSETS\graphics\characters\kwiat.png',
            'stats': (12, 20, 16),
        },
        'dasher': {
            'image': r'01.ASSETS\graphics\characters\dasher.png',
            'stats': (12, 14, 18),
        },
    }

    def __init__(self, player_name):

        super().__init__(
            image=self.PLAYERS[player_name]['image'],
            stats=self.PLAYERS[player_name]['stats'],
            gravity=True,
        )

        # parametry mapy
        self.floor = display_manager.GameWindowSettings.WINDOW_HEIGHT
        self.wall = display_manager.GameWindowSettings.WINDOW_WIDTH

        # czy klawisze wcisneite
        self.left_pressed, self.right_pressed, self.up_pressed, self.jumping = False, False, False, False

        # ustawienie gracza na mapie
        self.rect.y = self.floor - self.rect.height
        self.rect.x = 0

        self.on_ground = True
        self.distance_jumped, self.vel_y = 0, 0

    # przypisanie akcji gracza do działania
    def get_actions(self, actions):
        # akcje ruchu

        self.left_pressed = actions['left']
        self.right_pressed = actions['right']
        self.up_pressed = actions['up']

        self.update_movement()

    # ruch gracza
    def update_movement(self):
        self.vel_x = 0

        # grawitacja
        if not self.jumping:
            self.apply_gravity()

        # prawo lewo
        if self.left_pressed and not self.right_pressed:
            self.vel_x = -self.ms
        if self.right_pressed and not self.left_pressed:
            self.vel_x = self.ms

        # skakanie
        if self.up_pressed and not self.jumping and self.on_ground:
            self.vel_y = -self.jump
            self.on_ground = False
            self.jumping = True
            self.up_pressed = False
        elif not self.up_pressed:
            self.jumping = False

        self.distance_jumped += self.vel_y

        if self.distance_jumped <= 250 * -self.jump:
            self.jumping = False

        print(self.distance_jumped)
        print(50 * -self.jump)
        # zmienianie pozycji gracza
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # na sam koniec korekta ruchu w krytycznych przypadkach
        self.correct_movement()

    def apply_gravity(self):
        # jesli bedzie bug ze mozna spasc pod mape to przez to
        self.vel_y += self.GRAVITY

    def correct_movement(self):

        # poprawia ruch gracza jesli ten wychodzi poza mape, przelacza mape
        self.pass_left = False
        self.pass_right = False

        # skakanie
        if self.rect.bottom >= self.floor or self.on_ground == True:
            self.rect.bottom = self.floor
            self.on_ground = True
            self.jumping = False
            self.vel_y = 0
            self.distance_jumped = 0

        # prawo
        if self.rect.left > self.wall + 10:
            self.rect.right = 0
            self.pass_left = True

        # lewo
        if self.rect.right < -10:
            self.rect.left = self.wall
            self.pass_right = True
