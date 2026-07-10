import pandas as pd

from src.reference.database import ReferenceDatabase
from src.taxonomy import (
    UNKNOWN_SPECIES_LABEL,
    classify_sequence,
)


def make_database() -> ReferenceDatabase:
    dataframe = pd.DataFrame(
        [
            {
                "species": "Danio rerio",
                "id": "DRE001",
                "sequence": "ATCG",
            },
            {
                "species": "Danio rerio",
                "id": "DRE002",
                "sequence": "ATCC",
            },
            {
                "species": "Salmo salar",
                "id": "SSA001",
                "sequence": "GGGG",
            },
        ]
    )

    return ReferenceDatabase(dataframe)


def test_classify_sequence_uses_best_reference_per_species() -> None:
    result = classify_sequence(
        "ATCC",
        make_database(),
        min_similarity=95.0,
    )

    assert result["species"] == "Danio rerio"
    assert result["reference_id"] == "DRE002"
    assert result["identified"] is True


def test_classify_sequence_respects_minimum_similarity() -> None:
    result = classify_sequence(
        "AAAA",
        make_database(),
        min_similarity=90.0,
    )

    assert result["species"] == UNKNOWN_SPECIES_LABEL
    assert result["reference_id"] is None
    assert result["identified"] is False