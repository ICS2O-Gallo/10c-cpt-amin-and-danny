mport os
import arcade

WIDTH = 1300
HEIGHT = 700
SCREEN = "Main Menu"

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

#Change file path to appropriate one
tile_img = arcade.load_texture('Assets/download.jpeg')


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
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

    def draw_background(self):
        # TILES
        for x in range(self.whole_map_x, self.whole_map_x + self.whole_map_width, tile_img.width):
            for y in range(self.whole_map_y, self.whole_map_y + self.whole_map_length, tile_img.height):
                arcade.draw_xywh_rectangle_textured(x, y, tile_img.width, tile_img.height, tile_img)
        # TREES
        # BUILDING


class Player(object):
    def __init__(self, x=400, y=125, width=20):
        self.width = width
        self.height = width * 2
        self.height = width * 2
        self.radius = width / 2
        self.arm_width = width / 4
        self.x = x
        self.y = y

    def draw_player(self):
        # torso
        arcade.draw_xywh_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.BLUE)
        # head
        arcade.draw_circle_filled(self.x + self.radius, self.y + self.height + self.radius, self.radius, arcade.color.YELLOW)
        # legs
        arcade.draw_xywh_rectangle_filled(self.x, self.y - self.height, self.radius - 1, self.height, arcade.color.RED)
        arcade.draw_xywh_rectangle_filled(self.x + self.radius + 1, self.y - self.height, self.radius - 1, self.height, arcade.color.RED)
        # arms
        arcade.draw_xywh_rectangle_filled(self.x - self.arm_width, self.y + self.height * 0.2, self.arm_width, self.height * 0.8, arcade.color.RED)
        arcade.draw_xywh_rectangle_filled(self.x + self.width, self.y + self.height * 0.2, self.arm_width, self.height * 0.8, arcade.color.RED)


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    if SCREEN == "Main Menu":
        arcade.set_background_color(arcade.color.WHITE)
        main_screen = MainScreen()
        main_screen.draw_main_screen()
    elif SCREEN == "Game":
        game = Background()
        character = Player()
        game.draw_background()
        character.draw_player()



def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    global SCREEN
    if SCREEN == "Main Menu":
        if key == arcade.key.ENTER:
            SCREEN = "Game"
    elif SCREEN == "Game":
        if key == arcade.key.ESCAPE:
            SCREEN = "Main Menu"
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
