from src.validation import find_invalid_bases, validate_sequences


def test_find_invalid_bases_returns_unique_sorted_bases() -> None:
    assert find_invalid_bases("ATXCGZ") == ["X", "Z"]


def test_validate_sequences_normalizes_valid_sequence_to_uppercase() -> None:
    valid, invalid = validate_sequences(
        [{"id": "seq_1", "sequence": "atcgn"}],
        allow_n=True,
    )

    assert valid == [{"id": "seq_1", "sequence": "ATCGN"}]
    assert invalid == []


def test_validate_sequences_rejects_n_in_strict_mode() -> None:
    valid, invalid = validate_sequences(
        [{"id": "seq_1", "sequence": "ATCGN"}],
        allow_n=False,
    )

    assert valid == []
    assert invalid[0]["invalid_bases"] == ["N"]


def test_validate_sequences_rejects_empty_sequence() -> None:
    valid, invalid = validate_sequences(
        [{"id": "seq_1", "sequence": "   "}],
    )

    assert valid == []
    assert invalid == [
        {
            "id": "seq_1",
            "invalid_bases": [],
            "reason": "Sequência vazia.",
        }
    ]