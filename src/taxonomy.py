from src.reference.database import ReferenceDatabase
from src.similarity import calculate_similarity


UNKNOWN_SPECIES_LABEL = "Espécie não identificada"


def exact_match(
    sequence: str,
    database: ReferenceDatabase,
) -> str:
    """Return the species for an exact match."""
    normalized_sequence = sequence.upper()

    for record in database.iter_records():
        if normalized_sequence == record["sequence"]:
            return record["species"]

    return "Não identificado"


def rank_similarity_matches(
    sequence: str,
    database: ReferenceDatabase,
    top_n: int = 5,
) -> list[dict[str, object]]:
    """Return the best match for each species."""
    best_by_species: dict[
        str,
        dict[str, object],
    ] = {}

    for record in database.iter_records():
        species = record["species"]

        score = calculate_similarity(
            sequence,
            record["sequence"],
        )

        current_best = best_by_species.get(species)

        if (
            current_best is None
            or score > float(
                current_best["similarity"]
            )
        ):
            best_by_species[species] = {
                "species": species,
                "reference_id": record["id"],
                "similarity": score,
                "gene": record.get("gene", ""),
                "accession": record.get(
                    "accession",
                    "",
                ),
                "source": record.get("source", ""),
            }

    ranked_matches = sorted(
        best_by_species.values(),
        key=lambda item: float(
            item["similarity"]
        ),
        reverse=True,
    )

    return ranked_matches[:top_n]


def classify_sequence(
    sequence: str,
    database: ReferenceDatabase,
    min_similarity: float = 95.0,
    top_n: int = 5,
) -> dict[str, object]:
    """Classify using a validated reference database."""
    ranking = rank_similarity_matches(
        sequence,
        database,
        top_n=top_n,
    )

    if not ranking:
        return {
            "species": UNKNOWN_SPECIES_LABEL,
            "similarity": 0.0,
            "reference_id": None,
            "gene": None,
            "accession": None,
            "source": None,
            "identified": False,
            "ranking": [],
        }

    best_match = ranking[0]
    best_similarity = float(
        best_match["similarity"]
    )

    identified = (
        best_similarity >= min_similarity
    )

    return {
        "species": (
            best_match["species"]
            if identified
            else UNKNOWN_SPECIES_LABEL
        ),
        "similarity": best_similarity,
        "reference_id": (
            best_match["reference_id"]
            if identified
            else None
        ),
        "gene": (
            best_match["gene"]
            if identified
            else None
        ),
        "accession": (
            best_match["accession"]
            if identified
            else None
        ),
        "source": (
            best_match["source"]
            if identified
            else None
        ),
        "identified": identified,
        "ranking": ranking,
    }


def best_similarity_match(
    sequence: str,
    database: ReferenceDatabase,
) -> dict[str, object]:
    """Keep the original API for the best match."""
    classification = classify_sequence(
        sequence,
        database,
        min_similarity=0.0,
        top_n=1,
    )

    return {
        "species": classification["species"],
        "similarity": classification["similarity"],
    }