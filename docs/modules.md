# Módulos do BioTrace

## `src/fasta.py`

Responsável pela leitura de arquivos FASTA usando Biopython. Retorna as sequências em formato padronizado, com `id` e `sequence`.

## `src/validation.py`

Valida as sequências antes da análise. Aceita `A`, `T`, `C`, `G` e, opcionalmente, `N`. Sequências vazias ou com bases inválidas são separadas e não seguem para classificação.

## `src/stats.py`

Calcula estatísticas básicas das sequências válidas, incluindo quantidade, tamanho mínimo, tamanho máximo, comprimento médio e conteúdo GC.

## `src/similarity.py`

Calcula similaridade simples entre duas sequências por comparação posição a posição. Esta abordagem é suficiente para o MVP, mas não substitui alinhamento biológico real.

## `src/taxonomy.py`

Carrega o banco local de referência, calcula ranking das melhores correspondências e classifica a sequência aplicando o limiar mínimo de similaridade.

## `src/services/analysis_service.py`

Orquestra o fluxo completo de análise e isola as regras de negócio da interface Streamlit.

## `app/main.py`

Implementa a interface web em Streamlit, incluindo upload, parâmetros, mensagens, tabelas, ranking, gráfico e exportação CSV.
