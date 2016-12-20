import arcade.key

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.state = 0

        self.star = []

        for i in range(4):
            self.star.append(Star(100+200*i,650))
 
    def animate(self, delta):
        for i in range(4):
            self.star[i].animate(delta, self.state)

    def on_key_press(self, key, key_mod):
        if key == arcade.key.UP:
            self.state = 1
        if key == arcade.key.DOWN:
            self.state = 2
        if key == arcade.key.LEFT:
            self.state = 3
        if key == arcade.key.RIGHT:
            self.state = 4

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def animate(self, delta, state):
        if state == 0:
            self.y += 5
            if self.y >= 650:
                self.y = -50
        if state == 1:
            self.y += 5
            if self.y >= 650:
                self.y = -50
        if state == 2:
            self.y -= 5
            if self.y <= -50:
                self.y = 650
        if state == 3:
            self.x -= 5
            if self.x <= -50:
                self.x = 850
        if state == 4:
            self.x += 5
            if self.x >= 850:
                self.x = -50

