"""
Exercício 3 - Criar uma arquitetura de armazenamento de dados

Objetivo:
As análises até aqui liam o CSV de origem diretamente. Este script cria uma
camada de armazenamento desacoplada (um banco SQLite) para guardar o
resultado das análises: o total de despesas por categoria e ano.

Requisitos atendidos:
1. Cria um banco de dados (SQLite) para armazenar os resultados das análises.
2. Lê o arquivo de origem (CSV), calcula as análises e salva na nova estrutura.
3. Código em um único arquivo .py.
4. Execuções repetidas não duplicam os dados (usa UNIQUE + "upsert").
"""

import sqlite3
import pandas as pd

CSV_ORIGEM = "dados_despesa.csv"
BANCO_DADOS = "despesas_analises.db"


def criar_banco():
    """Cria o banco de dados e a tabela de análises, se ainda não existirem."""
    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS despesas_por_categoria_ano (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT NOT NULL,
            ano INTEGER NOT NULL,
            total_despesa REAL NOT NULL,
            UNIQUE (categoria, ano)
        )
        """
    )

    conexao.commit()
    return conexao


def calcular_analise():
    """Lê o CSV de origem e calcula o total de despesas por categoria e ano."""
    df = pd.read_csv(CSV_ORIGEM)
    resultado = (
        df.groupby(["despesa", "ano"])["valor_despesa"]
        .sum()
        .reset_index()
        .rename(columns={"despesa": "categoria", "valor_despesa": "total_despesa"})
    )
    return resultado


def salvar_analise(conexao, df_resultado):
    """Salva o resultado no banco sem duplicar registros já existentes.

    Usa "INSERT ... ON CONFLICT ... DO UPDATE" (upsert): se a combinação
    categoria+ano já existir, o valor é atualizado em vez de duplicado.
    Isso garante que rodar o script várias vezes seja seguro (idempotente).
    """
    cursor = conexao.cursor()

    for _, linha in df_resultado.iterrows():
        cursor.execute(
            """
            INSERT INTO despesas_por_categoria_ano (categoria, ano, total_despesa)
            VALUES (?, ?, ?)
            ON CONFLICT (categoria, ano)
            DO UPDATE SET total_despesa = excluded.total_despesa
            """,
            (linha["categoria"], int(linha["ano"]), float(linha["total_despesa"])),
        )

    conexao.commit()


def exibir_resumo(conexao):
    """Mostra o conteúdo atual da tabela, só para conferência."""
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT categoria, ano, total_despesa FROM despesas_por_categoria_ano "
        "ORDER BY ano, categoria"
    )
    linhas = cursor.fetchall()

    print(f"\nTotal de registros na tabela: {len(linhas)}")
    print("Categoria     | Ano  | Total")
    print("-" * 35)
    for categoria, ano, total in linhas:
        print(f"{categoria:<13} | {ano} | R$ {total:.2f}")


def main():
    conexao = criar_banco()
    df_resultado = calcular_analise()
    salvar_analise(conexao, df_resultado)
    exibir_resumo(conexao)
    conexao.close()
    print(f"\nAnálise salva com sucesso em '{BANCO_DADOS}'.")


if __name__ == "__main__":
    main()