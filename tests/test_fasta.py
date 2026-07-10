from pathlib import Path

from src.fasta import read_fasta


def test_read_fasta_returns_ids_and_sequences(fasta_file: Path) -> None:
    records = read_fasta(str(fasta_file))

    assert records == [
        {"id": "seq_1", "sequence": "ATCG"},
        {"id": "seq_2", "sequence": "atnn"},
    ]


def test_read_fasta_returns_empty_list_for_empty_file(tmp_path: Path) -> None:
    empty_file = tmp_path / "empty.fasta"
    empty_file.write_text("", encoding="utf-8")

    assert read_fasta(str(empty_file)) == []