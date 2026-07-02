def calculate_similarity(seq1, seq2):
    seq1 = seq1.upper()
    seq2 = seq2.upper()

    min_length = min(len(seq1), len(seq2))
    max_length = max(len(seq1), len(seq2))

    matches = 0

    for i in range(min_length):
        if seq1[i] == seq2[i]:
            matches += 1

    return round((matches / max_length) * 100, 2)