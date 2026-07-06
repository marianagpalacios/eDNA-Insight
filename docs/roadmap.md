# Roadmap do BioTrace

## MVP v0.1.0

- Leitura de arquivos FASTA.
- Cálculo de estatísticas básicas.
- Banco CSV local.
- Similaridade simples.
- Interface Streamlit.
- Tabela, gráfico e exportação CSV.

## MVP v0.2.0

- Renomeação completa para BioTrace.
- Validação de sequências.
- Limiar mínimo de similaridade.
- Ranking das cinco melhores correspondências.
- Banco local com múltiplas sequências por espécie.
- Melhorias na interface.
- Camada de serviço para separar regra de negócio da interface.
- Documentação atualizada.

## Próximo MVP sugerido: v0.3.0

Foco: qualidade e confiabilidade.

- Criar testes automatizados.
- Testar validação de sequências.
- Testar classificação com limiar mínimo.
- Testar ranking de correspondências.
- Validar estrutura do banco de referência.
- Detectar IDs duplicados no banco local.
- Exportar ranking completo em CSV.
- Melhorar tratamento de empates.

## Versões futuras

- Suporte a FASTQ.
- Estatísticas de qualidade.
- Índices de biodiversidade.
- Relatórios em PDF.
- Docker.
- GitHub Actions.
- Integrações futuras com ferramentas consolidadas, como BLAST ou Kraken2.
