from collections import deque

import point


def checker(dot: point.Point):
    array = deque()
    p1 = point.Point(dot.get_row() + 1, dot.get_col() + 1, dot.get_index() + 1)
    array.append(p1)
    p2 = point.Point(dot.get_row() + 1, dot.get_col(), dot.get_index() + 1)
    array.append(p2)
    p3 = point.Point(dot.get_row() + 1, dot.get_col() - 1, dot.get_index() + 1)
    array.append(p3)
    p4 = point.Point(dot.get_row(), dot.get_col() - 1, dot.get_index() + 1)
    array.append(p4)
    p5 = point.Point(dot.get_row() - 1, dot.get_col() - 1, dot.get_index() + 1)
    array.append(p5)
    p6 = point.Point(dot.get_row() - 1, dot.get_col(), dot.get_index() + 1)
    array.append(p6)
    p7 = point.Point(dot.get_row() - 1, dot.get_col() + 1, dot.get_index() + 1)
    array.append(p7)
    p8 = point.Point(dot.get_row(), dot.get_col() + 1, dot.get_index() + 1)
    array.append(p8)

    return array
