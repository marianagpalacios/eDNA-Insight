# BioTrace MVP v0.3.0 — Qualidade e confiabilidade

## 1. Objetivo

O MVP v0.3.0 foi criado para melhorar a confiabilidade do BioTrace antes da introdução de tecnologias mais complexas.

A versão não adiciona FASTQ, BLAST, IA, Docker ou bancos online.

O foco é fortalecer:

- testes;
- qualidade dos dados;
- separação de responsabilidades;
- estatísticas;
- observabilidade;
- documentação;
- preparação para evolução.

---

## 2. Situação anterior

O MVP v0.2.0 já possuía:

- leitura FASTA;
- validação das consultas;
- base `N` opcional;
- estatísticas básicas;
- similaridade posicional;
- classificação simplificada;
- limiar mínimo;
- ranking;
- banco CSV;
- interface;
- exportação;
- serviço de análise.

Os principais riscos eram:

- ausência de testes;
- valores hardcoded;
- banco acoplado à taxonomia;
- validação parcial do CSV;
- descarte silencioso de linhas;
- similaridade frágil a indels;
- poucas métricas;
- ausência de logs.

---

## 3. Entregas

### 3.1 Testes automatizados

Foi criada a estrutura com pytest.

A suíte final possui 28 testes.

Cobertura funcional:

- FASTA;
- validação;
- loader;
- validator;
- `ReferenceDatabase`;
- similaridade;
- taxonomia;
- estatísticas;
- logging.

### 3.2 Configuração centralizada

Parâmetros foram movidos para `src/config.py`.

Isso reduz inconsistência entre interface e serviço.

### 3.3 Camada de referência

Foram criados:

```text
src/reference/loader.py
src/reference/validator.py
src/reference/database.py
```

O módulo taxonômico deixou de carregar CSV diretamente.

### 3.4 Validação do banco

Erros bloqueantes:

- colunas ausentes;
- linhas vazias;
- IDs vazios;
- IDs duplicados;
- espécies sem nome;
- sequências vazias;
- caracteres inválidos.

Avisos:

- espaços removidos;
- minúsculas convertidas;
- opcionais ausentes;
- capitalização inconsistente.

### 3.5 Similaridade

A comparação posicional foi substituída por distância de edição normalizada.

A nova estratégia reconhece:

- substituições;
- inserções;
- deleções;
- comprimentos diferentes.

### 3.6 Estatísticas

Foram adicionadas:

- A%;
- T%;
- C%;
- G%;
- AT%;
- mediana;
- desvio padrão;
- métricas individuais;
- quantidade de `N`.

### 3.7 Logging

A execução registra:

- início;
- parâmetros;
- quantidade de registros;
- IDs inválidos;
- avisos do banco;
- falhas;
- duração.

### 3.8 Interface

A interface passou a mostrar:

- tempo;
- novas métricas;
- ranking configurável;
- estatísticas do banco;
- avisos;
- três exportações.

---

## 4. Item transferido

O banco com sequências reais foi transferido para o MVP v0.4.0.

### Motivo

Curadoria de dados científicos exige:

- definição do marcador;
- pesquisa de registros;
- conferência de accessions;
- avaliação da região;
- análise de comprimentos;
- documentação da origem;
- versionamento do conjunto.

Realizar essa tarefa como um MVP separado permite aprender o processo corretamente e evita inserir sequências sem rastreabilidade.

### Consequência

A arquitetura do banco está pronta, mas o conteúdo atual permanece demonstrativo.

---

## 5. Princípios de Engenharia de Software

### Responsabilidade única

- loader lê;
- validator valida;
- database representa;
- taxonomy classifica;
- stats mede;
- service coordena;
- interface apresenta.

### Baixo acoplamento

A classificação depende de `ReferenceDatabase`, não do CSV diretamente.

### Alta coesão

Regras relacionadas permanecem agrupadas.

### Fail fast

Erros estruturais interrompem a análise com mensagens claras.

### Encapsulamento

O DataFrame interno do banco não é exposto.

### Testabilidade

Funções e classes podem ser verificadas sem executar o Streamlit.

### Evolução incremental

Nenhuma ferramenta complexa foi introduzida antes da estabilização da base.

---

## 6. Conceitos de Bioinformática estudados

- FASTA;
- alfabeto de DNA;
- base ambígua `N`;
- composição nucleotídica;
- conteúdo AT e GC;
- indels;
- distância de edição;
- classificação por referência;
- importância do limiar;
- importância da cobertura do banco;
- diferença entre similaridade e alinhamento;
- necessidade de proveniência.

---

## 7. Trade-offs

### Levenshtein versus Needleman–Wunsch

Levenshtein foi escolhida porque:

- é compreensível;
- trata indels;
- não exige parâmetros biológicos prematuros.

Ela foi aceita com a limitação de não ser um alinhamento biológico.

### CSV versus banco de dados

CSV foi mantido porque:

- o conjunto é pequeno;
- é inspecionável;
- facilita aprendizado;
- não exige infraestrutura.

SQLite ou bancos externos só serão avaliados quando houver necessidade.

### Dicionários versus modelos tipados

Dicionários foram preservados para evitar uma refatoração ampla.

Modelos tipados entram quando os contratos estiverem estáveis.

### Logging padrão versus ferramenta externa

`logging` atende ao MVP sem dependências adicionais.

---

## 8. Fluxo Git utilizado

A versão foi desenvolvida em:

```text
feature/mvp-0.3
```

Os commits foram divididos por tema:

- testes;
- configuração;
- validação do banco;
- abstração do banco;
- similaridade;
- estatísticas;
- logging;
- interface;
- documentação.

A branch foi integrada à `main` por Pull Request.

A versão estável deve ser marcada com:

```text
v0.3.0
```

---

## 9. Critérios de aceite

O MVP é considerado concluído quando:

- a suíte passa;
- a aplicação compila;
- a interface executa;
- o arquivo de exemplo é analisado;
- erros do banco são apresentados;
- logs são gerados;
- exportações funcionam;
- documentação reflete o código;
- limitações são explícitas.

A curadoria do banco não faz parte do critério revisado desta versão.

---

## 10. Pontos fortes após o MVP

- arquitetura mais modular;
- responsabilidades claras;
- erros explícitos;
- testes úteis;
- algoritmo mais robusto;
- métricas mais completas;
- logs;
- interface informativa;
- base preparada para outro backend de referência.

---

## 11. Limitações restantes

- banco fictício;
- sem proveniência;
- sem complemento reverso;
- sem alinhamento;
- sem FASTQ;
- sem Phred;
- sem BLAST;
- sem manifesto;
- sem CI;
- sem modelos tipados;
- sem teste integrado do serviço;
- sem licença formal;
- desempenho não caracterizado.

---

## 12. Próxima etapa

O MVP v0.4.0 deve ser dedicado ao banco de referência e sua proveniência.

Isso transforma a camada já criada em um componente cientificamente mais confiável antes de avançar para FASTQ ou BLAST.