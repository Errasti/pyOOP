def print_matrix(lab):
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            print('%2s' % lab[i][j], end=" ")
        print()
