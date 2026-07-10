from pathlib import Path

import pytest


@pytest.fixture
def fasta_file(tmp_path: Path) -> Path:
    """Create a temporary FASTA file used by parser tests."""
    file_path = tmp_path / "sample.fasta"
    file_path.write_text(
        ">seq_1\nATCG\n>seq_2\natnn\n",
        encoding="utf-8",
    )
    return file_path