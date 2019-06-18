import os
import arcade
import random

WIDTH = 1300
HEIGHT = 700

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

background = arcade.load_texture('Assets\\background.jpeg')

floor = arcade.load_texture('Assets\\floor.png')
left_wall = arcade.load_texture('Assets\\left wall.png')
right_wall = arcade.load_texture('Assets\\right wall.png')
under_wall = arcade.load_texture('Assets\\under wall.png')
coner_wall = arcade.load_texture('Assets\\coner wall.png')
upper_wall = arcade.load_texture('Assets\\upper wall.png')


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

    def draw(self):
        # TITLE
        arcade.draw_text("ZombiE", self.x, 530, arcade.color.YELLOW, 100)
        # START BUTTON
        arcade.draw_xywh_rectangle_filled(
            self.x, self.y + 200, self.width,
            self.height, arcade.color.BATTLESHIP_GREY)
        arcade.draw_text(
            "NEW  GAME", self.font_x - (25 / 8 * self.font_size),
            self.font_y + 200, arcade.color.BLACK,
            self.font_size, font_name="TIMES NEW ROMAN")


class GameOverScreen(object):
    def __init__(self):
        self.x = WIDTH / 3
        self.y = HEIGHT / 3
        self.width = WIDTH / 3
        self.height = HEIGHT / 12
        self.font_size = (self.width * self.height) * (1 / 728)

    def draw_gameover_screen(self):
        arcade.draw_text(
            "You Died!", self.x, 530,
            arcade.color.RED_DEVIL, self.font_size * 2.5,
            font_name="TIMES NEW ROMAN")


class Background(object):
    def __init__(self):
        self.whole_map_x = -1 * WIDTH
        self.whole_map_y = -1 * HEIGHT
        self.whole_map_width = WIDTH * 3
        self.whole_map_length = HEIGHT * 3
        self.tile_img = arcade.load_texture('Assets\\background.jpeg')

    def draw_background(self):
        # TILES
        for x in range(
                self.whole_map_x, self.whole_map_x + self.whole_map_width,
                self.tile_img.width):
            for y in range(
                    self.whole_map_y, self.whole_map_y + self.whole_map_length,
                    self.tile_img.height):
                arcade.draw_xywh_rectangle_textured(
                    x, y, self.tile_img.width,
                    self.tile_img.height, self.tile_img)
        # BUILDING
        # Floor
        arcade.draw_xywh_rectangle_textured(
            375, 100, floor.width + 350, floor.height + 250, floor)
        # Left wall
        for x in range(500, WIDTH, left_wall.width):
            for y in range(500, HEIGHT, left_wall.height):
                arcade.draw_xywh_rectangle_textured(
                    375 - 125, 100, left_wall.width - 100,
                    left_wall.height + 250, left_wall)
        # Right wall
        for x in range(500, WIDTH, right_wall.width):
            for y in range(500, HEIGHT, right_wall.height):
                arcade.draw_xywh_rectangle_textured(
                    375 + 575, 100, right_wall.width - 100,
                    right_wall.height + 250, right_wall)
        # Upper wall
        for x in range(500, WIDTH, upper_wall.width):
            for y in range(500, HEIGHT, upper_wall.height):
                arcade.draw_xywh_rectangle_textured(375, 100 + 475,
                                                    upper_wall.width + 350,
                                                    upper_wall.height - 120,
                                                    upper_wall)
        # Under wall
        for x in range(500, WIDTH, under_wall.width):
            for y in range(500, HEIGHT, under_wall.height):
                arcade.draw_xywh_rectangle_textured(375, 100 - 105,
                                                    under_wall.width + 350,
                                                    under_wall.height - 120,
                                                    under_wall)
        # Coner Wall (Upper left)
        for x in range(500, WIDTH, coner_wall.width):
            for y in range(500, HEIGHT, coner_wall.height):
                arcade.draw_xywh_rectangle_textured(250, 100 + 475,
                                                    coner_wall.width + 5,
                                                    coner_wall.height - 15,
                                                    coner_wall)
        # Coner Wall (Upper right)
        for x in range(500, WIDTH, coner_wall.width):
            for y in range(500, HEIGHT, coner_wall.height):
                arcade.draw_xywh_rectangle_textured(950, 100 + 475,
                                                    coner_wall.width + 5,
                                                    coner_wall.height - 15,
                                                    coner_wall)
        # Coner Wall (Under left)
        for x in range(500, WIDTH, coner_wall.width):
            for y in range(500, HEIGHT, coner_wall.height):
                arcade.draw_xywh_rectangle_textured(250, 100 - 105,
                                                    coner_wall.width + 5, 
                                                    coner_wall.height - 15,
                                                    coner_wall)
        # Coner Wall (Under right)
        for x in range(500, WIDTH, coner_wall.width):
            for y in range(500, HEIGHT, coner_wall.height):
                arcade.draw_xywh_rectangle_textured(950, 100 - 105,
                                                    coner_wall.width + 5, 
                                                    coner_wall.height - 15,
                                                    coner_wall)


class Player(object):
    def __init__(self, sprite, size, x, y):
        # CREATES CHARACTER SPRITE AND ASSIGNS X AND Y VALUES
        self.player_sprite = arcade.Sprite(sprite, size)
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

        self.player_is_attacked = False
        self.health = 100
        self.orientation = -1

    def draw(self):
        self.player_sprite.draw()
        # health bar
        if self.player_is_attacked:
            arcade.draw_xywh_rectangle_filled(self.player_sprite.center_x
                                             -(self.player_sprite.width / 2.5),
                                              self.player_sprite.center_y
                                              + (self.player_sprite.height / 2),
                                              100, 5, arcade.color.RED)
            arcade.draw_xywh_rectangle_filled(self.player_sprite.center_x
                                              -(self.player_sprite.width / 2.5),
                                              self.player_sprite.center_y +
                                              (self.player_sprite.height / 2),
                                              self.health, 5, 
                                              arcade.color.GREEN)

    def player_movement(self):
        # CHANGES SPRITE'S X AND Y POSITIONS
        self.player_sprite.center_x += self.player_sprite.change_x
        self.player_sprite.center_y += self.player_sprite.change_y


class Weapon(object):
    def __init__(self, sprite_1, sprite_2, size, x, y, equipped, ammo, 
                fire_rate, character, type_of_bullet,
                 bullet_list):
        self.character = character
        # CREATES  SPRITE AND GIVES X AND Y POSITIONS
        self.size = size
        self.sprites = [sprite_1, sprite_2]
        self.weapon = arcade.Sprite(self.sprites[self.character.orientation],
                                    self.size)
        self.weapon.center_x = x
        self.weapon.center_y = y

        self.equipped = equipped
        self.attacking = False
        # STATS
        self.current_ammo = ammo
        self.full_clip = ammo
        self.fire_rate = fire_rate
        self.reload = False
        self.orientation = 1
        # THIS IS USED SO THE WEAPON OBJECT CAN REFERENCE THE CHARACTER
        # In FUNCTION
        self.bullet_sprite = type_of_bullet[0]
        self.bullet_size = type_of_bullet[1]
        self.bullet_damage = type_of_bullet[2]
        self.bullet_zombie_list = type_of_bullet[3]
        self.bullet_list = bullet_list

    def draw(self):
        if not self.equipped:
            arcade.draw_text("You need to equip a gun. Press E",
                             self.character.player_sprite.center_x,
                             self.character.player_sprite.center_y +
                             (self.character.player_sprite.height / 2),
                             arcade.color.WHITE, 10,
                             font_name="TIMES_NEW_ROMAN")
        elif self.current_ammo == 0:
            arcade.draw_text("You need to reload. Press R",
                             self.weapon.center_x, 
                             self.character.player_sprite.center_y +
                             (self.character.player_sprite.height /
                              2), arcade.color.WHITE, 10,
                             font_name="TIMES_NEW_ROMAN")
        elif self.current_ammo == self.full_clip:
            arcade.draw_text("Press Z or X to shoot", self.weapon.center_x,
                             self.character.player_sprite.center_y +
                             (self.character.player_sprite.height /
                              2), arcade.color.WHITE, 10,
                             font_name="TIMES_NEW_ROMAN")
        self.weapon.draw()

    def equip(self):
        # ATTACHES WEAPON TO CHARACTER
        if self.equipped:
            self.weapon.center_x = self.character.player_sprite.center_x - 30
            self.weapon.center_y = self.character.player_sprite.center_y

            self.weapon.change_x = self.character.player_sprite.change_x
            self.weapon.change_x = self.character.player_sprite.change_y

    def shoot(self, delta_time):
        if self.current_ammo > 0:
            if self.attacking:
                self.bullet_list.append(Bullet(self.bullet_sprite,
                                               self.bullet_size, 
                                               self.bullet_damage, 
                                               self.orientation,
                                               self.bullet_zombie_list, 
                                               self.bullet_list,
                                               self.weapon.center_x - 10, 
                                               self.weapon.center_y))
                self.current_ammo -= 1
        if self.reload:
            self.current_ammo = self.full_clip


class Bullet(object):
    def __init__(self, sprite, size, damage, orientation, zombie_list,
                 bullet_list, x, y):
        self.sprite = arcade.Sprite(sprite, size)
        self.sprite.center_x = x
        self.sprite.center_y = y
        self.damage = damage
        self.speed = 11
        self.zombie_list = zombie_list
        self.bullet_list = bullet_list
        self.orientation = orientation

    def draw(self):
        self.sprite.draw()

    def shoot(self, delta_time):
        self.sprite.change_x = self.speed * self.orientation
        self.sprite.center_x += self.sprite.change_x
        for zombie in self.zombie_list:
            if zombie.health > 0:
                if zombie.sprite.center_x - 16 <= self.sprite.center_x <= zombie.sprite.center_x + 16 \
                    and zombie.sprite.center_y - 23 < self.sprite.center_y < zombie.sprite.center_y + 23:
                    zombie.is_attacked = True
                    zombie.health -= self.damage


class Zombie(object):
    def __init__(self, sprite, size, x, y, health, speed, character, 
                 zombie_list, damage=5):
        # CREATES SPRITE
        self.sprite = arcade.Sprite(sprite, size)
        self.sprite.center_x = x
        self.sprite.center_y = y
        # REFRENCES CHARACTER SO ZOMBIE CAN GET ITS X AND Y POSI
        self.character = character
        self.distance_from_target_y = self.character.player_sprite.center_y - self.sprite.center_y
        self.distance_from_target_x = self.character.player_sprite.center_x - self.sprite.center_x

        self.zombie_list = zombie_list
        self.zombie_list.append(self)

        self.speed = speed
        self.health = health
        self.damage = damage
        self.is_attacked = False

    def draw(self):
        self.sprite.draw()
        if self.is_attacked:
            arcade.draw_xywh_rectangle_filled(self.sprite.center_x -
                                              (self.sprite.width / 2.5),
                                              self.sprite.center_y +
                                              (self.sprite.height / 2),
                                              100, 5, arcade.color.RED)
            arcade.draw_xywh_rectangle_filled(self.sprite.center_x -
                                              (self.sprite.width / 2.5),
                                              self.sprite.center_y +
                                              (self.sprite.height / 2),
                                              self.health, 5,
                                              arcade.color.GREEN)

    def follow_player(self):

        if self.distance_from_target_x > 36:
            self.sprite.change_x = self.speed
        elif self.distance_from_target_x < -36:
            self.sprite.change_x = -1 * self.speed

        if self.distance_from_target_y > 36:
            self.sprite.change_y = self.speed
        elif self.distance_from_target_y < -36:
            self.sprite.change_y = -1 * self.speed

        if -36 < self.distance_from_target_x < 36:
            self.sprite.change_x = 0

        if -36 < self.distance_from_target_y < 36:
            self.sprite.change_y = 0

        self.sprite.center_x += self.sprite.change_x
        self.sprite.center_y += self.sprite.change_y

    def zombie_attack(self, delta_time):
        if self.character.health > 0:
            if -36 < self.distance_from_target_x < 36 \
                    and -36 < self.distance_from_target_y < 36:
                self.character.health -= self.damage / 5
                self.character.player_is_attacked = True
            else:
                self.character.player_is_attacked = False


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(WIDTH, HEIGHT)
        self.SCREEN = "Main Menu"
        self.waves = [(2, 0, 0, 0), (3, 1, 0, 0), (5, 1, 0, 0),
                      (7, 2, 1, 0), (11, 3, 1, 0), (13, 4, 1, 1), (17, 5, 2, 1),
                      (19, 6, 2, 1), (23, 7, 3, 1), (29, 9, 4, 2)]
        self.wave_number = 0
        self.current_wave = self.waves[self.wave_number]
        self.main_screen = MainScreen()
        self.game_over = GameOverScreen()

        self.character = Player('Assets\\player.png', 1, 650, 650)
        self.game = Background()

        self.zombie_list = []
        self.bullet_list = []
        # These are the four types of bullets and their attributes
        self.bullet_1 = ['Assets\\shot.1.png', 1, 15, self.zombie_list]
        self.bullet_2 = ['Assets\\shot.2.png', 1, 20, self.zombie_list]
        self.bullet_3 = ['Assets\\shot.3.png', 1, 25, self.zombie_list]
        self.bullet_4 = ['Assets\\shot.4.png', 1, 30, self.zombie_list]

        self.zombie_1 = ['Assets\\zombie1.png', 1,
                         random.randrange(-1 * WIDTH, WIDTH * 3),
                         random.randrange(-1 * HEIGHT, HEIGHT * 3), 100, 2,
                         self.character, self.zombie_list, 2]
        self.zombie_2 = ['Assets\\zombie2.png', 1,
                         random.randrange(-1 * WIDTH, WIDTH * 3),
                         random.randrange(-1 * HEIGHT, HEIGHT * 3), 100, 3,
                         self.character, self.zombie_list, 1]
        self.zombie_3 = ['Assets\\zombie3.png', 1,
                         random.randrange(-1 * WIDTH, WIDTH * 3),
                         random.randrange(-1 * HEIGHT, HEIGHT * 3), 100, 2,
                         self.character, self.zombie_list, 5]
        self.zombie_4 = ['Assets\\zombie4.png', 1,
                         random.randrange(-1 * WIDTH, WIDTH * 3),
                         random.randrange(-1 * HEIGHT, HEIGHT * 3), 1000, 1,
                         self.character, self.zombie_list, 6]

        self.gun_1 = Weapon('Assets\\gun.1.png', 'Assets\\gun.1(2).png', 1, 200,
                            400, False, 15, 10, self.character, self.bullet_1,
                            self.bullet_list)
        self.gun_2 = Weapon('Assets\\gun.2.png', 'Assets\\gun.2(2).png', 1, 200,
                            400, False, 15, 10, self.character, self.bullet_2,
                            self.bullet_list)
        self.gun_3 = Weapon('Assets\\gun.3.png', 'Assets\\gun.3(2).png', 1, 200,
                            400, False, 15, 10, self.character, self.bullet_3,
                            self.bullet_list)
        self.gun_4 = Weapon('Assets\\gun.4.png', 'Assets\\gun.4(2).png', 1,
                            200, 400, False, 15, 10, self.character,    
                            self.bullet_4, self.bullet_list)

        self.weapon_distance_x = abs(
            self.character.player_sprite.center_x - self.gun_1.weapon.center_x)
        self.weapon_distance_y = abs(
            self.character.player_sprite.center_y - self.gun_1.weapon.center_y)

    def wave(self):
        if self.SCREEN == "Game":
            while not self.zombie_list:
                for num in range(0, self.current_wave[0]):
                    self.zombie_list.append(Zombie(self.zombie_1[0],
                                                   self.zombie_1[1],
                                                   self.zombie_1[2],
                                                   self.zombie_1[3],
                                                   self.zombie_1[4],
                                                   self.zombie_1[5],
                                                   self.zombie_1[6],
                                                   self.zombie_1[7]))
                for num in range(0, self.current_wave[1]):
                    self.zombie_list.append(Zombie(self.zombie_2[0],
                                                   self.zombie_2[1],
                                                   self.zombie_2[2],
                                                   self.zombie_2[3],
                                                   self.zombie_2[4],
                                                   self.zombie_2[5],
                                                   self.zombie_2[6],
                                                   self.zombie_2[7]))
                for num in range(0, self.current_wave[2]):
                    self.zombie_list.append(Zombie(self.zombie_3[0],
                                                   self.zombie_3[1],
                                                   self.zombie_3[2],
                                                   self.zombie_3[3],
                                                   self.zombie_3[4],
                                                   self.zombie_3[5],
                                                   self.zombie_3[6],
                                                   self.zombie_3[7]))
                for num in range(0, self.current_wave[3]):
                    self.zombie_list.append(Zombie(self.zombie_4[0],
                                                   self.zombie_4[1],
                                                   self.zombie_4[2],
                                                   self.zombie_4[3],
                                                   self.zombie_4[4],
                                                   self.zombie_4[5],
                                                   self.zombie_4[6],
                                                   self.zombie_4[7]))

    def update(self, delta_time):
        if self.SCREEN == "Game":
            self.weapon_distance_x = abs(
                self.character.player_sprite.center_x - self.gun_1.weapon.center_x)
            self.weapon_distance_y = abs(
                self.character.player_sprite.center_y - self.gun_1.weapon.center_y)

            arcade.set_viewport(-WIDTH / 2 +
                                self.character.player_sprite.center_x,
                                WIDTH / 2 +
                                self.character.player_sprite.center_x,
                                -HEIGHT / 2 +
                                self.character.player_sprite.center_y,
                                HEIGHT / 2 +
                                self.character.player_sprite.center_y)

            self.character.player_movement()

            self.gun_1.equip()
            self.gun_1.shoot(self.gun_1.fire_rate)

            for bullet in self.bullet_list:
                bullet.shoot(1 / 60)
                if abs(bullet.sprite.center_x - self.character.player_sprite.center_x) >= WIDTH / 2 \
                   or abs(bullet.sprite.center_y - self.character.player_sprite.center_y) >= HEIGHT / 2:
                    self.bullet_list.remove(bullet)

            for zombie in self.zombie_list:
                if zombie.health <= 0:
                    self.zombie_list.remove(zombie)
                zombie.follow_player()
                zombie.zombie_attack(1 / 60)

            if self.character.health <= 0:
                self.SCREEN = "Game Over"

            if not self.zombie_list:
                self.wave_number += 1
                self.current_wave = self.waves[self.wave_number]
                self.wave()

    def on_draw(self):
        arcade.start_render()
        # Draw in here...
        if self.SCREEN == "Main Menu":
            arcade.set_viewport(0, WIDTH, 0, HEIGHT)
            arcade.set_background_color(arcade.color.WHITE)
            self.main_screen.draw()
        elif self.SCREEN == "Game":
            self.game.draw_background()
            self.character.draw()
            self.gun_1.draw()
            arcade.draw_text(f"Wave: {self.wave_number - 1}",
                             self.character.player_sprite.center_x,
                             self.character.player_sprite.center_y+HEIGHT/4,
                             arcade.color.RED, 50)
            for zombie in self.zombie_list:
                zombie.draw()
            for bullet in self.bullet_list:
                bullet.draw()
        elif self.SCREEN == "Game Over":
            arcade.set_viewport(0, WIDTH, 0, HEIGHT)
            self.game_over.draw_gameover_screen()
            self.character.health = 100
            self.wave_number = 0

    def on_key_press(self, key, modifiers):
        if self.SCREEN == "Game":
            if key == arcade.key.W:
                self.character.player_sprite.change_y = 6
            elif key == arcade.key.A:
                self.character.orientation = -1
                self.character.player_sprite.change_x = -6
            elif key == arcade.key.D:
                self.character.orientation = 1
                self.character.player_sprite.change_x = 6
            elif key == arcade.key.S:
                self.character.player_sprite.change_y = -6

            if self.weapon_distance_x <= 36 \
                    and self.weapon_distance_x <= 36:
                if key == arcade.key.E:
                    self.gun_1.equipped = True

            if self.gun_1.equipped:
                if key == arcade.key.R:
                    self.gun_1.reload = True

            if key == arcade.key.Z:
                self.gun_1.orientation = -1
                self.gun_1.attacking = True
            elif key == arcade.key.X:
                self.gun_1.orientation = 1
                self.gun_1.attacking = True

    def on_key_release(self, key, modifiers):
        if self.SCREEN == "Main Menu":
            if key == arcade.key.ENTER:
                self.SCREEN = "Game"
        elif self.SCREEN == "Game":
            if key == arcade.key.ESCAPE:
                self.SCREEN = "Main Menu"

        # Look over this
        if self.SCREEN == "Game":
            if key == arcade.key.W:
                self.character.player_sprite.change_y = 0
            elif key == arcade.key.A:
                self.character.player_sprite.change_x = 0
            elif key == arcade.key.D:
                self.character.player_sprite.change_x = 0
            elif key == arcade.key.S:
                self.character.player_sprite.change_y = 0

            if self.gun_1.equipped:
                if key == arcade.key.R:
                    self.gun_1.reload = False

            if key == arcade.key.Z or key == arcade.key.X:
                self.gun_1.attacking = False

    def on_mouse_press(self, mouse_x, mouse_y, button, modifiers):
        if self.SCREEN == "Main Menu":
            if (self.main_screen.x < mouse_x < self.main_screen.x + self.main_screen.width and
                self.main_screen.y + 200 < mouse_y < self.main_screen.y + self.main_screen.height + 200):
                self.SCREEN = "Game"

    def on_mouse_release(self, x, y, button, modifiers):
        if self.SCREEN == "Game":
            if self.gun_1.equipped:
                self.gun_1.attacking = False


def main():
    window = MyGame()
    arcade.run()


if __name__ == '__main__':
    main()
