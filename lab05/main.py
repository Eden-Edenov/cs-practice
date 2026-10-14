import os
from tablestats import read_rows, count_types, total_minutes, to_csv


def main():
    filename = input().strip()

    with open(filename, "r", encoding="utf-8") as table:
        rows = read_rows(table)

    counts = count_types(rows)
    total_error_minutes = total_minutes(rows, "ошибка")

    print(len(rows))
    print(len(counts))
    print(total_error_minutes)

    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(to_csv(counts))

main()