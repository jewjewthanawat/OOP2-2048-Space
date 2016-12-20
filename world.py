class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.star = Star(100,650)
        self.star2 = Star(300,650)
        self.star3 = Star(500,650)
        self.star4 = Star(700,650)
 
    def animate(self, delta):
        self.star.animate(delta)
        self.star2.animate(delta)
        self.star3.animate(delta)
        self.star4.animate(delta)

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def animate(self, delta):
        self.y -= 5
        if (self.y <= -50):
            self.y = 650

