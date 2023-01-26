import random


class Matrix:
    columns = 20
    rows = 10

    def __init__(self, row, col):
        self.rows = row
        self.columns = col

    def fill_matrix(self):
        maze = [["##"] * self.columns for i in range(self.rows)]
        sequence = [" ", " ", " ", "##"]

        for i in range(1, self.rows - 1):
            for j in range(1, self.columns - 1):
                rand = random.choice(sequence)
                maze[i][j] = rand

        return maze
