def winner(name,scor):
    win = -1
    maximum = -1
    for i in range(len(scor)):
        if scor[i] > maximum:
            maximum = scor[i]
            win = name[i]

    return win

def average(scor):
    if scor == []:
        return 0.0
    cnt = 0
    summa = 0
    for i in scor:
        cnt += 1
        summa += i

    return f'{summa/cnt:.2f}'
