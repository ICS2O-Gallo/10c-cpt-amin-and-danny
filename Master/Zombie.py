import os
import arcade

WIDTH = 1300
HEIGHT = 700
SCREEN = "Main Menu"

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

background = arcade.load_texture('/home/robuntu/Downloads/download (2).jpeg')

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
        self.tile_img = arcade.load_texture('/home/robuntu/Hosseini/untitled/download.jpeg')

    def draw_background(self):
        # TILES
        for x in range(self.whole_map_x, self.whole_map_x + self.whole_map_width, self.tile_img.width):
            for y in range(self.whole_map_y, self.whole_map_y + self.whole_map_length, self.tile_img.height):
                arcade.draw_xywh_rectangle_textured(x, y, self.tile_img.width, self.tile_img.height, self.tile_img)
        # TREES
        # BUILDING


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

    def draw_player(self):
        # torso
        arcade.draw_xywh_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.BLUE)
        # head
        arcade.draw_circle_filled(self.x + self.radius, self.y + self.height + self.radius, self.radius,
                                  arcade.color.YELLOW)
        # legs
        arcade.draw_xywh_rectangle_filled(self.x, self.y - self.height, self.radius - 1, self.height, arcade.color.RED)
        arcade.draw_xywh_rectangle_filled(self.x + self.radius + 1, self.y - self.height, self.radius - 1, self.height,
                                          arcade.color.RED)
        # arms
        arcade.draw_xywh_rectangle_filled(self.x - self.arm_width, self.y + self.height * 0.2, self.arm_width,
                                          self.height * 0.8, arcade.color.RED)
        arcade.draw_xywh_rectangle_filled(self.x + self.width, self.y + self.height * 0.2, self.arm_width,
                                          self.height * 0.8, arcade.color.RED)

    def player_movement(self):
        self.x += self.change_x
        self.y += self.change_y


character = Player(400, 125, 20, 0, 0)


class Zombie(object):
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

    def draw_player(self):
        # torso
        arcade.draw_xywh_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.GREEN)
        # head
        arcade.draw_circle_filled(self.x + self.radius, self.y + self.height + self.radius, self.radius,
                                  arcade.color.GREEN)
        # legs
        arcade.draw_xywh_rectangle_filled(self.x, self.y - self.height, self.radius - 1, self.height, arcade.color.GREEN)
        arcade.draw_xywh_rectangle_filled(self.x + self.radius + 1, self.y - self.height, self.radius - 1, self.height,
                                          arcade.color.GREEN)
        # arms
        arcade.draw_xywh_rectangle_filled(self.x - self.arm_width, self.y + self.height * 0.2, self.arm_width,
                                          self.height * 0.8, arcade.color.RED)
        arcade.draw_xywh_rectangle_filled(self.x + self.width, self.y + self.height * 0.2, self.arm_width,
                                          self.height * 0.8, arcade.color.RED)

    def follow_player(self, delta_time):
        if getattr(character, 'x') > self.x:
            self.change_x = 2
        elif getattr(character, 'x') < self.x:
            self.change_x = -2
            
        if getattr(character, 'y') > self.y:
            self.change_y = 2
        elif getattr(character, 'y') < self.y:
            self.change_y = -2

        if getattr(character, 'x') == self.x:
            self.change_x = 0

        if getattr(character, 'y') == self.y:
            self.change_y = 0
        self.x += self.change_x
        self.y += self.change_y


zombie_1 = Zombie(100, 100, 20, 0, 0)
main_screen = MainScreen()
new_game = [main_screen.x, main_screen.y + 200, main_screen.width, main_screen.height]


def update(delta_time):
    if SCREEN == "Game":
        arcade.set_viewport(-WIDTH / 2 + character.x,
                            WIDTH / 2 + character.x,
                            -HEIGHT / 2 + character.y,
                            HEIGHT / 2 + character.y)
        character.player_movement()
        print(f"x:{getattr(character, 'change_x')}, y: {getattr(character, 'change_y')}")
        zombie_1.follow_player(1/60)
        print(f"x:{getattr(zombie_1, 'change_x')}, y: {getattr(zombie_1, 'change_y')}")


def on_draw():
    arcade.start_render()
    # Draw in here...
    if SCREEN == "Main Menu":
        arcade.set_background_color(arcade.color.WHITE)
        main_screen.draw_main_screen()
    elif SCREEN == "Game":
        game = Background()
        game.draw_background()
        for x in range(500, WIDTH, background.width):
            for y in range(500, HEIGHT, background.height):
                arcade.draw_xywh_rectangle_textured(375, 100, background.width + 350, background.height + 250, background)
        character.draw_player()
        zombie_1.draw_player()


def on_key_press(key, modifiers):
    global character
    if key == arcade.key.W:
        setattr(character, 'change_y', 5)
    elif key == arcade.key.A:
        setattr(character, 'change_x', -5)
    elif key == arcade.key.D:
        setattr(character, 'change_x', 5)
    elif key == arcade.key.S:
        setattr(character, 'change_y', -5)


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
    print(f"Click at ({x}, {y})")

    if (new_game[BTN_X] < x < new_game[BTN_X] + new_game[BTN_WIDTH] and
            new_game[BTN_Y] < y < new_game[BTN_Y] + new_game[BTN_HEIGHT]):
        SCREEN = 'Game'


if __name__ == '__main__':
    setup()
