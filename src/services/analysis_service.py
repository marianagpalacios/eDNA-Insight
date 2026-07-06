from collections.abc import Callable
from typing import Any

from src.fasta import read_fasta
from src.stats import summarize_sequences
from src.taxonomy import classify_sequence, load_reference_database
from src.validation import validate_sequences


ProgressCallback = Callable[[float, str], None]


class AnalysisError(Exception):
    """Raised when the analysis workflow cannot continue safely."""


def _notify(
    progress_callback: ProgressCallback | None,
    value: float,
    message: str,
) -> None:
    if progress_callback:
        progress_callback(value, message)


def analyze_fasta_file(
    file_path: str,
    reference_database_path: str,
    min_similarity: float = 95.0,
    allow_n: bool = True,
    top_n: int = 5,
    progress_callback: ProgressCallback | None = None,
) -> dict[str, Any]:
    """Run the complete MVP analysis pipeline for a FASTA file."""
    _notify(progress_callback, 0.1, "Lendo arquivo FASTA...")
    sequences = read_fasta(file_path)

    if not sequences:
        raise AnalysisError("Nenhuma sequência foi encontrada no arquivo FASTA.")

    _notify(progress_callback, 0.25, "Validando sequências...")
    valid_sequences, invalid_sequences = validate_sequences(sequences, allow_n=allow_n)

    if not valid_sequences:
        _notify(progress_callback, 1.0, "Análise interrompida por sequências inválidas.")
        return {
            "summary": summarize_sequences([]),
            "total_sequences": len(sequences),
            "valid_count": 0,
            "invalid_count": len(invalid_sequences),
            "invalid_sequences": invalid_sequences,
            "results": [],
            "rankings": {},
        }

    _notify(progress_callback, 0.45, "Calculando estatísticas...")
    summary = summarize_sequences(valid_sequences)

    _notify(progress_callback, 0.6, "Carregando banco de referência local...")
    database = load_reference_database(reference_database_path)

    results: list[dict[str, object]] = []
    rankings: dict[str, list[dict[str, object]]] = {}
    total_valid = len(valid_sequences)

    for index, item in enumerate(valid_sequences, start=1):
        progress = 0.6 + (0.35 * index / total_valid)

        _notify(
            progress_callback,
            progress,
            f"Classificando sequência {index} de {total_valid}...",
        )

        classification = classify_sequence(
            item["sequence"],
            database,
            min_similarity=min_similarity,
            top_n=top_n,
        )

        rankings[item["id"]] = classification["ranking"]

        results.append(
            {
                "ID": item["id"],
                "Espécie escolhida": classification["species"],
                "Melhor similaridade (%)": classification["similarity"],
                "Referência escolhida": classification["reference_id"] or "-",
                "Status": "Identificada" if classification["identified"] else "Não identificada",
            }
        )

    _notify(progress_callback, 1.0, "Análise concluída.")

    return {
        "summary": summary,
        "total_sequences": len(sequences),
        "valid_count": len(valid_sequences),
        "invalid_count": len(invalid_sequences),
        "invalid_sequences": invalid_sequences,
        "results": results,
        "rankings": rankings,
    }