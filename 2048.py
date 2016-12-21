import arcade
from world import World
from worldrenderer import WorldRenderer
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 660

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.world_renderer = WorldRenderer(self.world, SCREEN_WIDTH, SCREEN_HEIGHT)
 
    def on_draw(self):
        arcade.start_render()
        self.world_renderer.draw()

    def animate(self, delta):
        self.world.animate(delta)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
 
if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
