import arcade
from world import World

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

class WorldRenderer:
    def __init__(self, world, width, height):
        self.world = world
        self.width = width
        self.height = height

        self.set_asset()

    def draw(self):
        if self.world.state == 1:
            self.background[0].draw()
        if self.world.state == 2:
            self.background[1].draw()
        if self.world.state == 3:
            self.background[2].draw()
        if self.world.state == 4:
            self.background[3].draw()

        for i in range(4):
            self.star_sprite[i].draw()
            arcade.draw_text(str(i+10), self.star_sprite[i].model.x, self.star_sprite[i].model.y, arcade.color.BLACK, font_size=40, bold=True, align="center", anchor_x="center", anchor_y="center")

    def set_asset(self):
        self.background = []

        for i in range(4):
            self.background.append(arcade.Sprite('asset/b'+(str)(i+1)+'.png'))
            self.background[i].set_position(400, 300)

        self.star_sprite = []
        for i in range(4):
            self.star_sprite.append(ModelSprite('asset/s'+(str)(i+8)+'.png',model=self.world.star[i]))
