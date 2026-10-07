def winner(name,scor):
    win = -1
    maximum = -1
    for i in range(len(scor)):
        if scor[i] > maximum:
            maximum = scor[i]
            win = name[i]

    return win

