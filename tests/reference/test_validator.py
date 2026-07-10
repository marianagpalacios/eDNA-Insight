import pandas as pd
import pytest

from src.reference.validator import (
    ReferenceDatabaseValidationError,
    validate_reference_dataframe,
)


def test_validator_normalizes_whitespace_and_lowercase() -> None:
    database = pd.DataFrame(
        [
            {
                "species": " Danio rerio ",
                "id": " DRE001 ",
                "sequence": " at cg ",
            }
        ]
    )

    result = validate_reference_dataframe(database)

    assert result.dataframe.loc[0, "species"] == "Danio rerio"
    assert result.dataframe.loc[0, "id"] == "DRE001"
    assert result.dataframe.loc[0, "sequence"] == "ATCG"
    assert result.warnings


def test_validator_rejects_missing_required_columns() -> None:
    database = pd.DataFrame(
        [{"species": "Danio rerio"}]
    )

    with pytest.raises(
        ReferenceDatabaseValidationError,
        match="Colunas obrigatórias ausentes",
    ):
        validate_reference_dataframe(database)


def test_validator_rejects_duplicate_ids() -> None:
    database = pd.DataFrame(
        [
            {
                "species": "Danio rerio",
                "id": "DRE001",
                "sequence": "ATCG",
            },
            {
                "species": "Danio rerio",
                "id": "DRE001",
                "sequence": "ATCC",
            },
        ]
    )

    with pytest.raises(
        ReferenceDatabaseValidationError,
        match="IDs duplicados",
    ):
        validate_reference_dataframe(database)


def test_validator_rejects_invalid_sequence_characters() -> None:
    database = pd.DataFrame(
        [
            {
                "species": "Danio rerio",
                "id": "DRE001",
                "sequence": "ATXG",
            }
        ]
    )

    with pytest.raises(
        ReferenceDatabaseValidationError,
        match="Caracteres inválidos",
    ):
        validate_reference_dataframe(database)