limit = float(input())
recorded = int(input())

cnt_errors = 0
above_limit = 0
maximum = -1000000000
average = 0.0

not_errors = 0
current_temp = 0.0
summ_tepm = 0.0

for i in range(recorded):
    one_record = input()

    if one_record == 'error':
        cnt_errors += 1
    else:
        current_temp = float(one_record)
        summ_tepm += current_temp
        not_errors += 1

        if current_temp > limit:
            above_limit += 1

        maximum = max(maximum,current_temp)

average = summ_tepm/not_errors

