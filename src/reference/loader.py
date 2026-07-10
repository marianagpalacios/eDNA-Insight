from pathlib import Path

import pandas as pd
from pandas.errors import EmptyDataError, ParserError


class ReferenceDatabaseLoadError(Exception):
    """Raised when a reference CSV cannot be read safely."""


def load_reference_csv(file_path: str | Path) -> pd.DataFrame:
    """Load a reference CSV without applying biological validation."""
    path = Path(file_path)

    if not path.exists():
        raise ReferenceDatabaseLoadError(
            f"Banco de referência não encontrado: {path}."
        )

    if not path.is_file():
        raise ReferenceDatabaseLoadError(
            f"O caminho do banco de referência não é um arquivo: {path}."
        )

    try:
        return pd.read_csv(
            path,
            dtype=str,
            keep_default_na=False,
            skip_blank_lines=False,
        )

    except EmptyDataError as error:
        raise ReferenceDatabaseLoadError(
            "O arquivo do banco de referência está vazio."
        ) from error

    except ParserError as error:
        raise ReferenceDatabaseLoadError(
            "O CSV do banco de referência está malformado."
        ) from error

    except OSError as error:
        raise ReferenceDatabaseLoadError(
            f"Não foi possível acessar o banco de referência: {error}."
        ) from error