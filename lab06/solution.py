def count_items(list):
    counts = {}
    for elem in list:
        counts[elem] = counts.get(elem, 0) + 1
    return counts

def unique_sorted(spisok):
    return sorted(list(set(spisok)))

def common(list_first, list_second):
    return sorted(list(set(list_first) & set(list_second)))