"""Object-oriented access to a validated reference database."""

from collections.abc import Iterator
from pathlib import Path

import pandas as pd

from src.reference.loader import load_reference_csv
from src.reference.validator import (
    validate_reference_dataframe,
)


class ReferenceDatabase:
    """Represent a validated local reference database."""

    def __init__(
        self,
        dataframe: pd.DataFrame,
        warnings: tuple[str, ...] = (),
    ) -> None:
        self._dataframe = dataframe.copy()
        self.warnings = warnings

    @classmethod
    def from_csv(
        cls,
        file_path: str | Path,
    ) -> "ReferenceDatabase":
        """Load, validate, and create a database instance."""
        loaded = load_reference_csv(file_path)
        validation = validate_reference_dataframe(loaded)

        return cls(
            validation.dataframe,
            validation.warnings,
        )

    def iter_records(
        self,
    ) -> Iterator[dict[str, str]]:
        """Yield records without exposing the DataFrame."""
        for record in self._dataframe.to_dict(
            orient="records"
        ):
            yield {
                str(key): str(value)
                for key, value in record.items()
            }

    def find_by_species(
        self,
        species: str,
    ) -> list[dict[str, str]]:
        """Return references for one species."""
        matches = self._dataframe[
            self._dataframe["species"] == species
        ]

        return [
            {
                str(key): str(value)
                for key, value in record.items()
            }
            for record in matches.to_dict(
                orient="records"
            )
        ]

    def list_species(self) -> list[str]:
        """Return unique species in alphabetical order."""
        return sorted(
            self._dataframe["species"]
            .unique()
            .tolist()
        )

    def list_ids(self) -> list[str]:
        """Return reference IDs in file order."""
        return self._dataframe["id"].tolist()

    def statistics(self) -> dict[str, int]:
        """Return basic database statistics."""
        return {
            "reference_count": len(self._dataframe),
            "species_count": (
                self._dataframe["species"].nunique()
            ),
            "id_count": (
                self._dataframe["id"].nunique()
            ),
        }