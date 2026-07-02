# 📚 Developer Notebook — Fundamentos de Bioinformática para eDNA

> Este documento reúne os principais conceitos estudados durante o desenvolvimento do projeto **eDNA Insight**. Seu objetivo é registrar o aprendizado, organizar referências e servir como base para a implementação do software e para a futura escrita do Trabalho de Conclusão de Curso (TCC).

---

# Visão Geral

O objetivo do projeto é desenvolver uma plataforma capaz de automatizar parte da análise de dados de DNA ambiental (eDNA), desde a leitura dos arquivos gerados pelo sequenciamento até a produção de relatórios sobre biodiversidade.

Para isso, é necessário compreender como os dados são produzidos e quais etapas de processamento são realizadas em um pipeline de bioinformática.

O fluxo geral pode ser representado da seguinte forma:

```text
Ambiente (rio, lago, solo...)

        │

        ▼

Coleta da amostra

        │

        ▼

Extração do DNA

        │

        ▼

Sequenciamento

        │

        ▼

Arquivos FASTQ

        │

        ▼

Controle de qualidade

        │

        ▼

Filtragem

        │

        ▼

Identificação das sequências

        │

        ▼

Classificação taxonômica

        │

        ▼

Análises ecológicas

        │

        ▼

Relatórios e visualizações
```

Cada etapa desse fluxo será estudada ao longo do desenvolvimento do projeto.

---

# O que é eDNA?

Environmental DNA (eDNA) é o DNA presente no ambiente.

Organismos deixam constantemente material genético em locais como rios, lagos, oceanos, solo e até no ar.

Esse DNA pode ser proveniente de:

* células mortas;
* escamas;
* pelos;
* fezes;
* saliva;
* raízes;
* pólen;
* secreções.

Ao coletar uma amostra ambiental e sequenciar esse material genético, torna-se possível inferir quais organismos estiveram presentes naquele ambiente sem a necessidade de capturá-los.

---

# Sequenciamento

O sequenciamento consiste em determinar a ordem das bases nitrogenadas do DNA.

Como os genomas são muito grandes, os equipamentos não leem todo o DNA de uma única vez.

Eles produzem milhões de pequenos fragmentos chamados **reads**.

Esses reads representam a matéria-prima utilizada pela bioinformática.

---

# FASTQ

O formato FASTQ armazena as leituras produzidas pelo sequenciamento.

Cada sequência possui:

* identificador;
* sequência de nucleotídeos;
* informações de qualidade.

A qualidade informa a confiança da máquina em cada base identificada.

Esses dados são utilizados para remover leituras com baixa confiabilidade antes das análises.

---

# FASTA

O formato FASTA é uma versão simplificada.

Ele contém apenas:

* identificador;
* sequência.

Não armazena informações sobre qualidade.

É amplamente utilizado para armazenar sequências de referência e resultados já processados.

---

# Classificação Taxonômica

Após o sequenciamento, é necessário descobrir a qual organismo pertence cada sequência.

Isso é feito comparando as leituras obtidas com bancos de dados contendo sequências já conhecidas.

Quanto maior a similaridade entre duas sequências, maior a probabilidade de elas pertencerem ao mesmo organismo ou a organismos próximos evolutivamente.

Ferramentas como BLAST e Kraken2 realizam esse processo utilizando estratégias diferentes.

---

# OTUs

Durante muitos anos, sequências semelhantes eram agrupadas em unidades chamadas OTUs (Operational Taxonomic Units).

Normalmente utilizava-se um limiar de aproximadamente 97% de similaridade.

Essa abordagem reduz o impacto de erros de sequenciamento, mas pode agrupar organismos biologicamente distintos.

---

# ASVs

ASVs (Amplicon Sequence Variants) representam uma abordagem mais moderna.

Em vez de agrupar sequências semelhantes, algoritmos estatísticos tentam reconstruir as sequências biológicas reais, separando diferenças causadas por erro de sequenciamento das diferenças realmente existentes entre organismos.

Hoje, ASVs são consideradas o padrão para muitos estudos de metabarcoding.

---

# QIIME2

QIIME2 é uma plataforma de bioinformática que organiza diversas etapas da análise de microbiomas e eDNA.

Entre suas funcionalidades estão:

* controle de qualidade;
* filtragem;
* geração de ASVs;
* classificação taxonômica;
* cálculo de diversidade;
* visualizações.

Ele funciona como um pipeline completo para análise de dados.

---

# Kraken2

Kraken2 é uma ferramenta de classificação taxonômica extremamente rápida.

Seu funcionamento baseia-se na comparação de pequenos fragmentos das sequências (k-mers) com um banco de dados previamente indexado.

Por essa razão, consegue classificar milhões de sequências em poucos minutos.

---

# Objetivo do eDNA Insight

O projeto não pretende substituir ferramentas consolidadas da bioinformática.

O objetivo é integrar diferentes ferramentas em uma plataforma única, automatizando tarefas repetitivas e tornando o processo mais acessível para pesquisadores.

A ideia é que o usuário forneça apenas os arquivos de entrada e receba automaticamente análises, gráficos e relatórios organizados.

---

# Conceitos que ainda preciso estudar

* [ ] Estrutura do DNA
* [ ] PCR
* [ ] Amplicons
* [ ] Tecnologias de sequenciamento (Illumina, Nanopore e PacBio)
* [ ] Qualidade Phred
* [ ] Bancos de dados biológicos (NCBI, SILVA, BOLD, GTDB)
* [ ] BLAST
* [ ] Kraken2
* [ ] DADA2
* [ ] QIIME2
* [ ] Diversidade alfa
* [ ] Diversidade beta
* [ ] Índices de Shannon e Simpson
* [ ] Árvores filogenéticas
* [ ] Metabarcoding
* [ ] Snakemake
* [ ] Nextflow
* [ ] Docker aplicado à bioinformática

---

# Ideias para o projeto

*(Espaço reservado para registrar novas ideias durante os estudos.)*

---

# Dúvidas

*(Espaço reservado para registrar perguntas que surgirem durante o desenvolvimento.)*

---

# Referências

*(Artigos, livros, cursos e documentações consultadas.)*