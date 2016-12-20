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
 
        self.background = arcade.Sprite('asset/b1.png')
        self.background.set_position(400, 300)

        self.star_sprite = ModelSprite('asset/s'+(str)(1)+'.png',model=self.world.star)
        self.star_sprite2 = ModelSprite('asset/s'+(str)(1)+'.png',model=self.world.star2)
        self.star_sprite3 = ModelSprite('asset/s'+(str)(1)+'.png',model=self.world.star3)
        self.star_sprite4 = ModelSprite('asset/s'+(str)(1)+'.png',model=self.world.star4)

    def draw(self):
        self.background.draw()
        self.star_sprite.draw()
        self.star_sprite2.draw()
        self.star_sprite3.draw()
        self.star_sprite4.draw()
