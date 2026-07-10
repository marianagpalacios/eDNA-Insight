def edit_distance(seq1: str, seq2: str) -> int:
    """Return the Levenshtein distance."""
    first = seq1.upper()
    second = seq2.upper()

    if first == second:
        return 0

    if len(first) < len(second):
        first, second = second, first

    previous_row = list(
        range(len(second) + 1)
    )

    for row_index, first_base in enumerate(
        first,
        start=1,
    ):
        current_row = [row_index]

        for column_index, second_base in enumerate(
            second,
            start=1,
        ):
            insertion = (
                current_row[column_index - 1] + 1
            )

            deletion = (
                previous_row[column_index] + 1
            )

            substitution = (
                previous_row[column_index - 1]
                + (first_base != second_base)
            )

            current_row.append(
                min(
                    insertion,
                    deletion,
                    substitution,
                )
            )

        previous_row = current_row

    return previous_row[-1]


def calculate_similarity(
    seq1: str,
    seq2: str,
) -> float:
    """Return normalized edit similarity."""
    max_length = max(
        len(seq1),
        len(seq2),
    )

    if max_length == 0:
        return 0.0

    distance = edit_distance(seq1, seq2)

    similarity = (
        1 - distance / max_length
    ) * 100

    return round(
        max(similarity, 0.0),
        2,
    )