from collections import deque

import sides
import point


class CreateWay:
    maze = []
    finish = point.Point
    my_deque = deque()
    start = point.Point
    flag = True
    index = 1000

    def __init__(self, lab, finish: point.Point):
        self.maze = lab
        self.finish = finish

    def way(self):
        temp_deque = sides.checker(self.finish)
        min_index = 1000
        while temp_deque:
            dot: point.Point = temp_deque.popleft()
            if len(self.maze) > dot.get_row() >= 0 and len(self.maze[0]) > dot.get_col() >= 0:
                temp = self.maze[dot.get_row()][dot.get_col()]
                if type(temp) == int and temp < min_index:
                    min_index = self.maze[dot.get_row()][dot.get_col()]
                    self.index = min_index
                    self.start = dot

        while self.index > 1:
            self.maze[self.start.get_row()][self.start.get_col()] = "$"
            new_deque = sides.checker(self.start)
            while new_deque:
                temp_dot: point.Point = new_deque.popleft()
                if len(self.maze) > temp_dot.get_row() >= 0 and len(self.maze[0]) > temp_dot.get_col() >= 0:
                    if self.maze[temp_dot.get_row()][temp_dot.get_col()] == self.index - 1:
                        self.index = self.maze[temp_dot.get_row()][temp_dot.get_col()]
                        self.start = temp_dot
                        break

    def get_maze(self):
        return self.maze