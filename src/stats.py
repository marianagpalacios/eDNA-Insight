def sequence_length(sequence):
    return len(sequence)

def gc_content(sequence):
    sequence = sequence.upper()
    gc = sequence.count("G") + sequence.count("C")
    return round((gc / len(sequence)) * 100, 2) if sequence else 0

def summarize_sequences(sequences):
    lengths = [len(item["sequence"]) for item in sequences]

    return {
        "total_sequences": len(sequences),
        "min_length": min(lengths),
        "max_length": max(lengths),
        "average_length": round(sum(lengths) / len(lengths), 2),
        "gc_by_sequence": [
            {
                "id": item["id"],
                "gc_content": gc_content(item["sequence"])
            }
            for item in sequences
        ]
    }