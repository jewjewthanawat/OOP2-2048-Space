import math
import arcade.key
from random import randint

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.n = 4
        self.state = 0
        self.star = []
        self.black_hole = BlackHole()
        self.blank_cell = []
        self.all_star = []
        self.new_game()

    def new_game(self):
        self.star.clear()
        for i in range(self.n):
            self.star.append([])
            for j in range(self.n):
                self.star[i].append(0)
        self.check_blank_cell()
        self.random = 0      
        self.max = 0
        self.count = 0

    def on_key_press(self, key, key_modifiers):
        if self.state == 0: #new game
            if key == arcade.key.SPACE:
                #reset game
                self.new_game()
                self.state = 1
        if self.state == 2: #ready to input
            if key == arcade.key.UP and self.can_move_up():
                self.count += 1
                for i in range(self.n):
                    self.checking_cell = 0
                    self.checking_cell_value = 0
                    for j in range(self.n):
                        if self.star[j][i] != 0:
                            if self.checking_cell_value == 0:
                                self.star[j][i].set_target_y(self.checking_cell)
                                self.star[j][i].set_vy()
                                self.checking_cell_value = self.star[j][i].value
                            elif self.checking_cell_value == self.star[j][i].value:
                                self.star[j][i].set_target_y(self.checking_cell)
                                self.star[j][i].set_vy()
                                self.checking_cell += 1
                                self.checking_cell_value = 0
                            else:
                                self.checking_cell += 1
                                self.star[j][i].set_target_y(self.checking_cell)
                                self.star[j][i].set_vy()
                                self.checking_cell_value = self.star[j][i].value
                self.state = 3
            elif key == arcade.key.DOWN and self.can_move_down():
                self.count += 1
                for i in range(self.n):
                    self.checking_cell = self.n-1
                    self.checking_cell_value = 0
                    for j in range(self.n):
                        if self.star[self.n-1-j][i] != 0:
                            if self.checking_cell_value == 0:
                                self.star[self.n-1-j][i].set_target_y(self.checking_cell)
                                self.star[self.n-1-j][i].set_vy()
                                self.checking_cell_value = self.star[self.n-1-j][i].value
                            elif self.checking_cell_value == self.star[self.n-1-j][i].value:
                                self.star[self.n-1-j][i].set_target_y(self.checking_cell)
                                self.star[self.n-1-j][i].set_vy()
                                self.checking_cell -= 1
                                self.checking_cell_value = 0
                            else:
                                self.checking_cell -= 1
                                self.star[self.n-1-j][i].set_target_y(self.checking_cell)
                                self.star[self.n-1-j][i].set_vy()
                                self.checking_cell_value = self.star[self.n-1-j][i].value
                self.state = 4
            elif key == arcade.key.LEFT and self.can_move_left():
                self.count += 1
                for i in range(self.n):
                    self.checking_cell = 0
                    self.checking_cell_value = 0
                    for j in range(self.n):
                        if self.star[i][j] != 0:
                            if self.checking_cell_value == 0:
                                self.star[i][j].set_target_x(self.checking_cell)
                                self.star[i][j].set_vx()
                                self.checking_cell_value = self.star[i][j].value
                            elif self.checking_cell_value == self.star[i][j].value:
                                self.star[i][j].set_target_x(self.checking_cell)
                                self.star[i][j].set_vx()
                                self.checking_cell += 1
                                self.checking_cell_value = 0
                            else:
                                self.checking_cell += 1
                                self.star[i][j].set_target_x(self.checking_cell)
                                self.star[i][j].set_vx()
                                self.checking_cell_value = self.star[i][j].value
                self.state = 5
            elif key == arcade.key.RIGHT and self.can_move_right():
                self.count += 1
                for i in range(self.n):
                    self.checking_cell = self.n-1
                    self.checking_cell_value = 0
                    for j in range(self.n):
                        if self.star[i][self.n-1-j] != 0:
                            if self.checking_cell_value == 0:
                                self.star[i][self.n-1-j].set_target_x(self.checking_cell)
                                self.star[i][self.n-1-j].set_vx()
                                self.checking_cell_value = self.star[i][self.n-1-j].value
                            elif self.checking_cell_value == self.star[i][self.n-1-j].value:
                                self.star[i][self.n-1-j].set_target_x(self.checking_cell)
                                self.star[i][self.n-1-j].set_vx()
                                self.checking_cell -= 1
                                self.checking_cell_value = 0
                            else:
                                self.checking_cell -= 1
                                self.star[i][self.n-1-j].set_target_x(self.checking_cell)
                                self.star[i][self.n-1-j].set_vx()
                                self.checking_cell_value = self.star[i][self.n-1-j].value
                self.state = 6
 
    def animate(self, delta):
        if self.state == 1: #gen star
            self.random = randint(0,len(self.blank_cell)-1)
            self.star[math.floor(self.blank_cell[self.random]/self.n)][self.blank_cell[self.random]%self.n] = Star(105+150*(self.blank_cell[self.random]%self.n), 555-150*math.floor(self.blank_cell[self.random]/self.n))
            self.check_blank_cell()
            if self.count % 6 == 0 and self.count != 0:
                self.black_hole.appear = True
                self.black_hole.type = randint(0,1)
                self.black_hole_range = [0,1,2,3]
                if self.black_hole.type == 0:
                    self.black_hole.x1 = randint(0,4)
                    self.black_hole.x2 = randint(0,4)
                    self.black_hole.y1 = randint(0,3)
                    self.black_hole_range.remove(self.black_hole.y1)
                    self.black_hole.y2 = self.black_hole_range[randint(0,2)]
                else:
                    self.black_hole.x1 = randint(0,3)
                    self.black_hole_range.remove(self.black_hole.x1)
                    self.black_hole.x2 = self.black_hole_range[randint(0,2)]
                    self.black_hole.y1 = randint(0,4)
                    self.black_hole.y2 = randint(0,4)
                self.black_hole.set_position()
            else:
                self.black_hole.appear = False
            if self.is_end():
                self.state = 0
            else:
                self.state = 2
        elif self.state == 3: #animate move up
            for i in range(self.n):
                for j in range(self.n):
                    if self.star[i][j] != 0:
                        if self.star[i][j].y < self.star[i][j].target:
                            self.star[i][j].y += self.star[i][j].v
                        if self.star[i][j].y > self.star[i][j].target:
                            self.star[i][j].y = self.star[i][j].target
            if self.is_all_y_stable():
                self.recalculate()
        elif self.state == 4: #animate move down
            for i in range(self.n):
                for j in range(self.n):
                    if self.star[i][j] != 0:
                        if self.star[i][j].y > self.star[i][j].target:
                            self.star[i][j].y += self.star[i][j].v
                        if self.star[i][j].y < self.star[i][j].target:
                            self.star[i][j].y = self.star[i][j].target
            if self.is_all_y_stable():
                self.recalculate()
        elif self.state == 5: #animate move left
            for i in range(self.n):
                for j in range(self.n):
                    if self.star[i][j] != 0:
                        if self.star[i][j].x > self.star[i][j].target:
                            self.star[i][j].x += self.star[i][j].v
                        if self.star[i][j].x < self.star[i][j].target:
                            self.star[i][j].x = self.star[i][j].target
            if self.is_all_x_stable():
                self.recalculate()
        elif self.state == 6: #animate move right
            for i in range(self.n):
                for j in range(self.n):
                    if self.star[i][j] != 0:
                        if self.star[i][j].x < self.star[i][j].target:
                            self.star[i][j].x += self.star[i][j].v
                        if self.star[i][j].x > self.star[i][j].target:
                            self.star[i][j].x = self.star[i][j].target
            if self.is_all_x_stable():
                self.recalculate()
                        

    def check_blank_cell(self):
        self.blank_cell.clear()
        for i in range(self.n):
            for j in range(self.n):
                if self.star[i][j] == 0:
                    self.blank_cell.append(self.n*i+j)

    def can_move_up(self):
        for i in range(self.n-1):
            for j in range(self.n):
                if self.star[self.n-1-i-1][j] == 0 and self.star[self.n-1-i][j] != 0:
                    return True
                if self.star[self.n-1-i][j] != 0 and self.star[self.n-1-i-1][j] != 0 and self.star[self.n-1-i][j].value == self.star[self.n-1-i-1][j].value:
                    return True
        return False

    def can_move_down(self):
        for i in range(self.n-1):
            for j in range(self.n):
                if self.star[i+1][j] == 0 and self.star[i][j] != 0:
                    return True
                if self.star[i][j] != 0 and self.star[i+1][j] != 0 and self.star[i][j].value == self.star[i+1][j].value:
                    return True
        return False

    def can_move_left(self):
        for i in range(self.n-1):
            for j in range(self.n):
                if self.star[j][i] == 0 and self.star[j][i+1] != 0:
                    return True
                if self.star[j][i] != 0 and self.star[j][i+1] != 0 and self.star[j][i].value == self.star[j][i+1].value:
                    return True
        return False

    def can_move_right(self):
        for i in range(self.n-1):
            for j in range(self.n):
                if self.star[j][self.n-1-i] == 0 and self.star[j][self.n-1-i-1] != 0:
                    return True
                if self.star[j][self.n-1-i] != 0 and self.star[j][self.n-1-i-1] != 0 and self.star[j][self.n-1-i].value == self.star[j][self.n-1-i-1].value:
                    return True
        return False

    def can_move(self):
        return self.can_move_up() or self.can_move_down() or self.can_move_left() or self.can_move_right()

    def is_all_x_stable(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.star[i][j] != 0 and self.star[i][j].x != self.star[i][j].target:
                    return False
        return True
    
    def is_all_y_stable(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.star[i][j] != 0 and self.star[i][j].y != self.star[i][j].target:
                    return False
        return True

    def recalculate(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.star[i][j] != 0:
                    self.merge_cell(i, j)
        self.all_star.clear()
        for i in range(self.n):
            for j in range(self.n):
                if self.star[i][j] != 0:
                    self.all_star.append(self.star[i][j])
                    self.for_del = self.star[i][j]
                    self.star[i][j] = 0
                    del self.for_del
        for i in range(len(self.all_star)):
            self.star[(int)((555 - self.all_star[i].y)/150)][(int)((self.all_star[i].x - 105)/150)] = self.all_star[i]
        self.check_blank_cell()
        self.state = 1

    def merge_cell(self, i, j):
        for k in range(self.n):
            for l in range(self.n):
                if self.star[k][l] != 0 and (k != i or l != j) and self.star[k][l].x == self.star[i][j].x and self.star[k][l].y == self.star[i][j].y:
                    self.star[i][j].value *= 2
                    if self.star[i][j].value > self.max:
                        self.max = self.star[i][j].value
                    self.star[k][l] = 0
                    return
                    
    def is_end(self):
        return (len(self.blank_cell) == 0) and (not self.can_move())

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.target = -1
        self.v = 0
        if randint(1,4) == 4:
            self.value = 4
        else:
            self.value = 2

    def set_vx(self):
        self.v = (self.target - self.x)/5

    def set_vy(self):
        self.v = (self.target - self.y)/5

    def set_target_x(self, cell):
        self.target = 105+150*cell

    def set_target_y(self, cell):
        self.target = 555-150*cell

class BlackHole:
    def __init__(self):
        self.appear = False
        self.type = 0
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
        self.real_x1 = 0
        self.real_x2 = 0
        self.real_y1 = 0
        self.real_y2 = 0

    def set_position(self):
        if self.type == 0:
            self.real_x1 = 30+150*self.x1
            self.real_x2 = 30+150*self.x2
            self.real_y1 = 555-150*self.y1
            self.real_y2 = 555-150*self.y2
        else:
            self.real_x1 = 105+150*self.x1
            self.real_x2 = 105+150*self.x2
            self.real_y1 = 630-150*self.y1
            self.real_y2 = 630-150*self.y2
