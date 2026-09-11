"""
Exercício 1 - Analisar Despesas por Categoria e Ano

Objetivo:
Solicitar ao usuário uma categoria de despesa e um ano, verificar se existem
registros para essa combinação e exibir o total de despesas. O processo se
repete até que o usuário digite "sair".
"""

import pandas as pd

df = pd.read_csv("dados_despesa.csv")


def buscar_total_despesa(categoria, ano):
    """Filtra o DataFrame por categoria e ano e retorna o total gasto.

    Retorna None se não houver registros para a combinação informada.
    """
    filtro = df[
        (df["despesa"].str.lower() == categoria.lower())
        & (df["ano"] == ano)
    ]

    if filtro.empty:
        return None

    return filtro["valor_despesa"].sum()


def main():
    while True:
        categoria = input(
            "Digite o tipo de despesa que deseja filtrar (ou 'sair' para encerrar): "
        ).strip()

        if categoria.lower() == "sair":
            print("Programa encerrado.")
            break

        ano_input = input("Digite o ano que deseja filtrar (ex.: 2023): ").strip()

        if not ano_input.isdigit():
            print("Ano inválido. Digite apenas números (ex.: 2023).\n")
            continue

        ano = int(ano_input)
        total = buscar_total_despesa(categoria, ano)

        if total is None:
            print(f"Não foram encontradas despesas para '{categoria}' no ano {ano}.\n")
        else:
            print(f"Total de despesas para '{categoria}' no ano {ano}: R$ {total:.2f}\n")


if __name__ == "__main__":
    main()