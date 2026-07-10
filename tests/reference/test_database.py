from pathlib import Path

from src.reference.database import ReferenceDatabase


def test_reference_database_exposes_queries_and_statistics(
    tmp_path: Path,
) -> None:
    path = tmp_path / "reference.csv"

    path.write_text(
        "species,id,sequence\n"
        "Danio rerio,DRE001,ATCG\n"
        "Danio rerio,DRE002,ATCC\n"
        "Salmo salar,SSA001,GGGG\n",
        encoding="utf-8",
    )

    database = ReferenceDatabase.from_csv(path)

    assert database.list_species() == [
        "Danio rerio",
        "Salmo salar",
    ]

    assert database.list_ids() == [
        "DRE001",
        "DRE002",
        "SSA001",
    ]

    assert len(
        database.find_by_species("Danio rerio")
    ) == 2

    assert database.statistics() == {
        "reference_count": 3,
        "species_count": 2,
        "id_count": 3,
    }