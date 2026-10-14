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


def total_minutes(rows, kind):
    total = 0.0
    has_kind = False

    for row in rows:
        if row.get("тип") == kind:
            has_kind = True
            minutes_str = row.get("минуты", "0")
            minutes_str = minutes_str.replace(',', '.')
            try:
                total += float(minutes_str)
            except ValueError:
                continue

    if not has_kind:
        return 0.0

    return round(total, 1)

def to_csv(counts):
    result = ["тип,количество"]

    for kind in sorted(counts.keys()):
        result.append(f"{kind},{counts[kind]}")

    return "\n".join(result) + "\n"

with open('events.csv', encoding="utf-8") as table:
    ans_rows = read_rows(table)
    print(ans_rows)

    ans_count = count_types(ans_rows)
    print(ans_count)

    ans_minutes = total_minutes(ans_rows,'ошибка')
    print(ans_minutes)
    ans_minutes = total_minutes(ans_rows, 'запуск')
    print(ans_minutes)

    ans_csv = to_csv(ans_count)
    print(ans_csv)