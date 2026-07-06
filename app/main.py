from pathlib import Path
import sys
import tempfile

import pandas as pd
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from src.services.analysis_service import AnalysisError, analyze_fasta_file


REFERENCE_DATABASE_PATH = (
    PROJECT_ROOT / "data" / "reference" / "species_database.csv"
)


st.set_page_config(
    page_title="BioTrace",
    page_icon="🌿",
    layout="wide",
)


st.title("🌿 BioTrace")

st.write(
    "MVP para análise simples de arquivos FASTA com validação de sequências, "
    "classificação por banco local e exportação dos resultados."
)


with st.sidebar:
    st.header("Parâmetros da análise")

    min_similarity = st.slider(
        "Limiar mínimo de similaridade (%)",
        min_value=0.0,
        max_value=100.0,
        value=95.0,
        step=0.5,
    )

    allow_n = st.checkbox(
        "Permitir base ambígua N",
        value=True,
    )

    st.caption(
        "Se a melhor correspondência ficar abaixo do limiar, "
        "a sequência será marcada como espécie não identificada."
    )


uploaded_file = st.file_uploader(
    "Envie um arquivo FASTA",
    type=["fasta", "fa"],
)


if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".fasta") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    progress_bar = st.progress(
        0.0,
        text="Preparando análise...",
    )

    def update_progress(value: float, message: str) -> None:
        progress_bar.progress(
            min(max(value, 0.0), 1.0),
            text=message,
        )

    try:
        analysis = analyze_fasta_file(
            file_path=temp_path,
            reference_database_path=str(REFERENCE_DATABASE_PATH),
            min_similarity=min_similarity,
            allow_n=allow_n,
            top_n=5,
            progress_callback=update_progress,
        )

    except AnalysisError as error:
        st.error(str(error))
        st.stop()

    except ValueError as error:
        st.error(f"Erro de configuração ou validação: {error}")
        st.stop()

    except Exception as error:
        st.error(f"Não foi possível concluir a análise: {error}")
        st.stop()

    finally:
        Path(temp_path).unlink(missing_ok=True)

    valid_count = analysis["valid_count"]
    invalid_count = analysis["invalid_count"]
    total_sequences = analysis["total_sequences"]

    if invalid_count:
        st.error(
            f"{invalid_count} sequência(s) inválida(s) foram encontrada(s) "
            "e não serão classificadas."
        )

        invalid_df = pd.DataFrame(analysis["invalid_sequences"])

        invalid_df["invalid_bases"] = invalid_df["invalid_bases"].apply(
            lambda bases: ", ".join(bases) if bases else "-"
        )

        invalid_df.columns = [
            "ID",
            "Bases inválidas",
            "Motivo",
        ]

        st.dataframe(
            invalid_df,
            use_container_width=True,
        )

    if valid_count == 0:
        st.warning("Nenhuma sequência válida ficou disponível para análise.")
        st.stop()

    st.success(
        f"Análise concluída: {valid_count} de {total_sequences} "
        "sequência(s) analisada(s)."
    )

    metric_col1, metric_col2, metric_col3 = st.columns(3)

    metric_col1.metric(
        "Sequências recebidas",
        total_sequences,
    )

    metric_col2.metric(
        "Sequências analisadas",
        valid_count,
    )

    metric_col3.metric(
        "Sequências inválidas",
        invalid_count,
    )

    summary = analysis["summary"]

    st.subheader("Estatísticas")

    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

    stat_col1.metric(
        "Total válido",
        summary["total_sequences"],
    )

    stat_col2.metric(
        "Maior sequência",
        f"{summary['max_length']} bp",
    )

    stat_col3.metric(
        "Menor sequência",
        f"{summary['min_length']} bp",
    )

    stat_col4.metric(
        "Comprimento médio",
        f"{summary['average_length']} bp",
    )

    gc_df = pd.DataFrame(summary["gc_by_sequence"])

    if not gc_df.empty:
        gc_df.columns = [
            "ID",
            "GC (%)",
        ]

        st.caption("Conteúdo GC por sequência válida")

        st.dataframe(
            gc_df,
            use_container_width=True,
        )

    st.subheader("Identificação taxonômica")

    results_df = pd.DataFrame(analysis["results"])

    st.dataframe(
        results_df,
        use_container_width=True,
    )

    st.subheader("Ranking das cinco melhores correspondências")

    for sequence_id, ranking in analysis["rankings"].items():
        selected_row = results_df.loc[results_df["ID"] == sequence_id].iloc[0]
        selected_species = selected_row["Espécie escolhida"]
        identified = selected_row["Status"] == "Identificada"

        ranking_df = pd.DataFrame(ranking)

        ranking_df.columns = [
            "Espécie",
            "Referência",
            "Similaridade (%)",
        ]

        ranking_df["Escolhida"] = ranking_df["Espécie"].apply(
            lambda species: "✅" if identified and species == selected_species else ""
        )

        with st.expander(f"Sequência {sequence_id}"):
            st.dataframe(
                ranking_df.style.apply(
                    lambda row: [
                        "font-weight: bold; background-color: #E8F5E9"
                        if row["Escolhida"] == "✅"
                        else ""
                        for _ in row
                    ],
                    axis=1,
                ),
                use_container_width=True,
            )

    st.subheader("Resumo por espécie escolhida")

    species_count = results_df["Espécie escolhida"].value_counts().reset_index()

    species_count.columns = [
        "Espécie",
        "Quantidade",
    ]

    st.dataframe(
        species_count,
        use_container_width=True,
    )

    st.subheader("Gráfico de espécies")

    st.bar_chart(
        species_count.set_index("Espécie")
    )

    csv = results_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Baixar resultados em CSV",
        data=csv,
        file_name="biotrace_results.csv",
        mime="text/csv",
    )