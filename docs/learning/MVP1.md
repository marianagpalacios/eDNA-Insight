# MVP 1 — BioTrace v0.2.0

Esta etapa registra a evolução do BioTrace para o MVP v0.2.0. O objetivo principal foi melhorar a confiabilidade da análise, organizar melhor o código e preparar o projeto para novas versões, sem reescrever a arquitetura do zero.

O BioTrace continua sendo um software científico em desenvolvimento para análise inicial de sequências de DNA ambiental, utilizando arquivos FASTA, banco local em CSV, Python, Biopython, Pandas e Streamlit.

---

## Objetivo da versão

O MVP v0.2.0 teve como foco evoluir a base inicial do projeto com melhorias incrementais. As principais metas foram:

* renomear completamente o projeto para BioTrace;
* validar sequências antes da análise;
* impedir que sequências inválidas sejam classificadas;
* adicionar um limiar mínimo de similaridade;
* mostrar um ranking das melhores correspondências;
* permitir múltiplas sequências de referência por espécie;
* melhorar a interface Streamlit;
* separar melhor as regras de negócio da interface;
* atualizar a documentação do projeto.

---

## Visão geral do fluxo

O fluxo atual do BioTrace funciona como uma linha de processamento:

```text
Arquivo FASTA enviado pelo usuário
        ↓
Leitura do arquivo
        ↓
Validação das sequências
        ↓
Cálculo de estatísticas
        ↓
Carregamento do banco local
        ↓
Comparação por similaridade
        ↓
Classificação taxonômica simplificada
        ↓
Exibição dos resultados na interface
        ↓
Exportação CSV
```

A ideia é garantir que cada etapa tenha uma responsabilidade clara e que o projeto continue simples de entender e evoluir.

---

## Organização dos principais arquivos

A arquitetura foi mantida modular. Cada arquivo possui uma função específica:

```text
app/main.py
```

Responsável pela interface Streamlit. Mostra o upload do arquivo, parâmetros, mensagens, tabelas, ranking, gráfico e botão de exportação.

```text
src/fasta.py
```

Responsável pela leitura dos arquivos FASTA usando Biopython. Ele transforma as sequências em uma lista de dicionários com `id` e `sequence`.

```text
src/validation.py
```

Responsável pela validação das sequências. Verifica se cada sequência possui apenas bases válidas: `A`, `T`, `C`, `G` e, opcionalmente, `N`.

```text
src/stats.py
```

Responsável pelo cálculo das estatísticas básicas, como quantidade de sequências, menor tamanho, maior tamanho, comprimento médio e conteúdo GC.

```text
src/similarity.py
```

Responsável pelo cálculo simples de similaridade entre duas sequências. A comparação é feita posição por posição, sem alinhamento biológico real.

```text
src/taxonomy.py
```

Responsável pelo carregamento do banco local, cálculo do ranking das melhores correspondências e classificação final com base no limiar mínimo de similaridade.

```text
src/services/analysis_service.py
```

Responsável por orquestrar o fluxo completo de análise. Ele conecta leitura, validação, estatísticas, classificação e retorno dos resultados para a interface.

---

## Validação das sequências

Uma das principais melhorias desta versão foi a criação do arquivo:

```text
src/validation.py
```

Esse módulo verifica se as sequências contêm apenas bases válidas.

Por padrão, são aceitas:

```text
A, T, C, G, N
```

A base `N` representa uma base ambígua, comum em dados biológicos quando não é possível determinar com certeza qual base está naquela posição.

Também existe a opção de validação mais rígida, aceitando apenas:

```text
A, T, C, G
```

Sequências vazias ou com caracteres inválidos são separadas e não seguem para classificação.

Exemplo:

```text
ATCGATCG  → válida
ATCGNNTA  → válida se N estiver permitido
ATCGXBTA  → inválida
```

Essa validação evita que o sistema tente classificar sequências problemáticas e gere resultados pouco confiáveis.

---

## Limiar mínimo de similaridade

Antes, o sistema sempre retornava a espécie mais parecida, mesmo que a similaridade fosse baixa. Isso poderia gerar classificações incorretas.

Agora foi adicionado um parâmetro chamado:

```text
Limiar mínimo de similaridade (%)
```

Se a melhor correspondência estiver abaixo desse valor, o resultado será:

```text
Espécie não identificada
```

Exemplo:

```text
Limiar configurado: 95%
Melhor similaridade encontrada: 89%
Resultado: Espécie não identificada
```

Essa alteração melhora a confiabilidade da classificação, pois evita respostas forçadas.

---

## Ranking das melhores correspondências

Outra melhoria importante foi a criação de um ranking com as melhores correspondências.

Agora, para cada sequência válida, o BioTrace mostra as cinco espécies mais próximas, com suas respectivas similaridades.

Exemplo:

```text
Espécie                 Similaridade
Danio rerio             98.2%
Cyprinus carpio         95.4%
Oreochromis niloticus   94.8%
Astyanax altiparanae    92.1%
Salmo salar             90.3%
```

A espécie escolhida é destacada visualmente na interface, desde que tenha ultrapassado o limiar mínimo de similaridade.

---

## Banco de referência com múltiplas sequências

O banco local também foi melhorado.

Antes, havia apenas uma sequência por espécie. Agora, o banco permite várias sequências para a mesma espécie.

A nova estrutura é:

```csv
species,id,sequence
Danio rerio,DRE001,ATCGATCGATCGATCG
Danio rerio,DRE002,ATCGATCGATCGATTG
Danio rerio,DRE003,ATCGATCGTTCGATCG
```

Cada linha representa uma sequência de referência.

As colunas obrigatórias são:

* `species`: nome da espécie;
* `id`: identificador da sequência de referência;
* `sequence`: sequência de DNA usada na comparação.

A classificação considera todas as sequências disponíveis no banco. Para o ranking final, cada espécie aparece apenas uma vez, representada pela melhor sequência de referência daquela espécie.

---

## Camada de serviço

Uma decisão arquitetural importante foi criar uma camada de serviço:

```text
src/services/analysis_service.py
```

Antes, a interface Streamlit concentrava muita lógica de análise. Isso poderia deixar o arquivo `main.py` confuso e difícil de manter.

Com a camada de serviço, o fluxo principal passou a ser organizado assim:

```text
main.py
  ↓
analysis_service.py
  ↓
fasta.py
validation.py
stats.py
taxonomy.py
similarity.py
```

O `analysis_service.py` é responsável por coordenar as etapas:

1. ler o arquivo FASTA;
2. validar as sequências;
3. calcular estatísticas;
4. carregar o banco local;
5. classificar as sequências;
6. montar os resultados finais.

Assim, o `main.py` fica mais focado na interface, e as regras de negócio ficam centralizadas no serviço.

---

## Melhorias na interface

A interface Streamlit também recebeu melhorias importantes:

* título e textos atualizados para BioTrace;
* barra lateral com parâmetros da análise;
* controle do limiar mínimo de similaridade;
* opção para permitir ou não a base `N`;
* barra de progresso durante a análise;
* mensagens de erro para sequências inválidas;
* mensagens de sucesso ao concluir a análise;
* indicadores de sequências recebidas, analisadas e inválidas;
* tabela com resultados de classificação;
* ranking das cinco melhores correspondências;
* gráfico de espécies identificadas;
* exportação dos resultados em CSV.

Essas melhorias deixam o uso do sistema mais claro para o usuário.

---

## Responsabilidade de cada módulo

A principal ideia de organização usada nesta versão foi a responsabilidade única.

Cada parte do sistema deve fazer apenas uma coisa principal:

```text
fasta.py
Lê arquivos FASTA.

validation.py
Valida as sequências.

stats.py
Calcula estatísticas.

similarity.py
Compara sequências.

taxonomy.py
Classifica usando o banco local.

analysis_service.py
Organiza o fluxo completo.

main.py
Exibe a interface para o usuário.
```

Essa divisão melhora a manutenção, facilita testes futuros e torna o projeto mais fácil de evoluir.

---

## Limitações atuais

Mesmo com as melhorias, o BioTrace v0.2.0 ainda possui limitações importantes:

* não usa BLAST;
* não usa Kraken2;
* não usa QIIME2;
* não usa DADA2;
* não usa bancos online;
* não processa arquivos FASTQ;
* não realiza alinhamento biológico real;
* a similaridade ainda é calculada de forma simples, por posição.

Essas limitações são intencionais nesta fase, pois o objetivo é evoluir o projeto de forma incremental.

---

## Próximo MVP recomendado

O próximo MVP sugerido é o BioTrace v0.3.0, com foco em qualidade e confiabilidade.

As próximas melhorias recomendadas são:

* criar testes automatizados;
* testar a validação de sequências;
* testar o limiar mínimo de similaridade;
* testar o ranking de correspondências;
* validar a estrutura do banco de referência;
* detectar IDs duplicados no banco local;
* exportar também o ranking completo em CSV;
* melhorar o tratamento de empates entre espécies;
* adicionar documentação de contribuição.

Antes de adicionar ferramentas mais complexas, como FASTQ, BLAST ou bancos externos, é importante fortalecer a base atual do projeto.

---

## Conclusão

O MVP v0.2.0 tornou o BioTrace mais organizado, confiável e preparado para evoluções futuras.

As principais melhorias foram a validação das sequências, o uso de limiar mínimo de similaridade, o ranking das melhores correspondências, a nova estrutura do banco local e a separação da regra de negócio em uma camada de serviço.

A arquitetura continua simples, mas agora está mais próxima de um projeto real de software científico em desenvolvimento.
