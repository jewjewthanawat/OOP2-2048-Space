import math
import arcade
import arcade.key
from random import randint

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.n = 4
        self.state = -1
        self.tutorial = False
        self.is_finish = False
        self.max = 2049
        self.star = []
        self.black_hole = BlackHole()
        self.star_cell = []
        self.blank_cell = []
        self.all_star = []

    def new_game(self):
        self.star.clear()
        for i in range(self.n):
            self.star.append([])
            for j in range(self.n):
                self.star[i].append(0)
        self.check_blank_cell()
        self.random = 0
        self.score = 0
        self.max = 0
        self.count = 0
        self.last_count0 = 0
        self.last_count1 = 0
        self.lock_x = 0
        self.lock_y = 0
        self.sun = False
        self.is_finish = False

    def on_key_press(self, key, key_modifiers):
        if self.state == -1: #first page
            if key == arcade.key.SPACE:
                self.tutorial = False
                self.new_game()
                self.state = 1
            elif key == arcade.key.H:
                if self.tutorial:
                    self.tutorial = False
                else:
                    self.tutorial = True
        elif self.state == 0: #end game
            if key == arcade.key.SPACE:
                self.tutorial = False
                self.new_game()
                self.state = 1
            elif key == arcade.key.H:
                if self.tutorial:
                    self.tutorial = False
                else:
                    self.tutorial = True
        elif self.state == 2: #ready to input
            if key == arcade.key.UP and self.can_move_up():
                for i in range(self.n):
                    self.checking_cell = 0
                    self.checking_cell_value = 0
                    for j in range(self.n):
                        if self.star[j][i] != 0:
                            if self.star[j][i].lock:
                                self.checking_cell_value = self.star[j][i].value
                                self.checking_cell = j
                                self.star[j][i].set_target_y(self.checking_cell)
                            elif (self.black_hole.appear
                                  and ((self.black_hole.type1 == 1 and i == self.black_hole.x1 and j >= self.black_hole.y1)
                                       or (self.black_hole.type2 == 1 and i == self.black_hole.x2 and j >= self.black_hole.y2))):
                                if i == self.black_hole.x1:
                                    if i == self.lock_x and self.star[self.lock_y][i] != 0 and self.star[self.lock_y][i].lock and self.lock_y >= self.black_hole.y1 and j > self.lock_y:
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
                                    else:
                                        self.star[j][i].target = self.black_hole.real_y1
                                        self.star[j][i].set_vy()
                                else:
                                    if i == self.lock_x and self.star[self.lock_y][i] != 0 and self.star[self.lock_y][i].lock and self.lock_y >= self.black_hole.y2 and j > self.lock_y:
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
                                    else:
                                        self.star[j][i].target = self.black_hole.real_y2
                                        self.star[j][i].set_vy()
                            else:
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
                for i in range(self.n):
                    self.checking_cell = self.n-1
                    self.checking_cell_value = 0
                    for j in range(self.n):
                        if self.star[self.n-1-j][i] != 0:
                            if self.star[self.n-1-j][i].lock:
                                self.checking_cell_value = self.star[self.n-1-j][i].value
                                self.checking_cell = self.n-1-j
                                self.star[self.n-1-j][i].set_target_y(self.checking_cell)
                            elif (self.black_hole.appear
                                  and ((self.black_hole.type1 == 1 and i == self.black_hole.x1 and self.n-1-j < self.black_hole.y1)
                                       or (self.black_hole.type2 == 1 and i == self.black_hole.x2 and self.n-1-j < self.black_hole.y2))):
                                if i == self.black_hole.x1:
                                    if i == self.lock_x and self.star[self.lock_y][i] != 0 and self.star[self.lock_y][i].lock and self.lock_y < self.black_hole.y1 and self.n-1-j < self.lock_y:
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
                                    else:
                                        self.star[self.n-1-j][i].target = self.black_hole.real_y1
                                        self.star[self.n-1-j][i].set_vy()
                                else:
                                    if i == self.lock_x and self.star[self.lock_y][i] != 0 and self.star[self.lock_y][i].lock and self.lock_y < self.black_hole.y2 and self.n-1-j < self.lock_y:
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
                                    else:
                                        self.star[self.n-1-j][i].target = self.black_hole.real_y2
                                        self.star[self.n-1-j][i].set_vy()
                            else:
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
                for i in range(self.n):
                    self.checking_cell = 0
                    self.checking_cell_value = 0
                    for j in range(self.n):
                        if self.star[i][j] != 0:
                            if self.star[i][j].lock:
                                self.checking_cell_value = self.star[i][j].value
                                self.checking_cell = j
                                self.star[i][j].set_target_x(self.checking_cell)
                            elif (self.black_hole.appear
                                  and ((self.black_hole.type1 == 0 and i == self.black_hole.y1 and j >= self.black_hole.x1)
                                       or (self.black_hole.type2 == 0 and i == self.black_hole.y2 and j >= self.black_hole.x2))):
                                if i == self.black_hole.y1:
                                    if i == self.lock_y and self.star[i][self.lock_x] != 0 and self.star[i][self.lock_x].lock and self.lock_x >= self.black_hole.x1 and j > self.lock_x:
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
                                    else:
                                        self.star[i][j].target = self.black_hole.real_x1
                                        self.star[i][j].set_vx()
                                else:
                                    if i == self.lock_y and self.star[i][self.lock_x] != 0 and self.star[i][self.lock_x].lock and self.lock_x >= self.black_hole.x2 and j > self.lock_x:
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
                                    else:
                                        self.star[i][j].target = self.black_hole.real_x2
                                        self.star[i][j].set_vx()
                            else:
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
                for i in range(self.n):
                    self.checking_cell = self.n-1
                    self.checking_cell_value = 0
                    for j in range(self.n):
                        if self.star[i][self.n-1-j] != 0:
                            if self.star[i][self.n-1-j].lock:
                                self.checking_cell_value = self.star[i][self.n-1-j].value
                                self.checking_cell = self.n-1-j
                                self.star[i][self.n-1-j].set_target_x(self.checking_cell)
                            elif (self.black_hole.appear
                                  and ((self.black_hole.type1 == 0 and i == self.black_hole.y1 and self.n-1-j < self.black_hole.x1)
                                       or (self.black_hole.type2 == 0 and i == self.black_hole.y2 and self.n-1-j < self.black_hole.x2))):
                                if i == self.black_hole.y1:
                                    if i == self.lock_y and self.star[i][self.lock_x] != 0 and self.star[i][self.lock_x].lock and self.lock_x < self.black_hole.x2 and self.n-1-j < self.lock_x:
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
                                    else:
                                        self.star[i][self.n-1-j].target = self.black_hole.real_x1
                                        self.star[i][self.n-1-j].set_vx()
                                else:
                                    if i == self.lock_y and self.star[i][self.lock_x] != 0 and self.star[i][self.lock_x].lock and self.lock_x < self.black_hole.x2 and self.n-1-j < self.lock_x:
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
                                    else:
                                        self.star[i][self.n-1-j].target = self.black_hole.real_x2
                                        self.star[i][self.n-1-j].set_vx()
                            else:
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
            elif key == arcade.key.Z:
                if self.count - self.last_count0 >= 25:
                    self.last_count0 = self.count
                    self.sun = True
            elif key == arcade.key.X:
                if self.count - self.last_count1 >= 25:
                    self.last_count1 = self.count
                    for i in range(self.n):
                        for j in range(self.n):
                            if self.star[i][j] != 0 and self.star[i][j].value > 0:
                                self.star[i][j].charge = True
        elif self.state == 7:
            if key == arcade.key.SPACE:
                self.tutorial = False
                self.new_game()
                self.state = 1
            elif key == arcade.key.K:
                self.state = 2
            elif key == arcade.key.H:
                if self.tutorial:
                    self.tutorial = False
                else:
                    self.tutorial = True
        elif self.state == 8:
            if key == arcade.key.SPACE:
                self.tutorial = False
                self.new_game()
                self.state = 1
            elif key == arcade.key.H:
                if self.tutorial:
                    self.tutorial = False
                else:
                    self.tutorial = True
 
    def animate(self, delta):
        if self.state == 1: #gen star
            arcade.pause(0.1)
            if self.count % 6 == 0 and len(self.star_cell) > 0:
                self.random = randint(0,len(self.star_cell)-1)
                self.lock_x = self.star_cell[self.random]%self.n
                self.lock_y = math.floor(self.star_cell[self.random]/self.n)
                self.star[self.lock_y][self.lock_x].lock = True
            elif self.star[self.lock_y][self.lock_x] != 0:
                self.star[self.lock_y][self.lock_x].lock = False
            if self.count % 10 == 0 and self.count != 0:
                self.black_hole.appear = True
                self.black_hole.type1 = randint(0,1)
                self.black_hole.type2 = randint(0,1)
                if self.black_hole.type1 == 0:
                    self.black_hole.x1 = randint(0,4)
                    self.black_hole.y1 = randint(0,3)
                else:
                    self.black_hole.x1 = randint(0,3)
                    self.black_hole.y1 = randint(0,4)
                if self.black_hole.type2 == self.black_hole.type1:
                    self.black_hole_range1 = [0,1,2,3]
                    self.black_hole_range2 = [0,1,2,3,4]
                    if self.black_hole.type2 == 0:
                        self.black_hole_range1.remove(self.black_hole.y1)
                        self.black_hole_range2.remove(self.black_hole.x1)
                        self.black_hole.x2 = self.black_hole_range2[randint(0,3)]
                        self.black_hole.y2 = self.black_hole_range1[randint(0,2)]
                    else:
                        self.black_hole_range1.remove(self.black_hole.x1)
                        self.black_hole_range2.remove(self.black_hole.y1)
                        self.black_hole.x2 = self.black_hole_range1[randint(0,2)]
                        self.black_hole.y2 = self.black_hole_range2[randint(0,3)]
                else:
                    if self.black_hole.type2 == 0:
                        self.black_hole.x2 = randint(0,4)
                        self.black_hole.y2 = randint(0,3)
                    else:
                        self.black_hole.x2 = randint(0,3)
                        self.black_hole.y2 = randint(0,4)                    
                self.black_hole.set_position()
            else:
                self.black_hole.appear = False
            self.random = randint(0,len(self.blank_cell)-1)
            self.star[math.floor(self.blank_cell[self.random]/self.n)][self.blank_cell[self.random]%self.n] = Star(105+150*(self.blank_cell[self.random]%self.n), 555-150*math.floor(self.blank_cell[self.random]/self.n), self.sun)
            self.sun = False
            for i in range(self.n):
                for j in range(self.n):
                    if self.star[i][j] != 0 and self.star[i][j].value == -1:                        
                        arcade.pause(0.5)
                        self.for_del = self.star[i][j]
                        self.star[i][j] = 0
                        del self.for_del
                        for k in range(self.n):
                            if self.star[i][k] != 0 and self.star[i][k].value > 0:
                                if self.star[i][k].value < 131072:
                                    self.star[i][k].value *= 2
                                self.score += (int)(math.log2(self.max)*self.star[i][k].value/4)
                            if self.star[k][j] != 0 and self.star[k][j].value > 0:
                                if self.star[k][j].value < 131072:
                                    self.star[k][j].value *= 2
                                self.score += (int)(math.log2(self.max)*self.star[k][j].value/4)
            self.check_max()
            self.check_blank_cell()
            if self.is_end():
                self.state = 0
            elif (not self.is_finish) and self.max == 2048:
                self.is_finish = True
                self.state = 7
            elif self.score > 100000:
                self.state = 8
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
        self.star_cell.clear()
        self.blank_cell.clear()
        for i in range(self.n):
            for j in range(self.n):
                if self.star[i][j] == 0:
                    self.blank_cell.append(self.n*i+j)
                else:
                    self.star_cell.append(self.n*i+j)

    def check_max(self):
        self.max = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.star[i][j] != 0 and self.star[i][j].value > self.max:
                    self.max = self.star[i][j].value

    def can_move_up(self):
        if self.black_hole.appear and self.black_hole.type1 == 1 and self.black_hole.y1 != 4:
            for i in range(self.n-self.black_hole.y1):
                if self.star[self.n-1-i][self.black_hole.x1] != 0:
                    return True
        if self.black_hole.appear and self.black_hole.type2 == 1 and self.black_hole.y2 != 4:
            for i in range(self.n-self.black_hole.y2):
                if self.star[self.n-1-i][self.black_hole.x2] != 0:
                    return True
        for i in range(self.n-1):
            for j in range(self.n):
                if self.star[self.n-1-i-1][j] == 0 and self.star[self.n-1-i][j] != 0 and (not self.star[self.n-1-i][j].lock):
                    return True
                if self.star[self.n-1-i][j] != 0 and self.star[self.n-1-i-1][j] != 0 and self.star[self.n-1-i][j].value == self.star[self.n-1-i-1][j].value and (not self.star[self.n-1-i][j].lock):
                    return True
        return False

    def can_move_down(self):
        if self.black_hole.appear and self.black_hole.type1 == 1 and self.black_hole.y1 != 0:
            for i in range(self.black_hole.y1):
                if self.star[i][self.black_hole.x1] != 0:
                    return True
        if self.black_hole.appear and self.black_hole.type2 == 1 and self.black_hole.y2 != 0:
            for i in range(self.black_hole.y2):
                if self.star[i][self.black_hole.x2] != 0:
                    return True
        for i in range(self.n-1):
            for j in range(self.n):
                if self.star[i+1][j] == 0 and self.star[i][j] != 0 and (not self.star[i][j].lock):
                    return True
                if self.star[i][j] != 0 and self.star[i+1][j] != 0 and self.star[i][j].value == self.star[i+1][j].value and (not self.star[i][j].lock):
                    return True
        return False

    def can_move_left(self):
        if self.black_hole.appear and self.black_hole.type1 == 0 and self.black_hole.x1 != 4:
            for i in range(self.black_hole.x1):
                if self.star[self.black_hole.y1][i] != 0:
                    return True
        if self.black_hole.appear and self.black_hole.type2 == 0 and self.black_hole.x2 != 4:
            for i in range(self.black_hole.x2):
                if self.star[self.black_hole.y2][i] != 0:
                    return True
        for i in range(self.n-1):
            for j in range(self.n):
                if self.star[j][i] == 0 and self.star[j][i+1] != 0 and (not self.star[j][i+1].lock):
                    return True
                if self.star[j][i] != 0 and self.star[j][i+1] != 0 and self.star[j][i].value == self.star[j][i+1].value and (not self.star[j][i+1].lock):
                    return True
        return False

    def can_move_right(self):
        if self.black_hole.appear and self.black_hole.type1 == 0 and self.black_hole.x1 != 0:
            for i in range(self.n-self.black_hole.x1):
                if self.star[self.black_hole.y1][self.n-1-i] != 0:
                    return True
        if self.black_hole.appear and self.black_hole.type2 == 0 and self.black_hole.x2 != 0:
            for i in range(self.n-self.black_hole.x2):
                if self.star[self.black_hole.y2][self.n-1-i] != 0:
                    return True
        for i in range(self.n-1):
            for j in range(self.n):
                if self.star[j][self.n-1-i] == 0 and self.star[j][self.n-1-i-1] != 0 and (not self.star[j][self.n-1-i-1].lock):
                    return True
                if self.star[j][self.n-1-i] != 0 and self.star[j][self.n-1-i-1] != 0 and self.star[j][self.n-1-i].value == self.star[j][self.n-1-i-1].value and (not self.star[j][self.n-1-i-1].lock):
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
                if self.star[i][j] != 0 and ((self.star[i][j].x == self.black_hole.real_x1 and self.star[i][j].y == self.black_hole.real_y1) or (self.star[i][j].x == self.black_hole.real_x2 and self.star[i][j].y == self.black_hole.real_y2)):
                    self.for_del = self.star[i][j]
                    self.star[i][j] = 0
                    del self.for_del
        for i in range(self.n):
            for j in range(self.n):
                if self.star[i][j] != 0:
                    if self.star[i][j].value < 0:
                        self.star[i][j].value += 1 
                    else:
                        self.merge_cell(i, j)
        self.all_star.clear()
        for i in range(self.n):
            for j in range(self.n):
                if self.star[i][j] != 0:
                    self.star[i][j].charge = False
                    self.all_star.append(self.star[i][j])
                    self.for_del = self.star[i][j]
                    self.star[i][j] = 0
                    del self.for_del
        for i in range(len(self.all_star)):
            self.star[(int)((555 - self.all_star[i].y)/150)][(int)((self.all_star[i].x - 105)/150)] = self.all_star[i]
        for i in range(self.n):
            for j in range(self.n):
                if self.star[i][j] != 0 and self.star[i][j].value == -1:                        
                    for k in range(self.n):
                        if self.star[i][k] != 0 and self.star[i][k].value > 0:
                            self.star[i][k].charge = True
                        if self.star[k][j] != 0 and self.star[k][j].value > 0:
                            self.star[k][j].charge = True
        self.check_max()
        self.check_blank_cell()
        self.count += 1
        self.state = 1

    def merge_cell(self, i, j):
        for k in range(self.n):
            for l in range(self.n):
                if self.star[k][l] != 0 and (k != i or l != j) and self.star[k][l].x == self.star[i][j].x and self.star[k][l].y == self.star[i][j].y:
                    if self.star[i][j].charge:
                        if self.star[i][j].value <= 32:
                            self.star[i][j].value **= 2
                            self.score += (int)(math.log2(self.max)*self.star[i][j].value/4)
                        else:
                            self.star[i][j].value *= 2
                            self.score += (int)(2*math.log2(self.max)*self.star[i][j].value/4)
                    else:
                        if self.star[i][j].value < 131072:
                            self.star[i][j].value *= 2
                        self.score += (int)(math.log2(self.max)*self.star[i][j].value/4)
                    self.for_del = self.star[k][l]
                    self.star[k][l] = 0
                    del self.for_del
                    return
                    
    def is_end(self):
        return ((len(self.blank_cell) == 0) and (not self.can_move()))

class Star:
    def __init__(self, x, y, sun):
        self.x = x
        self.y = y
        self.target = -1
        self.v = 0
        self.lock = False
        self.charge = False
        if sun:
            self.value = -3
        else:
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
        self.type1 = 0
        self.type2 = 0
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
        self.real_x1 = 0
        self.real_x2 = 0
        self.real_y1 = 0
        self.real_y2 = 0

    def set_position(self):
        if self.type1 == 0:
            self.real_x1 = 30+150*self.x1
            self.real_y1 = 555-150*self.y1
        else:
            self.real_x1 = 105+150*self.x1
            self.real_y1 = 630-150*self.y1
        if self.type2 == 0:
            self.real_x2 = 30+150*self.x2
            self.real_y2 = 555-150*self.y2
        else:
            self.real_x2 = 105+150*self.x2
            self.real_y2 = 630-150*self.y2
