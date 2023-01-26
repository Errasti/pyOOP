import erase_matrix
import init_wave
import create_way
import point
import matrix
import print_matrix

lab = []
flag = True
start = point.Point(0, 1, 1)
finish = point.Point(4, 10, 80)


def menu():
    global lab
    global flag
    print("1.Создать лабиринт\n"
          "2.Вывести лабиринт\n"
          "3.Создать волну\n"
          "4.Создать путь\n"
          "5.Выход")
    number = input("Введите пункт меню: ")
    print("/////////////////////////")

    while flag:
        if number == "1":
            temp = matrix.Matrix(10, 20)
            lab = temp.fill_matrix()
            lab[start.get_row()][start.get_col()] = start.get_index()
            lab[finish.get_row()][finish.get_col()] = finish.get_index()
            menu()
        elif number == "2":
            print_matrix.print_matrix(lab)
            menu()
        elif number == "3":
            cr = init_wave.CreateWave(lab, start)
            cr.create_wave()
            print_matrix.print_matrix(cr.get_maze())
            menu()
        elif number == "4":
            cw = create_way.CreateWay(lab, finish)
            cw.way()
            clean_matrix = erase_matrix.clear(cw.get_maze())
            print_matrix.print_matrix(clean_matrix)
            menu()
        elif number == "5":
            flag = False
        else:
            menu()


menu()
