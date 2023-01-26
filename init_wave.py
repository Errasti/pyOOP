import sides
import point
from collections import deque


class CreateWave:
    maze = []
    start = point.Point
    my_deque = deque()

    def __init__(self, lab, start: point.Point):
        self.maze = lab
        self.start = start

    def create_wave(self):
        self.my_deque.append(self.start)

        while self.my_deque:
            temp_dot: point.Point = self.my_deque.popleft()
            self.maze[temp_dot.get_row()][temp_dot.get_col()] = temp_dot.get_index()
            temp_deque = sides.checker(temp_dot)
            while temp_deque:
                dot: point.Point = temp_deque.popleft()
                if self.maze[dot.get_row()][dot.get_col()] == " ":
                    self.maze[dot.get_row()][dot.get_col()] = dot.get_index()
                    self.my_deque.append(dot)

    def get_maze(self):
        return self.maze
