import os
import arcade


WIDTH = 1300
HEIGHT = 700
SCREEN = "Main Menu"

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

background = arcade.load_texture \
    ('D:\Programs\cpt-amin-and-danny\Master\Assets\download (2).jpeg')

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
        self.tile_img = arcade.load_texture \
            ('D:\Programs\cpt-amin-and-danny\Master\Assets\download.jpeg')

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
            arcade.draw_xywh_rectangle_filled(self.player_sprite.center_x - (self.player_sprite.width / 2.5),
                                              self.player_sprite.center_y + (self.player_sprite.height / 2),
                                              100, 5, arcade.color.RED)
            arcade.draw_xywh_rectangle_filled(self.player_sprite.center_x - (self.player_sprite.width / 2.5),
                                              self.player_sprite.center_y + (self.player_sprite.height / 2),
                                              self.health, 5, arcade.color.GREEN)

    def player_movement(self):
        self.player_sprite.center_x += self.player_sprite.change_x
        self.player_sprite.center_y += self.player_sprite.change_y

    def player_death(self):
        global SCREEN

        if self.health <= 0:
            SCREEN = "Main Menu"



character = Player \
    ('D:\Programs\cpt-amin-and-danny\Master\Assets\pixil-frame-0(5).png',
     2, 400, 100)

class Weapon(object):
    def __init__(self, sprite, size, x, y, equipped, damage, ammo, reload_rate):
        self.weapon = arcade.Sprite(sprite, size)
        self.weapon.center_x = x
        self.weapon.center_y = y
        self.equipped = equipped
        self.damage = damage
        self.ammo = ammo
        self.reload_rate = reload_rate

    def draw(self):
        self.weapon.draw()

    def equip(self):
        if self.equipped:
            self.weapon.center_x = character.player_sprite.center_x
            self.weapon.center_y = character.player_sprite.center_y
            self.weapon. change_x = character.player_sprite.change_x
            self.weapon. change_x = character.player_sprite.change_y


gun = Weapon('C:\\Users\\Administrator\\Downloads\\pixel-64x64 (3).png', 1, 200, 400, False, 5, 10, 5)


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
                character.health -= 10 * delta_time
            setattr(character, 'player_is_attacked', True)
        else:
            setattr(character, 'player_is_attacked', False)


zombie_1 = Zombie('D:\Programs\cpt-amin-and-danny\Master\Assets\pixel-272x221.png', 1, 100, 200)
main_screen = MainScreen()
new_game = [main_screen.x, main_screen.y + 200, main_screen.width, main_screen.height]


def update(delta_time):
    if SCREEN == "Game":
        weapon_distance_x = abs(character.player_sprite.center_x - gun.weapon.center_x)
        weapon_distance_y = abs(character.player_sprite.center_y - gun.weapon.center_y)
        arcade.set_viewport(-WIDTH / 2 + character.player_sprite.center_x,
                            WIDTH / 2 + character.player_sprite.center_x,
                            -HEIGHT / 2 + character.player_sprite.center_y,
                            HEIGHT / 2 + character.player_sprite.center_y)
        character.player_movement()
        zombie_1.follow_player()
        zombie_1.zombie_attack(1 / 60)
        character.player_death()
        gun.equip()
        print(f"Gun Equipped: {gun.equipped}")
        print(f"({weapon_distance_x}, {weapon_distance_y})")


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
        gun.draw()



def on_key_press(key, modifiers):
    global character, SCREEN, weapon_distance_x, weapon_distance_y
    if SCREEN == "Game":
        if key == arcade.key.W:
            character.player_sprite.change_y = 6
        elif key == arcade.key.A:
            character.player_sprite.change_x = -6
        elif key == arcade.key.D:
            character.player_sprite.change_x = 6
        elif key == arcade.key.S:
            character.player_sprite.change_y = -6

        if weapon_distance_x <= 5 and weapon_distance_x <= 5:
            if key == arcade.key.E:
                gun.equipped = True


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

    


if __name__ == '__main__':
    setup()
