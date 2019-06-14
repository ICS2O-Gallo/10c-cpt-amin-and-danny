import os
import arcade
from math import floor

WIDTH = 1300
HEIGHT = 700
SCREEN = "Main Menu"

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

background = arcade.load_texture('D:\Programs\c-cpt-amin-and-danny\Master\Assets\download(1).jpeg')

BTN_X = 0
BTN_Y = 1
BTN_WIDTH = 2
BTN_HEIGHT = 3


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


class MainScreen(object):
    def __init__(self):
        self.x = WIDTH / 3
        self.y = HEIGHT / 3
        self.width = WIDTH / 3
        self.height = HEIGHT / 12
        self.title_size = (self.width * self.height) * (3 / 728)
        self.font_size = (self.width * self.height) * (1 / 728)
        self.font_x = (self.width - self.font_size) / 2 + self.x
        self.font_y = (self.height - self.font_size) / 2 + self.y

    def draw_main_screen(self):
        # TITLE
        arcade.draw_text("ZombiE", self.x, HEIGHT - (1.6 * self.title_size), arcade.color.YELLOW, self.title_size)
        # START BUTTON
        arcade.draw_xywh_rectangle_filled(self.x, self.y + 200, self.width, self.height, arcade.color.BATTLESHIP_GREY)
        arcade.draw_text("NEW  GAME", self.font_x - (25 / 8 * self.font_size), self.font_y + 200, arcade.color.BLACK,
                         self.font_size, font_name="TIMES NEW ROMAN")
        # CONTINUE BUTTON
        arcade.draw_xywh_rectangle_filled(self.x, self.y + 100, self.width, self.height, arcade.color.BATTLESHIP_GREY)
        arcade.draw_text(" CONTINUE ", self.font_x - (26 / 8 * self.font_size), self.font_y + 100, arcade.color.BLACK,
                         self.font_size, font_name="TIMES NEW ROMAN")
        # OPTIONS BUTTON
        arcade.draw_xywh_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.BATTLESHIP_GREY)
        arcade.draw_text("OPTIONS", self.font_x - (19 / 8 * self.font_size), self.font_y, arcade.color.BLACK,
                         self.font_size, font_name="TIMES NEW ROMAN")


class Background(object):
    def __init__(self):
        self.whole_map_x = -1 * WIDTH
        self.whole_map_y = -1 * HEIGHT
        self.whole_map_width = WIDTH * 3
        self.whole_map_length = HEIGHT * 3

        # Change file path to appropriate one
        self.tile_img = arcade.load_texture('download.jpeg')

    def draw_background(self):
        # TILES
        for x in range(self.whole_map_x, self.whole_map_x + self.whole_map_width, self.tile_img.width):
            for y in range(self.whole_map_y, self.whole_map_y + self.whole_map_length, self.tile_img.height):
                arcade.draw_xywh_rectangle_textured(x, y, self.tile_img.width, self.tile_img.height, self.tile_img)
        # TREES
        # BUILDING
        for x in range(500, WIDTH, background.width):
            for y in range(500, HEIGHT, background.height):
                arcade.draw_xywh_rectangle_textured(375, 100, background.width + 350, background.height + 250,
                                                    background)


class Player(object):
    def __init__(self, x, y, width, change_x, change_y):
        self.width = width
        self.height = width * 2
        self.height = width * 2
        self.radius = width / 2
        self.arm_width = width / 4
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.color = arcade.color.YELLOW
        self.health = 100
        self.player_is_attacked = False

    def draw_player(self):
        # torso
        arcade.draw_xywh_rectangle_filled(self.x, self.y, self.width, self.height, self.color)
        # head
        arcade.draw_circle_filled(self.x + self.radius, self.y + self.height + self.radius, self.radius,
                                  self.color)
        # legs
        arcade.draw_xywh_rectangle_filled(self.x, self.y - self.height, self.radius - 1, self.height, arcade.color.RED)
        arcade.draw_xywh_rectangle_filled(self.x + self.radius + 1, self.y - self.height, self.radius - 1, self.height,
                                          self.color)
        # arms
        arcade.draw_xywh_rectangle_filled(self.x - self.arm_width, self.y + self.height * 0.2, self.arm_width,
                                          self.height * 0.8, self.color)
        arcade.draw_xywh_rectangle_filled(self.x + self.width, self.y + self.height * 0.2, self.arm_width,
                                          self.height * 0.8, self.color)
        # health bar
        if self.player_is_attacked:
            arcade.draw_xywh_rectangle_filled(self.x,  self.y + self.height + self.height, 100, 5, arcade.color.GREEN)
            arcade.draw_xywh_rectangle_filled(self.x + self.health, self.y + self.height + self.height,
                                              100 - self.health, 5, arcade.color.RED)

    def player_movement(self):
        self.x += self.change_x
        self.y += self.change_y

    def player_death(self):
        if self.health == 0:
            SCREEN = "Main Screen"


character = Player(400, 100, 20, 0, 0)


class Zombie(object):
    def __init__(self, sprite, size, x, y):
        self.character_sprite = arcade.Sprite(sprite, size)
        self.character_sprite.center_x = x
        self.character_sprite.center_y = y
        self.character_sprite.change_x = 0
        self.character_sprite.change_y = 0

    def draw(self):
        self.character_sprite.draw()


    def follow_player(self):
        if getattr(character, 'x') > self.character_sprite.center_x:
            self.character_sprite.change_x = 2
        elif getattr(character, 'x') < self.character_sprite.center_x:
            self.character_sprite.change_x = -2

        if getattr(character, 'y') > self.character_sprite.center_y:
            self.character_sprite.change_y = 2
        elif getattr(character, 'y') < self.character_sprite.center_y:
            self.character_sprite.change_y = -2

        if getattr(character, 'x') == self.character_sprite.center_x or getattr(character, 'x') == self.character_sprite.center_x -1 \
                or getattr(character, 'x') == self.character_sprite.center_x + 1:
            self.character_sprite.change_x = 0

        if getattr(character, 'y') == self.character_sprite.center_y or getattr(character, 'y') == self.character_sprite.center_y -1 \
                or getattr(character, 'y') == self.character_sprite.center_y + 1:
            self.character_sprite.change_y = 0
        self.character_sprite.center_x += self.character_sprite.change_x
        self.character_sprite.center_y += self.character_sprite.change_y

    def zombie_attack(self, delta_time):
        if getattr(character, 'x') == self.character_sprite.center_x and getattr(character, 'y') == self.character_sprite.center_y:
            character.health -= 5 * delta_time
            setattr(character, 'player_is_attacked', True)
        else:
            setattr(character, 'player_is_attacked', False)


zombie_1 = Zombie('D:\Programs\pixil-frame-0 (1).png', 2, 100, 200)
main_screen = MainScreen()
new_game = [main_screen.x, main_screen.y + 200, main_screen.width, main_screen.height]


def update(delta_time):
    if SCREEN == "Game":
        arcade.set_viewport(-WIDTH / 2 + character.x,
                            WIDTH / 2 + character.x,
                            -HEIGHT / 2 + character.y,
                            HEIGHT / 2 + character.y)
        character.player_movement()
        zombie_1.follow_player()
        zombie_1.zombie_attack(1/60)
        print(f"Player is attacked: {character.player_is_attacked}")
        print(f"Player {getattr(character, 'health')} HP")


def on_draw():
    arcade.start_render()
    # Draw in here...
    if SCREEN == "Main Menu":
        arcade.set_background_color(arcade.color.WHITE)
        main_screen.draw_main_screen()
    elif SCREEN == "Game":
        game = Background()
        game.draw_background()
        character.draw_player()
        zombie_1.draw()


def on_key_press(key, modifiers):
    global character
    if key == arcade.key.W:
        setattr(character, 'change_y', 6)
    elif key == arcade.key.A:
        setattr(character, 'change_x', -6)
    elif key == arcade.key.D:
        setattr(character, 'change_x', 6)
    elif key == arcade.key.S:
        setattr(character, 'change_y', -6)


def on_key_release(key, modifiers):
    global SCREEN, character
    if SCREEN == "Main Menu":
        if key == arcade.key.ENTER:
            SCREEN = "Game"
    elif SCREEN == "Game":
        if key == arcade.key.ESCAPE:
            SCREEN = "Main Menu"

    if key == arcade.key.W:
        setattr(character, 'change_y', 0)
    elif key == arcade.key.A:
        setattr(character, 'change_x', 0)
    elif key == arcade.key.D:
        setattr(character, 'change_x', 0)
    elif key == arcade.key.S:
        setattr(character, 'change_y', 0)


def on_mouse_press(x, y, button, modifiers):
    global SCREEN

    if (new_game[BTN_X] < x < new_game[BTN_X] + new_game[BTN_WIDTH] and
            new_game[BTN_Y] < y < new_game[BTN_Y] + new_game[BTN_HEIGHT]):
        SCREEN = 'Game'


if __name__ == '__main__':
    setup()
