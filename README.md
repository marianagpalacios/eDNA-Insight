# 🌿 eDNA Insight

> Plataforma open source para análise automatizada de DNA ambiental (eDNA), identificação taxonômica e geração de indicadores de biodiversidade.

## 📖 Sobre o projeto

O **eDNA Insight** é um projeto em desenvolvimento que tem como objetivo simplificar a análise de dados de DNA ambiental (Environmental DNA - eDNA), permitindo que pesquisadores realizem análises de biodiversidade de forma mais acessível, automatizada e reprodutível.

A proposta é integrar diferentes etapas do pipeline de bioinformática em uma única plataforma, desde a leitura de arquivos de sequenciamento até a geração de relatórios e visualizações interativas.

Este projeto também servirá como base para um Trabalho de Conclusão de Curso (TCC) em Bioinformática.

---

# 🎯 Objetivos

* Automatizar análises de DNA ambiental.
* Facilitar a identificação taxonômica de espécies.
* Gerar métricas de biodiversidade.
* Produzir relatórios científicos automaticamente.
* Tornar ferramentas de bioinformática mais acessíveis através de uma interface intuitiva.

---

# 🚀 Roadmap

## Versão 0.1 — Manipulação de sequências

* [ ] Leitura de arquivos FASTA
* [ ] Estatísticas básicas das sequências
* [ ] Cálculo de conteúdo GC
* [ ] Comprimento médio das sequências
* [ ] Exportação de relatório

---

## Versão 0.2 — Suporte a FASTQ

* [ ] Leitura de arquivos FASTQ
* [ ] Estatísticas de qualidade
* [ ] Distribuição do tamanho das leituras

---

## Versão 0.3 — Interface Web

* [ ] Interface utilizando Streamlit
* [ ] Upload de arquivos
* [ ] Visualização de resultados
* [ ] Download de relatórios

---

## Versão 0.4 — Classificação Taxonômica

* [ ] Integração com BLAST
* [ ] Integração com Kraken2
* [ ] Identificação automática de espécies

---

## Versão 0.5 — Biodiversidade

* [ ] Índices de diversidade
* [ ] Abundância relativa
* [ ] Comparação entre amostras

---

## Versão 1.0

* [ ] Pipeline completo
* [ ] Dashboard interativo
* [ ] Relatórios em PDF
* [ ] Docker
* [ ] Testes automatizados
* [ ] Documentação completa

---

# 🛠️ Tecnologias

Planejadas para o desenvolvimento:

* Python
* Biopython
* Pandas
* NumPy
* Plotly
* Streamlit
* SQLite
* Docker
* GitHub Actions

---

# 📂 Estrutura inicial

```text
edna-insight/

├── app/
├── analysis/
├── parsers/
├── taxonomy/
├── reports/
├── database/
├── tests/
├── docs/
├── data/
├── notebooks/
└── README.md
```

---

# 📅 Status do projeto

🚧 Em desenvolvimento inicial.

Atualmente o foco está na implementação da leitura e análise básica de arquivos biológicos, estabelecendo a base para as futuras funcionalidades.

---

# 💡 Visão de longo prazo

O objetivo é que o eDNA Insight evolua para uma plataforma capaz de:

* interpretar dados de eDNA de forma automatizada;
* integrar ferramentas consolidadas de bioinformática;
* gerar visualizações interativas;
* produzir relatórios científicos;
* apoiar pesquisas em conservação ambiental e monitoramento da biodiversidade.

---

# 🤝 Contribuições

Contribuições, sugestões e discussões são bem-vindas. Conforme o projeto amadurecer, serão disponibilizadas diretrizes para colaboração.

---

# 📄 Licença

Este projeto será distribuído sob a licença MIT.
