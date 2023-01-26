def clear(lab):
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if type(lab[i][j]) == int and lab[i][j] != 1 and lab[i][j] != 99:
                lab[i][j] = " "
    return lab