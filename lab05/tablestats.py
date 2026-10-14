def read_rows(lines):
    rows = []
    zagolovok = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        fields = [field.strip() for field in line.split(',')]

        if zagolovok is None:
            zagolovok = fields
            continue

        if len(fields) != len(zagolovok):
            continue

        row_dict = {zagolovok[i]: fields[i] for i in range(len(zagolovok))}
        rows.append(row_dict)

    return rows

def count_types(ryad):
    counts = {}
    for row in ryad:
        kind = row.get("тип")
        if kind:
            counts[kind] = counts.get(kind, 0) + 1
    return counts



with open('events.csv', encoding="utf-8") as table:
    ans_rows = read_rows(table)
    print(ans_rows)
    ans_count = count_types(ans_rows)
    print(ans_count)