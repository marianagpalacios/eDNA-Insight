# 🌿 BioTrace

> Plataforma open source para análise automatizada de DNA ambiental (eDNA), identificação taxonômica e geração de indicadores de biodiversidade.

> **Status:** MVP v0.1.0 — prova de conceito inicial.

## 📖 Sobre o projeto

O **eDNA Insight** é um projeto em desenvolvimento que tem como objetivo simplificar a análise de dados de DNA ambiental (Environmental DNA - eDNA), permitindo que pesquisadores realizem análises de biodiversidade de forma mais acessível, automatizada e reprodutível.

A proposta é integrar diferentes etapas do pipeline de bioinformática em uma única plataforma, desde a leitura de arquivos de sequenciamento até a geração de relatórios e visualizações interativas.

---

# ✅ O que já foi feito — MVP v0.1.0

A primeira versão funcional do projeto implementa um fluxo simplificado para análise de arquivos FASTA.

Funcionalidades já implementadas:

* Leitura de arquivos FASTA com Biopython.
* Upload de arquivos pela interface web.
* Cálculo de estatísticas básicas das sequências.
* Cálculo de conteúdo GC.
* Identificação taxonômica simplificada usando banco local em CSV.
* Cálculo de similaridade simples entre sequências.
* Exibição dos resultados em tabela.
* Resumo da quantidade de sequências por espécie provável.
* Gráfico de barras com a distribuição das espécies.
* Exportação dos resultados em CSV.
* Documentação inicial em `docs/learning`.

---

# 🎯 Objetivos

* Automatizar análises de DNA ambiental.
* Facilitar a identificação taxonômica de espécies.
* Gerar métricas de biodiversidade.
* Produzir relatórios científicos automaticamente.
* Tornar ferramentas de bioinformática mais acessíveis através de uma interface intuitiva.

---

# 🚀 Roadmap

## Versão 0.1 — MVP inicial: análise de FASTA

* [x] Leitura de arquivos FASTA
* [x] Upload de arquivos pela interface
* [x] Estatísticas básicas das sequências
* [x] Cálculo de conteúdo GC
* [x] Comprimento médio das sequências
* [x] Banco local de referência em CSV
* [x] Similaridade simples entre sequências
* [x] Identificação taxonômica simplificada
* [x] Tabela de resultados
* [x] Gráfico de distribuição por espécie
* [x] Exportação dos resultados em CSV

---

## Versão 0.2 — Melhorias no MVP

* [ ] Validação de sequências
* [ ] Filtro mínimo de similaridade
* [ ] Tratamento de erros na interface
* [ ] Melhoria do banco local de referência
* [ ] Uso de sequências reais de referência
* [ ] Testes automatizados

---

## Versão 0.3 — Suporte a FASTQ

* [ ] Leitura de arquivos FASTQ
* [ ] Estatísticas de qualidade
* [ ] Distribuição do tamanho das leituras
* [ ] Análise de qualidade Phred

---

## Versão 0.4 — Classificação Taxonômica

* [ ] Integração com BLAST
* [ ] Integração com Kraken2
* [ ] Identificação automática de espécies
* [ ] Suporte a bancos biológicos reais

---

## Versão 0.5 — Biodiversidade

* [ ] Índices de diversidade
* [ ] Abundância relativa
* [ ] Comparação entre amostras
* [ ] Visualizações ecológicas

---

## Versão 1.0

* [ ] Pipeline completo
* [ ] Dashboard interativo
* [ ] Relatórios em PDF
* [ ] Docker
* [ ] GitHub Actions
* [ ] Testes automatizados
* [ ] Documentação completa

---

# 🛠️ Tecnologias

Utilizadas no MVP atual:

* Python
* Biopython
* Pandas
* Streamlit

Planejadas para próximas versões:

* NumPy
* Plotly
* SQLite
* Docker
* GitHub Actions
* BLAST
* Kraken2

---

# 📂 Estrutura atual

```text
edna-insight/

├── app/
│   └── main.py
├── src/
│   ├── fasta.py
│   ├── stats.py
│   ├── similarity.py
│   └── taxonomy.py
├── data/
│   ├── examples/
│   │   └── sample.fasta
│   └── reference/
│       └── species_database.csv
├── docs/
│   └── learning/
├── tests/
├── requirements.txt
└── README.md
