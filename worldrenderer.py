import arcade
from world import World

class WorldRenderer:
    def __init__(self, world, width, height):
        self.world = world
        self.width = width
        self.height = height

        self.set_asset()

    def draw(self):
        if self.world.max <= 512:
            self.background[0].draw()
        elif self.world.max <= 1024:
            self.background[1].draw()
        elif self.world.max <= 2048:
            self.background[2].draw()
        else:
            self.background[3].draw()

        if self.world.state == -1:
            arcade.draw_texture_rectangle(400, 330, self.item_texture[8].width, self.item_texture[8].height, self.item_texture[8], 0)
            if self.world.tutorial:
                arcade.draw_texture_rectangle(400, 330, self.item_texture[10].width, self.item_texture[10].height, self.item_texture[10], 0)
        else:
            for i in range(len(self.world.star)):
                for j in range(len(self.world.star[i])):
                    if self.world.star[i][j] != 0:
                        if self.world.star[i][j].charge: #and self.world.star[i][j].value <= 32 and self.world.star[i][j].value > 0:
                            arcade.draw_texture_rectangle(self.world.star[i][j].x, self.world.star[i][j].y, self.item_texture[3].width, self.item_texture[3].height, self.item_texture[3], 0)
                        arcade.draw_texture_rectangle(self.world.star[i][j].x, self.world.star[i][j].y, self.star_texture[self.world.star[i][j].value].width, self.star_texture[self.world.star[i][j].value].height, self.star_texture[self.world.star[i][j].value], 0)
                        if self.world.star[i][j].lock:
                            arcade.draw_texture_rectangle(self.world.star[i][j].x, self.world.star[i][j].y, self.item_texture[2].width, self.item_texture[2].height, self.item_texture[2], 0)
                        #arcade.draw_text(str(self.world.star[i][j].value), self.world.star[i][j].x, self.world.star[i][j].y, arcade.color.BLACK, font_size=40, bold=True, align="center", anchor_x="center", anchor_y="center")
            if self.world.black_hole.appear:
                arcade.draw_texture_rectangle(self.world.black_hole.real_x1, self.world.black_hole.real_y1, self.item_texture[self.world.black_hole.type1].width, self.item_texture[self.world.black_hole.type1].height, self.item_texture[self.world.black_hole.type1], 0)
                arcade.draw_texture_rectangle(self.world.black_hole.real_x2, self.world.black_hole.real_y2, self.item_texture[self.world.black_hole.type2].width, self.item_texture[self.world.black_hole.type2].height, self.item_texture[self.world.black_hole.type2], 0)
            arcade.draw_text("score", 730, 600, arcade.color.GREEN, 40, align = "center", bold = True, anchor_x = "center", anchor_y = "center")
            arcade.draw_text(str(self.world.score), 730, 550, arcade.color.GREEN, 30, align = "center", bold = True, anchor_x = "center", anchor_y = "center")
            if self.world.count - self.world.last_count0 >= 25:
                arcade.draw_texture_rectangle(730, 440, self.star_texture[-3].width, self.star_texture[-3].height, self.star_texture[-3], 0)
                arcade.draw_texture_rectangle(730, 440, self.item_texture[6].width, self.item_texture[6].height, self.item_texture[6], 0)
            else:
                arcade.draw_texture_rectangle(730, 440, self.item_texture[4].width, self.item_texture[4].height, self.item_texture[4], 0)
            if self.world.count - self.world.last_count1 >= 25:
                arcade.draw_texture_rectangle(730, 220, 100, 100, self.item_texture[3], 0)
                arcade.draw_texture_rectangle(730, 220, self.item_texture[7].width, self.item_texture[7].height, self.item_texture[7], 0)
            else:
                arcade.draw_texture_rectangle(730, 220, 100, 100, self.item_texture[5], 0)
            if self.world.state == 0 or self.world.state == 7 or self.world.state == 8:
                if self.world.state == 0:
                    arcade.draw_texture_rectangle(330, 330, self.item_texture[9].width, self.item_texture[9].height, self.item_texture[9], 0)
                elif self.world.state == 7:
                    arcade.draw_texture_rectangle(330, 330, self.item_texture[11].width, self.item_texture[11].height, self.item_texture[11], 0)
                else:
                    arcade.draw_texture_rectangle(330, 330, self.item_texture[12].width, self.item_texture[12].height, self.item_texture[12], 0)
                arcade.draw_text("your score : "+(str)(self.world.score)+"    your max star value :"+(str)(self.world.max), 330, 410, arcade.color.GREEN, 20, align = "center", bold = True, anchor_x = "center", anchor_y = "center")
                if self.world.tutorial:
                    arcade.draw_texture_rectangle(400, 330, self.item_texture[10].width, self.item_texture[10].height, self.item_texture[10], 0)
            
    def set_asset(self):
        self.background = []

        for i in range(4):
            self.background.append(arcade.Sprite('asset/b'+(str)(i+1)+'.png'))
            self.background[i].set_position(400, 330)

        self.star_texture = {}
        for i in range(17):
            self.star_texture[2**(i+1)] = arcade.load_texture('asset/s'+(str)(i+1)+'.png')
        #for i in range(12,17):    
        #    self.star_texture[2**(i+1)] = arcade.load_texture('asset/s12.png')
        self.star_texture[-3] = arcade.load_texture('asset/h4.png')
        self.star_texture[-2] = arcade.load_texture('asset/h5.png')
        self.star_texture[-1] = arcade.load_texture('asset/h6.png')

        self.item_texture = {}
        for i in range(4):
            self.item_texture[i] = arcade.load_texture('asset/h'+(str)(i)+'.png')
        self.item_texture[4] = arcade.load_texture('asset/h7.png')
        self.item_texture[5] = arcade.load_texture('asset/h8.png')
        self.item_texture[6] = arcade.load_texture('asset/p0.png')
        self.item_texture[7] = arcade.load_texture('asset/p1.png')

        self.item_texture[8] = arcade.load_texture('asset/first.png')
        self.item_texture[9] = arcade.load_texture('asset/over.png')
        self.item_texture[10] = arcade.load_texture('asset/tutorial.png')
        self.item_texture[11] = arcade.load_texture('asset/pause.png')
        self.item_texture[12] = arcade.load_texture('asset/win.png')
