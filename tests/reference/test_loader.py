from pathlib import Path

import pytest

from src.reference.loader import (
    ReferenceDatabaseLoadError,
    load_reference_csv,
)


def test_load_reference_csv_reads_all_values_as_text(
    tmp_path: Path,
) -> None:
    path = tmp_path / "reference.csv"

    path.write_text(
        "species,id,sequence\n"
        "Danio rerio,001,ATCG\n",
        encoding="utf-8",
    )

    database = load_reference_csv(path)

    assert database.loc[0, "id"] == "001"
    assert database.loc[0, "species"] == "Danio rerio"


def test_load_reference_csv_rejects_missing_file(
    tmp_path: Path,
) -> None:
    with pytest.raises(
        ReferenceDatabaseLoadError,
        match="não encontrado",
    ):
        load_reference_csv(
            tmp_path / "missing.csv"
        )