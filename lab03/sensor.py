limit = int(input())
recorded = int(input())

cnt_errors = 0
above_limit = 0
maximum = -1000000000
average = 0.0

current_temp = 0.0
summ_tepm = 0.0

for i in range(recorded):
    one_record = input()
    