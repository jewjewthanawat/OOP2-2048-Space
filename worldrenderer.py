import arcade
from world import World

class WorldRenderer:
    def __init__(self, world, width, height):
        self.world = world
        self.width = width
        self.height = height

        self.set_asset()

    def draw(self):
        if self.world.max <= 1024:
            self.background[0].draw()
        if self.world.max <= 2048:
            self.background[1].draw()
        if self.world.max <= 4096:
            self.background[2].draw()
        if self.world.max > 4096:
            self.background[3].draw()

        for i in range(len(self.world.star)):
            for j in range(len(self.world.star[i])):
                if self.world.star[i][j] != 0 :
                    arcade.draw_texture_rectangle(self.world.star[i][j].x, self.world.star[i][j].y, self.star_texture[self.world.star[i][j].value].width, self.star_texture[self.world.star[i][j].value].height, self.star_texture[self.world.star[i][j].value], 0)
                    arcade.draw_text(str(self.world.star[i][j].value), self.world.star[i][j].x, self.world.star[i][j].y, arcade.color.BLACK, font_size=40, bold=True, align="center", anchor_x="center", anchor_y="center")

    def set_asset(self):
        self.background = []

        for i in range(4):
            self.background.append(arcade.Sprite('asset/b'+(str)(i+1)+'.png'))
            self.background[i].set_position(400, 300)

        self.star_texture = {}
        for i in range(12):
            self.star_texture[2**(i+1)] = arcade.load_texture('asset/s'+(str)(i+1)+'.png')
        for i in range(12,17):    
            self.star_texture[2**(i+1)] = arcade.load_texture('asset/s12.png')
