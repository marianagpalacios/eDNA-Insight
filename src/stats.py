from src.fasta import SequenceRecord


def sequence_length(sequence: str) -> int:
    return len(sequence)


def gc_content(sequence: str) -> float:
    sequence = sequence.upper()
    gc = sequence.count("G") + sequence.count("C")
    return round((gc / len(sequence)) * 100, 2) if sequence else 0.0


def summarize_sequences(sequences: list[SequenceRecord]) -> dict[str, object]:
    lengths = [len(item["sequence"]) for item in sequences]

    if not lengths:
        return {
            "total_sequences": 0,
            "min_length": 0,
            "max_length": 0,
            "average_length": 0.0,
            "gc_by_sequence": [],
        }

    return {
        "total_sequences": len(sequences),
        "min_length": min(lengths),
        "max_length": max(lengths),
        "average_length": round(sum(lengths) / len(lengths), 2),
        "gc_by_sequence": [
            {
                "id": item["id"],
                "gc_content": gc_content(item["sequence"]),
            }
            for item in sequences
        ],
    }