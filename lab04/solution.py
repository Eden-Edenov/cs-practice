def winner(names: list[str], scores: list[float]) -> str:
    if not scores or not names:
        return ""
    best_index = max(range(len(scores)), key=lambda i: scores[i])
    return names[best_index]


def average(scores: list[float]) -> float:
    if not scores:
        return 0.0

    return round(sum(scores) / len(scores), 2)


def ranking(names: list[str], scores: list[float]) -> list[str]:
    indices = list(range(len(names)))
    indices.sort(key=lambda i: scores[i], reverse=True)

    return [names[i] for i in indices]


def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg_score = average(scores)
    return [names[i] for i in range(len(scores)) if scores[i] > avg_score]