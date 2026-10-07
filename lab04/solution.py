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

def ranking(name,scor):
    new_names = list(range(len(name)))
    new_names.sort(key=lambda i: scor[i], reverse=True)

    return [name[i] for i in new_names]

def above_average(name,scor):
    above = []
    aver = average(scor)
    for i in range(len(scor)):
        if scor[i] > aver:
            above.append(name[i])

    return above