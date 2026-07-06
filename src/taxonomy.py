import pandas as pd

from src.similarity import calculate_similarity


UNKNOWN_SPECIES_LABEL = "Espécie não identificada"
REQUIRED_REFERENCE_COLUMNS = {"species", "id", "sequence"}


def load_reference_database(file_path: str) -> pd.DataFrame:
    """Load and validate the local reference database."""
    database = pd.read_csv(file_path)
    missing_columns = REQUIRED_REFERENCE_COLUMNS.difference(database.columns)

    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(
            "Banco de referência inválido. "
            f"Colunas obrigatórias ausentes: {missing}."
        )

    database = database.dropna(subset=["species", "id", "sequence"]).copy()

    if database.empty:
        raise ValueError("Banco de referência vazio ou sem sequências válidas.")

    database["species"] = database["species"].astype(str).str.strip()
    database["id"] = database["id"].astype(str).str.strip()
    database["sequence"] = database["sequence"].astype(str).str.upper().str.strip()

    return database


def exact_match(sequence: str, database: pd.DataFrame) -> str:
    """Return the species for an exact sequence match, when available."""
    sequence = sequence.upper()

    for _, row in database.iterrows():
        if sequence == row["sequence"].upper():
            return str(row["species"])

    return "Não identificado"


def rank_similarity_matches(
    sequence: str,
    database: pd.DataFrame,
    top_n: int = 5,
) -> list[dict[str, object]]:
    """Return the best species-level similarity matches for a sequence."""
    best_by_species: dict[str, dict[str, object]] = {}

    for _, row in database.iterrows():
        species = str(row["species"])
        reference_id = str(row["id"])
        score = calculate_similarity(sequence, str(row["sequence"]))

        current_best = best_by_species.get(species)
        if current_best is None or score > float(current_best["similarity"]):
            best_by_species[species] = {
                "species": species,
                "reference_id": reference_id,
                "similarity": score,
            }

    ranked_matches = sorted(
        best_by_species.values(),
        key=lambda item: float(item["similarity"]),
        reverse=True,
    )

    return ranked_matches[:top_n]


def classify_sequence(
    sequence: str,
    database: pd.DataFrame,
    min_similarity: float = 95.0,
    top_n: int = 5,
) -> dict[str, object]:
    """Classify a sequence using a local database and a similarity threshold."""
    ranking = rank_similarity_matches(sequence, database, top_n=top_n)

    if not ranking:
        return {
            "species": UNKNOWN_SPECIES_LABEL,
            "similarity": 0.0,
            "reference_id": None,
            "identified": False,
            "ranking": [],
        }

    best_match = ranking[0]
    best_similarity = float(best_match["similarity"])
    identified = best_similarity >= min_similarity

    return {
        "species": best_match["species"] if identified else UNKNOWN_SPECIES_LABEL,
        "similarity": best_similarity,
        "reference_id": best_match["reference_id"] if identified else None,
        "identified": identified,
        "ranking": ranking,
    }


def best_similarity_match(sequence: str, database: pd.DataFrame) -> dict[str, object]:
    """Keep the original MVP API returning the single best match."""
    classification = classify_sequence(sequence, database, min_similarity=0.0, top_n=1)
    return {
        "species": classification["species"],
        "similarity": classification["similarity"],
    }