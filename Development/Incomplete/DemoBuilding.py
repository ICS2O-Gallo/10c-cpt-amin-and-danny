import os
import arcade

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)
tile_img = arcade.load_texture('/home/robuntu/Hosseini/untitled/download.jpeg')
arcade.draw_xywh_rectangle_textured(x, y, tile_img.width, tile_img.height, tile_img)
