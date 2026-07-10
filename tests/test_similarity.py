import pytest

from src.similarity import (
    calculate_similarity,
    edit_distance,
)


def test_identical_sequences_have_full_similarity() -> None:
    assert edit_distance("ATCG", "ATCG") == 0
    assert calculate_similarity(
        "ATCG",
        "ATCG",
    ) == 100.0


def test_similarity_handles_one_substitution() -> None:
    assert edit_distance("ATCG", "ATCC") == 1
    assert calculate_similarity(
        "ATCG",
        "ATCC",
    ) == 75.0


def test_similarity_handles_one_insertion() -> None:
    assert edit_distance("ATCG", "ATTCG") == 1
    assert calculate_similarity(
        "ATCG",
        "ATTCG",
    ) == 80.0


def test_similarity_handles_one_deletion() -> None:
    assert edit_distance("ATTCG", "ATCG") == 1
    assert calculate_similarity(
        "ATTCG",
        "ATCG",
    ) == 80.0


def test_similarity_handles_different_lengths() -> None:
    assert calculate_similarity(
        "ATCG",
        "AT",
    ) == 50.0


@pytest.mark.parametrize(
    ("seq1", "seq2"),
    [
        ("", ""),
        ("ATCG", ""),
        ("", "ATCG"),
    ],
)
def test_similarity_with_empty_sequence_is_zero(
    seq1: str,
    seq2: str,
) -> None:
    assert calculate_similarity(
        seq1,
        seq2,
    ) == 0.0


def test_similarity_is_case_insensitive() -> None:
    assert calculate_similarity(
        "atcg",
        "ATCG",
    ) == 100.0