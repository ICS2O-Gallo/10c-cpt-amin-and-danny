import os
import arcade


WIDTH = 1300
HEIGHT = 700
SCREEN = "Main Menu"

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

background = arcade.load_texture(r'C:\Users\User\Desktop\cpt\background.jpeg')

floor = arcade.load_texture(r'C:\Users\User\Desktop\cpt\floor.png')
left_wall = arcade.load_texture(r'C:\Users\User\Desktop\cpt\left wall.png')
right_wall = arcade.load_texture(r'C:\Users\User\Desktop\cpt\right wall.png')
upper_wall = arcade.load_texture(r'C:\Users\User\Desktop\cpt\upper wall.png')
under_wall = arcade.load_texture(r'C:\Users\User\Desktop\cpt\under wall.png')
coner_wall = arcade.load_texture(r'C:\Users\User\Desktop\cpt\coner wall.png')

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
        self.tile_img = arcade.load_texture(r'C:\Users\User\Desktop\cpt\background.jpeg')

    def draw_background(self):
        # TILES
        for x in range(self.whole_map_x, self.whole_map_x + self.whole_map_width, self.tile_img.width):
            for y in range(self.whole_map_y, self.whole_map_y + self.whole_map_length, self.tile_img.height):
                arcade.draw_xywh_rectangle_textured(x, y, self.tile_img.width, self.tile_img.height, self.tile_img)
        # BUILDING
        # Floor
        for x in range(500, WIDTH, floor.width):
            for y in range(500, HEIGHT, floor.height):
                arcade.draw_xywh_rectangle_textured(375, 100, floor.width + 350, floor.height + 250, floor)
        # Left wall
        for x in range(500, WIDTH, left_wall.width):
            for y in range(500, HEIGHT, left_wall.height):
                arcade.draw_xywh_rectangle_textured(375 - 125, 100, left_wall.width - 100, left_wall.height + 250,
                                                    left_wall)
        # Right wall
        for x in range(500, WIDTH, right_wall.width):
            for y in range(500, HEIGHT, right_wall.height):
                arcade.draw_xywh_rectangle_textured(375 + 575, 100, right_wall.width - 100, right_wall.height + 250,
                                                    right_wall)
        # Upper wall
        for x in range(500, WIDTH, upper_wall.width):
            for y in range(500, HEIGHT, upper_wall.height):
                arcade.draw_xywh_rectangle_textured(375, 100 + 475, upper_wall.width + 350, upper_wall.height - 120,
                                                    upper_wall)
        # Under wall
        for x in range(500, WIDTH, under_wall.width):
            for y in range(500, HEIGHT, under_wall.height):
                arcade.draw_xywh_rectangle_textured(375, 100 - 105, under_wall.width + 350, under_wall.height - 120,
                                                    under_wall)
        # Coner Wall (Upper left)
        for x in range(500, WIDTH, coner_wall.width):
            for y in range(500, HEIGHT, coner_wall.height):
                arcade.draw_xywh_rectangle_textured(250, 100 + 475, coner_wall.width + 5, coner_wall.height - 15,
                                                    coner_wall)
        # Coner Wall (Upper right)
        for x in range(500, WIDTH, coner_wall.width):
            for y in range(500, HEIGHT, coner_wall.height):
                arcade.draw_xywh_rectangle_textured(950, 100 + 475, coner_wall.width + 5, coner_wall.height - 15,
                                                    coner_wall)
        # Coner Wall (Under left)
        for x in range(500, WIDTH, coner_wall.width):
            for y in range(500, HEIGHT, coner_wall.height):
                arcade.draw_xywh_rectangle_textured(250, 100 - 105, coner_wall.width + 5, coner_wall.height - 15,
                                                    coner_wall)
        # Coner Wall (Under right)
        for x in range(500, WIDTH, coner_wall.width):
            for y in range(500, HEIGHT, coner_wall.height):
                arcade.draw_xywh_rectangle_textured(950, 100 - 105, coner_wall.width + 5, coner_wall.height - 15,
                                                    coner_wall)

class GameoverScreen(object):
    def __init__(self):
        self.x = WIDTH / 3
        self.y = HEIGHT / 3
        self.width = WIDTH / 3
        self.height = HEIGHT / 12
        self.title_size = (self.width * self.height) * (3 / 728)
        self.font_size = (self.width * self.height) * (1 / 728)
        self.font_x = (self.width - self.font_size) / 2 + self.x
        self.font_y = (self.height - self.font_size) / 2 + self.y

    def draw_gameover_screen(self):
        arcade.draw_text("You Died!", 0 - 30, 275, arcade.color.RED_DEVIL, self.font_size * 2.5,
                         font_name="TIMES NEW ROMAN")
        arcade.draw_xywh_rectangle_filled(0 - 10, 65, self.width, self.height, arcade.color.BATTLESHIP_GREY)
        arcade.draw_text("Main Menu", 100, 75,arcade.color.BLACK, self.font_size, font_name="TIMES NEW ROMAN")



class Player(object):
    def __init__(self, sprite, size, x, y):
        self.player_sprite = arcade.Sprite(sprite, size)
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        self.player_is_attacked = False
        self.health = 100

    def draw(self):
        self.player_sprite.draw()
        # health bar
        if self.player_is_attacked:
            arcade.draw_xywh_rectangle_filled(self.player_sprite.center_x - (self.player_sprite.width / 4),
                                              self.player_sprite.center_y + (self.player_sprite.height / 2),
                                              100, 5, arcade.color.RED)
            arcade.draw_xywh_rectangle_filled(self.player_sprite.center_x - (self.player_sprite.width / 4),
                                              self.player_sprite.center_y + (self.player_sprite.height / 2),
                                              self.health, 5, arcade.color.GREEN)

    def player_movement(self):
        self.player_sprite.center_x += self.player_sprite.change_x
        self.player_sprite.center_y += self.player_sprite.change_y

    def player_death(self):
        global SCREEN

        if self.health <= 0:
            SCREEN = "Game Over"



character = Player(r'C:\Users\User\Desktop\cpt\player.png', 2, 400, 100)


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
        if character.player_sprite.center_x > self.character_sprite.center_x:
            self.character_sprite.change_x = 2
        elif character.player_sprite.center_x < self.character_sprite.center_x:
            self.character_sprite.change_x = -2

        if character.player_sprite.center_y > self.character_sprite.center_y:
            self.character_sprite.change_y = 2
        elif character.player_sprite.center_y < self.character_sprite.center_y:
            self.character_sprite.change_y = -2

        if character.player_sprite.center_x == self.character_sprite.center_x \
                or self.character_sprite.center_x == self.character_sprite.center_x - 1 \
                or character.player_sprite.center_x == self.character_sprite.center_x + 1:
            self.character_sprite.change_x = 0

        if character.player_sprite.center_y == self.character_sprite.center_y \
                or character.player_sprite.center_y == self.character_sprite.center_y - 1 \
                or character.player_sprite.center_y == self.character_sprite.center_y + 1:
            self.character_sprite.change_y = 0
        self.character_sprite.center_x += self.character_sprite.change_x
        self.character_sprite.center_y += self.character_sprite.change_y

    def zombie_attack(self, delta_time):
        if character.player_sprite.center_x == self.character_sprite.center_x \
                and character.player_sprite.center_y == self.character_sprite.center_y:
            if character.health > 0:
                character.health -= 5 * delta_time
            setattr(character, 'player_is_attacked', True)
        else:
            setattr(character, 'player_is_attacked', False)


zombie_1 = Zombie(r'C:\Users\User\Desktop\cpt\zombie1.png', 2, 100, 200)


main_screen = MainScreen()
new_game = [main_screen.x, main_screen.y + 200, main_screen.width, main_screen.height]


gameover_screen = GameoverScreen()
main_menu = [gameover_screen.x, gameover_screen.y + 200, gameover_screen.width, gameover_screen.height]

def update(delta_time):
    if SCREEN == "Game":
        arcade.set_viewport(-WIDTH / 2 + character.player_sprite.center_x,
                            WIDTH / 2 + character.player_sprite.center_x,
                            -HEIGHT / 2 + character.player_sprite.center_y,
                            HEIGHT / 2 + character.player_sprite.center_y)
        character.player_movement()
        zombie_1.follow_player()
        zombie_1.zombie_attack(1 / 60)
        character.player_death()
        print(f"Player is attacked: {character.player_is_attacked}")
        print(f"Player {getattr(character, 'health')} HP")


def on_draw():
    arcade.start_render()
    # Draw in here...
    if SCREEN == "Main Menu":
        arcade.set_viewport(0, WIDTH, 0, HEIGHT)
        arcade.set_background_color(arcade.color.WHITE)
        main_screen.draw_main_screen()
    elif SCREEN == "Game":
        game = Background()
        game.draw_background()
        character.draw()
        zombie_1.draw()
    elif SCREEN == "Game Over":
        arcade.set_background_color(arcade.color.WHITE)
        gameover_screen.draw_gameover_screen()


def on_key_press(key, modifiers):
    global character
    if key == arcade.key.W:
        character.player_sprite.change_y = 6
    elif key == arcade.key.A:
        character.player_sprite.change_x = -6
    elif key == arcade.key.D:
        character.player_sprite.change_x = 6
    elif key == arcade.key.S:
        character.player_sprite.change_y = -6


def on_key_release(key, modifiers):
    global SCREEN, character
    if SCREEN == "Main Menu":
        if key == arcade.key.ENTER:
            SCREEN = "Game"
    elif SCREEN == "Game":
        if key == arcade.key.ESCAPE:
            SCREEN = "Main Menu"

    # Look over this
    if key == arcade.key.W:
        character.player_sprite.change_y = 0
    elif key == arcade.key.A:
        character.player_sprite.change_x = 0
    elif key == arcade.key.D:
        character.player_sprite.change_x = 0
    elif key == arcade.key.S:
        character.player_sprite.change_y = 0


def on_mouse_press(x, y, button, modifiers):
    global SCREEN

    if (new_game[BTN_X] < x < new_game[BTN_X] + new_game[BTN_WIDTH] and
            new_game[BTN_Y] < y < new_game[BTN_Y] + new_game[BTN_HEIGHT]):
        SCREEN = 'Game'

    elif (main_menu[BTN_X] < x < main_menu[BTN_X] + main_menu[BTN_WIDTH] and
            main_menu[BTN_Y] < y < main_menu[BTN_Y] + main_menu[BTN_HEIGHT]):
        SCREEN = 'Main Menu'


if __name__ == '__main__':
    setup()
