import os
import arcade


WIDTH = 1300
HEIGHT = 700

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

background = arcade.load_texture('Assets\\floor.png')


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
        self.tile_img = arcade.load_texture('Assets\\background.jpeg')

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
            arcade.draw_xywh_rectangle_filled(self.player_sprite.center_x - (self.player_sprite.width / 2.5),
                                              self.player_sprite.center_y + (self.player_sprite.height / 2),
                                              100, 5, arcade.color.RED)
            arcade.draw_xywh_rectangle_filled(self.player_sprite.center_x - (self.player_sprite.width / 2.5),
                                              self.player_sprite.center_y + (self.player_sprite.height / 2),
                                              self.health, 5, arcade.color.GREEN)

    def player_movement(self):
        #CHANGES SPRITE'S X AND Y POSITIONS
        self.player_sprite.center_x += self.player_sprite.change_x
        self.player_sprite.center_y += self.player_sprite.change_y



class Weapon(object):
    def __init__(self, sprite_1, sprite_2, size, x, y, equipped, ammo, reload_rate, character, type_of_bullet, bullet_list):
        self.character = character
        #CREATES  SPRITE AND GIVES X AND Y POSITIONS
        self.size = size
        self.sprites = [sprite_1, sprite_2]
        self.weapon = arcade.Sprite(self.sprites[self.character.orientation], self.size)
        self.weapon.center_x = x
        self.weapon.center_y = y

        self.equipped = equipped
        self.attacking = False
        #STATS
        self.ammo = ammo
        self.reload_rate = reload_rate
        #THIS IS USED SO THE WEAPON OBJECT CAN REFERENCE THE CHARACTER In FUNCTION
        self.bullet_sprite = type_of_bullet[0]
        self.bullet_size = type_of_bullet[1]
        self.bullet_damage = type_of_bullet[2]
        self.bullet_zombie_list = type_of_bullet[3]
        self.bullet_list = bullet_list

    def draw(self):
        
        self.weapon.draw()

            
    def equip(self):
        #ATTACHES WEAPON TO CHARACTER
        if self.equipped:
            self.weapon.center_x = self.character.player_sprite.center_x - 30
            self.weapon.center_y = self.character.player_sprite.center_y 

            self.weapon.change_x = self.character.player_sprite.change_x
            self.weapon.change_x = self.character.player_sprite.change_y
            

    def shoot(self):
        while len(self.bullet_list) == 
            if self.attacking:
                self.bullet_list.append(Bullet(self.bullet_sprite, self.bullet_size, self.character.orientation, self.bullet_damage, self.bullet_zombie_list, self.bullet_list, self.weapon.center_x - 10, self.weapon.center_y))


class Bullet(object):
    def __init__(self, sprite, size, orientation, damage, zombie_list, bullet_list, x= 10, y = 10):
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
                    if self.sprite.center_x == zombie.sprite.center_x and zombie.sprite.center_y - 27 < self.sprite.center_y < zombie.sprite.center_y + 27:
                        zombie.is_attacked = True
                        print("ATTACKED")
                        zombie.health -= self.damage
                        self.bullet_list.remove(self)


class Zombie(object):
    def __init__(self, sprite, size, x, y, health, character, zombie_list, damage=5):
        #CREATES SPRITE
        self.orientation = False
        self.sprite = arcade.Sprite(sprite, size)
        self.sprite.center_x = x
        self.sprite.center_y = y
        #REFRENCES CHARACTER SO ZOMBIE CAN GET ITS X AND Y POSI
        self.character = character
        self.zombie_list = zombie_list
        self.zombie_list.append(self)

        self.health = health
        self.damage = damage
        self.is_attacked = False

    def draw(self):
        self.sprite.draw()
        if self.is_attacked:
            arcade.draw_xywh_rectangle_filled(self.sprite.center_x - (self.sprite.width / 2.5),
                                              self.sprite.center_y + (self.sprite.height / 2),
                                              100, 5, arcade.color.RED)
            arcade.draw_xywh_rectangle_filled(self.sprite.center_x - (self.sprite.width / 2.5),
                                              self.sprite.center_y + (self.sprite.height / 2),
                                              self.health, 5, arcade.color.GREEN)

    def follow_player(self):

        self.distance_from_target_x = self.character.player_sprite.center_x - self.sprite.center_x
        self.distance_from_target_y = self.character.player_sprite.center_y - self.sprite.center_y

        if self.distance_from_target_x > 36:
            self.sprite.change_x = 2
        elif self.distance_from_target_x < -36:
            self.sprite.change_x = -2
            #CHANGES THE DIRECTION THE SPRITE IS FACING
            # self.sprite.set_texture(1)

        if self.distance_from_target_y > 36:
            self.sprite.change_y = 2
        elif self.distance_from_target_y < -36:
            self.sprite.change_y = -2

        if -36 < self.distance_from_target_x < 36:
            self.sprite.change_x = 0

        if -36 < self.distance_from_target_y < 36:
            self.sprite.change_y = 0
        
        self.sprite.center_x += self.sprite.change_x
        self.sprite.center_y += self.sprite.change_y

    def zombie_attack(self, delta_time):
        if -36 < self.distance_from_target_x < 36 and -36 < self.distance_from_target_y < 36:
            self.character.health -= self.damage * delta_time
            self.character.player_is_attacked = True
        else:
            self.character.player_is_attacked = False


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(WIDTH, HEIGHT)
        self.SCREEN = "Main Menu"
        self.main_screen = MainScreen()

        self.game = Background()

        self.zombie_list = []
        self.bullet_list = [] 
        # These are the four types of bullets and their attributes
        self.bullet_1 = ['Assets\shot.1.png', 1, 15, self.zombie_list]
        self.bullet_2 = ['Assets\shot.2.png', 1, 20, self.zombie_list]
        self.bullet_3 = ['Assets\shot.3.png', 1, 25, self.zombie_list]
        self.bullet_4 = ['Assets\shot.4.png', 1, 30, self.zombie_list]
        
        self.character = Player('Assets\player.png',1, 400, 100)
        self.zombie_1 = Zombie('Assets\zombie1.png', 1, 100, 200, 100, self.character, self.zombie_list)
        
        self.gun_1 = Weapon('Assets\gun.1.png', 'Assets\gun.1(2).png', 1, 200, 400, False, 5, 10, self.character, self.bullet_1, self.bullet_list)
        self.gun_2 = Weapon('Assets\gun.2.png', 'Assets\gun.2(2).png', 1, 200, 400, False, 5, 10, self.character, self.bullet_2, self.bullet_list)
        self.gun_3 = Weapon('Assets\gun.3.png', 'Assets\gun.3(2).png', 1, 200, 400, False, 5, 10, self.character, self.bullet_3, self.bullet_list)
        self.gun_4 = Weapon('Assets\gun.4.png', 'Assets\gun.4(2).png', 1, 200, 400, False, 5, 10, self.character, self.bullet_4, self.bullet_list)
        

        self.weapon_distance_x = abs(self.character.player_sprite.center_x - self.gun_1.weapon.center_x)
        self.weapon_distance_y = abs(self.character.player_sprite.center_y - self.gun_1.weapon.center_y)

    
    def update(self, delta_time):
        if self.SCREEN == "Game":
            self.weapon_distance_x = abs(self.character.player_sprite.center_x - self.gun_1.weapon.center_x)
            self.weapon_distance_y = abs(self.character.player_sprite.center_y - self.gun_1.weapon.center_y)

            arcade.set_viewport(-WIDTH / 2 + self.character.player_sprite.center_x,
                            WIDTH / 2 + self.character.player_sprite.center_x,
                            -HEIGHT / 2 + self.character.player_sprite.center_y,
                            HEIGHT / 2 + self.character.player_sprite.center_y)

            self.character.player_movement()

            self.gun_1.equip()
            self.gun_1.shoot()

            for bullet in self.bullet_list:
                bullet.shoot(1/60)

            for zombie in self.zombie_list:
                zombie.follow_player()
                zombie.zombie_attack(1 / 60)
                if zombie.health <= 0:
                    self.zombie_list.remove(zombie)
            
            if self.character.health <= 0:
                self.SCREEN = "Main Menu"

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
            for zombie in self.zombie_list:
                zombie.draw()
            for bullet in self.bullet_list:
                bullet.draw()



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

            if self.weapon_distance_x <= 36 and self.weapon_distance_x <= 36:
                if key == arcade.key.E:
                    self.gun_1.equipped = True

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

    def on_mouse_press(self, x, y, button, modifiers):
        if self.SCREEN == "Main Menu":
            if (self.main_screen.x < x < self.main_screen.x + self.main_screen.width and
                    self.main_screen.y + 200 < y < self.main_screen.y + self.main_screen.height + 200):
                self.SCREEN = "Game"
        if self.SCREEN == "Game":
            if self.gun_1.equipped:
                self.gun_1.attacking = True
                
    
    def on_mouse_release(self, x, y, button, modifiers):
        if self.SCREEN == "Game":
            if self.gun_1.equipped:
                self.gun_1.attacking = False



def main():
    window = MyGame()
    arcade.run()


if __name__ == '__main__':
    main()
