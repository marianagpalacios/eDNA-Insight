import pandas as pd
from src.similarity import calculate_similarity

def load_reference_database(file_path):
    return pd.read_csv(file_path)

def exact_match(sequence, database):
    sequence = sequence.upper()

    for _, row in database.iterrows():
        if sequence == row["sequence"].upper():
            return row["species"]

    return "Não identificado"

def best_similarity_match(sequence, database):
    best_species = None
    best_score = 0

    for _, row in database.iterrows():
        score = calculate_similarity(sequence, row["sequence"])

        if score > best_score:
            best_score = score
            best_species = row["species"]

    return {
        "species": best_species,
        "similarity": best_score
    }