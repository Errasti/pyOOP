class Point:

    def __init__(self, row, col, index):
        self.x = row
        self.y = col
        self.index = index

    def get_col(self):
        return self.y

    def get_row(self):
        return self.x

    def get_index(self):
        return self.index

    def check(self, row, col):
        return self.x == row & self.y == col

