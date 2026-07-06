# Arquitetura do BioTrace

O BioTrace segue uma arquitetura simples, modular e incremental, adequada para um MVP científico em evolução.

## Camadas principais

- `app/`: interface Streamlit.
- `src/`: módulos centrais da aplicação.
- `src/services/`: camada de serviço responsável por orquestrar o fluxo de análise.
- `data/examples/`: arquivos FASTA de exemplo.
- `data/reference/`: banco local de referência em CSV.
- `docs/`: documentação técnica e registros de evolução.

## Decisão arquitetural principal

A interface Streamlit não deve concentrar regra de negócio. Por isso, o fluxo principal foi movido para `src/services/analysis_service.py`.

Esse serviço coordena:

1. leitura do FASTA;
2. validação das sequências;
3. cálculo de estatísticas;
4. carregamento do banco de referência;
5. classificação por similaridade;
6. montagem dos resultados para a interface.

Essa organização reduz acoplamento e facilita a criação de testes automatizados em versões futuras.
