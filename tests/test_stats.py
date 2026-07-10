from src.stats import (
    sequence_composition,
    summarize_sequences,
)


def test_sequence_composition_calculates_percentages() -> None:
    metrics = sequence_composition("AATCGN")

    assert metrics == {
        "length": 6,
        "a_frequency": 33.33,
        "t_frequency": 16.67,
        "c_frequency": 16.67,
        "g_frequency": 16.67,
        "at_content": 50.0,
        "gc_content": 33.33,
        "n_count": 1,
    }


def test_summarize_adds_median_and_std_dev() -> None:
    summary = summarize_sequences(
        [
            {
                "id": "seq_1",
                "sequence": "ATCG",
            },
            {
                "id": "seq_2",
                "sequence": "ATCGAT",
            },
            {
                "id": "seq_3",
                "sequence": "ATCGATCG",
            },
        ]
    )

    assert summary["average_length"] == 6.0
    assert summary["median_length"] == 6.0
    assert summary["length_std_dev"] == 1.63
    assert len(summary["sequence_metrics"]) == 3


def test_summarize_handles_empty_collection() -> None:
    summary = summarize_sequences([])

    assert summary["total_sequences"] == 0
    assert summary["median_length"] == 0.0
    assert summary["length_std_dev"] == 0.0
    assert summary["sequence_metrics"] == []