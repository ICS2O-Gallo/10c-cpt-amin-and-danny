import os
import arcade


WIDTH = 1300
HEIGHT = 700


file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

tile_img = arcade.load_texture('/home/robuntu/Hosseini/untitled/download.jpeg')


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw

    arcade.run()
    
def update(delta_time):
    pass

def on_draw():
    arcade.start_render()
    arcade.draw_xywh_rectangle_textured(100, 200, tile_img.width, tile_img.height, tile_img)
