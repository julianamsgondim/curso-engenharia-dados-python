# Curso de Engenharia de Dados - Python

Exercícios práticos do curso, organizados por módulo.

## Módulo 1

- **Exercício 1** — Análise de despesas por categoria e ano, usando pandas para filtrar e somar os dados de um CSV.
- **Exercício 2** — Sistema de controle de estoque usando dicionários (adicionar/remover itens).
- **Exercício 3** — Arquitetura de armazenamento de dados: lê o CSV de despesas, calcula os totais por categoria/ano e salva num banco SQLite, usando upsert para garantir que rodar o script várias vezes não duplica registros.

## Como rodar

1. Crie um ambiente virtual:

python -m venv venv

2. Ative o ambiente virtual (Windows):

venv\Scripts\activate

3. Instale as dependências:

pip install pandas

4. Rode o script desejado (de dentro da pasta `modulo-1`):

python nome_do_arquivo.py
