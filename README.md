# 🌿 BioTrace

> Plataforma open source para análise automatizada de DNA ambiental (eDNA), identificação taxonômica simplificada e geração de indicadores iniciais de biodiversidade.

> **Status:** MVP v0.2.0 — análise de arquivos FASTA com validação de sequências, limiar mínimo de similaridade, ranking de correspondências e banco local com múltiplas referências por espécie.

---

## 📖 Sobre o projeto

O **BioTrace** é um software científico em desenvolvimento voltado para análise inicial de sequências de DNA ambiental, conhecido como **eDNA** (*Environmental DNA*). O objetivo do projeto é tornar etapas básicas de análise bioinformática mais acessíveis, reprodutíveis e compreensíveis por meio de uma interface web simples feita com Streamlit.

Nesta versão, o BioTrace ainda não substitui ferramentas consolidadas de bioinformática, como BLAST, Kraken2, QIIME2 ou DADA2. O foco atual é construir a base do sistema de forma incremental, utilizando apenas arquivos FASTA, banco local em CSV, Python, Biopython, Pandas e Streamlit.

---

## ✅ Funcionalidades implementadas

### MVP v0.1.0 — Base inicial

- Leitura de arquivos FASTA com Biopython.
- Upload de arquivos pela interface Streamlit.
- Cálculo de estatísticas básicas das sequências.
- Cálculo de conteúdo GC.
- Cálculo simples de similaridade entre sequências.
- Identificação taxonômica simplificada com banco local em CSV.
- Exibição dos resultados em tabela.
- Gráfico de distribuição por espécie.
- Exportação dos resultados em CSV.
- Documentação inicial em `docs/learning`.

### MVP v0.2.0 — Evolução incremental

- Renomeação completa do projeto para **BioTrace**.
- Validação das sequências antes do processamento.
- Aceitação das bases `A`, `T`, `C`, `G` e, opcionalmente, `N`.
- Bloqueio de classificação para sequências inválidas.
- Exibição das sequências inválidas com motivo e bases problemáticas.
- Limiar mínimo de similaridade configurável pela interface.
- Retorno de **Espécie não identificada** quando nenhuma correspondência ultrapassa o limiar.
- Ranking das cinco melhores correspondências por sequência analisada.
- Destaque visual da espécie escolhida no ranking.
- Banco local com múltiplas sequências de referência por espécie.
- Barra de progresso durante a análise.
- Mensagens claras de sucesso, erro e alerta.
- Indicadores de sequências recebidas, analisadas e inválidas.
- Camada de serviço para separar regra de negócio da interface.
- Atualização da documentação técnica do projeto.

---

## 🧬 Fluxo atual de processamento

O fluxo do MVP v0.2.0 funciona da seguinte forma:

1. O usuário envia um arquivo FASTA pela interface.
2. O arquivo é salvo temporariamente para leitura.
3. O BioTrace lê as sequências usando Biopython.
4. As sequências são validadas antes de qualquer análise.
5. Sequências inválidas são separadas e não são classificadas.
6. Sequências válidas seguem para cálculo de estatísticas.
7. O banco local de referência em CSV é carregado.
8. Cada sequência válida é comparada com todas as sequências do banco.
9. O sistema calcula um ranking das melhores correspondências por espécie.
10. O limiar mínimo de similaridade é aplicado.
11. Os resultados são exibidos em tabela, ranking, gráfico e exportação CSV.

---

## 🧪 Validação de sequências

Antes da classificação, o BioTrace verifica se as sequências possuem apenas bases válidas.

Por padrão, são aceitas:

```text
A, T, C, G, N
```

A base `N` representa uma base ambígua. Pela interface, o usuário pode desativar a aceitação de `N`, permitindo apenas:

```text
A, T, C, G
```

Sequências vazias ou com caracteres inválidos são exibidas ao usuário e não entram no processo de classificação.

---

## 🎚️ Limiar mínimo de similaridade

A interface possui um parâmetro configurável chamado **Limiar mínimo de similaridade (%)**.

Exemplo:

```text
95%
```

Se a melhor correspondência de uma sequência estiver abaixo desse valor, o resultado será:

```text
Espécie não identificada
```

Isso evita que o sistema force uma identificação quando a similaridade encontrada é baixa.

---

## 🧾 Banco de referência local

O banco de referência fica em:

```text
data/reference/species_database.csv
```

A estrutura esperada é:

```csv
species,id,sequence
Danio rerio,DRE001,ATCGATCGATCGATCG
Danio rerio,DRE002,ATCGATCGATCGATTG
Cyprinus carpio,CCA001,ATCGATCGATCGTTTG
```

Cada linha representa uma sequência de referência. A mesma espécie pode aparecer em várias linhas, desde que cada sequência tenha um `id` próprio.

Colunas obrigatórias:

| Coluna | Descrição |
|---|---|
| `species` | Nome da espécie de referência. |
| `id` | Identificador único da sequência de referência. |
| `sequence` | Sequência de DNA usada na comparação. |

A classificação considera todas as sequências disponíveis no banco. Para o ranking final, cada espécie aparece uma vez, representada pela sua melhor sequência de referência.

---

## 📂 Estrutura atual do projeto

```text
BioTrace/
├── app/
│   └── main.py
├── data/
│   ├── examples/
│   │   └── sample.fasta
│   └── reference/
│       └── species_database.csv
├── docs/
│   ├── architecture.md
│   ├── modules.md
│   ├── roadmap.md
│   └── learning/
│       ├── MVP0.md
│       ├── MVP1.md
│       └── fundamentos.md
├── src/
│   ├── __init__.py
│   ├── fasta.py
│   ├── similarity.py
│   ├── stats.py
│   ├── taxonomy.py
│   ├── validation.py
│   └── services/
│       ├── __init__.py
│       └── analysis_service.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧱 Organização dos módulos

| Arquivo | Responsabilidade |
|---|---|
| `app/main.py` | Interface Streamlit. Exibe upload, parâmetros, mensagens, tabelas, ranking, gráfico e exportação. |
| `src/fasta.py` | Leitura de arquivos FASTA usando Biopython. |
| `src/validation.py` | Validação das sequências e separação entre válidas e inválidas. |
| `src/stats.py` | Cálculo de estatísticas básicas e conteúdo GC. |
| `src/similarity.py` | Cálculo simples de similaridade entre sequências. |
| `src/taxonomy.py` | Carregamento do banco local, ranking e classificação por similaridade. |
| `src/services/analysis_service.py` | Orquestra o fluxo completo de análise. |

A interface Streamlit não concentra mais as regras principais de negócio. Essa responsabilidade foi movida para a camada de serviço em `src/services/analysis_service.py`.

---

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/marianagpalacios/BioTrace.git
cd BioTrace
```

### 2. Criar ambiente virtual

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

No Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
streamlit run app/main.py
```

---

## 🧪 Como testar manualmente

Use o arquivo de exemplo:

```text
data/examples/sample.fasta
```

Com o limiar padrão de 95%, o comportamento esperado é:

- sequências compatíveis com o banco devem ser identificadas;
- sequências com baixa similaridade devem aparecer como **Espécie não identificada**;
- sequências com bases inválidas devem ser bloqueadas e exibidas como inválidas;
- o ranking deve mostrar as cinco melhores correspondências disponíveis.

Também é possível verificar a sintaxe do projeto com:

```bash
python -m compileall app src
```

---

## 🛠️ Tecnologias utilizadas

- Python
- Streamlit
- Biopython
- Pandas

---

## 🗺️ Roadmap

### Versão 0.1.0 — MVP inicial

- [x] Leitura de arquivos FASTA.
- [x] Upload pela interface.
- [x] Estatísticas básicas.
- [x] Conteúdo GC.
- [x] Banco local em CSV.
- [x] Similaridade simples.
- [x] Identificação taxonômica simplificada.
- [x] Tabela, gráfico e exportação CSV.

### Versão 0.2.0 — Validação, ranking e melhor organização

- [x] Validação de sequências.
- [x] Suporte opcional à base `N`.
- [x] Limiar mínimo de similaridade.
- [x] Retorno de **Espécie não identificada** abaixo do limiar.
- [x] Ranking das cinco melhores correspondências.
- [x] Banco local com múltiplas sequências por espécie.
- [x] Barra de progresso.
- [x] Mensagens de sucesso, erro e alerta.
- [x] Camada de serviço para orquestração da análise.
- [x] Atualização da documentação.

### Próximo MVP sugerido — v0.3.0

Foco recomendado: **qualidade e confiabilidade**.

- [ ] Criar testes automatizados.
- [ ] Testar validação de sequências.
- [ ] Testar limiar mínimo de similaridade.
- [ ] Testar ranking das correspondências.
- [ ] Validar o banco de referência antes da análise.
- [ ] Detectar IDs duplicados no banco local.
- [ ] Exportar também o ranking completo em CSV.
- [ ] Melhorar tratamento de empates entre espécies.
- [ ] Adicionar documentação de contribuição.

### Versões futuras

- [ ] Suporte a FASTQ.
- [ ] Estatísticas de qualidade Phred.
- [ ] Índices de biodiversidade.
- [ ] Relatórios em PDF.
- [ ] Docker.
- [ ] GitHub Actions.
- [ ] Integração futura com ferramentas consolidadas de bioinformática, como BLAST ou Kraken2.

---

## ⚠️ Limitações atuais

O BioTrace v0.2.0 ainda possui limitações importantes:

- não utiliza BLAST;
- não utiliza Kraken2;
- não utiliza QIIME2;
- não utiliza DADA2;
- não acessa bancos online;
- não processa arquivos FASTQ;
- não realiza alinhamento biológico real;
- a similaridade ainda é calculada por comparação simples de posições.

Essas limitações são intencionais nesta fase, pois o projeto está evoluindo como MVP incremental.

---

## 📌 Observação científica

Os resultados gerados nesta versão devem ser interpretados como uma demonstração computacional e educacional do fluxo de análise. Para aplicações científicas reais, será necessário integrar métodos de alinhamento, bancos de referência curados, controle de qualidade e validação estatística.
