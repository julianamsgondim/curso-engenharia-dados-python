"""
Exercício 2 - Nível Ninja das Galáxias - Controle de Estoque

Objetivo:
Sistema simples de controle de estoque. O usuário pode adicionar um item
(com quantidade) ou remover um item (ajustando a quantidade), até decidir
encerrar digitando "sair".
"""

estoque = {}


def adicionar_item(nome, quantidade):
    nome = nome.strip().lower()
    estoque[nome] = estoque.get(nome, 0) + quantidade
    print(f"'{nome}' adicionado. Quantidade atual: {estoque[nome]}\n")


def remover_item(nome, quantidade):
    nome = nome.strip().lower()

    if nome not in estoque:
        print(f"O item '{nome}' não existe no estoque.\n")
        return

    if quantidade >= estoque[nome]:
        del estoque[nome]
        print(f"'{nome}' removido completamente do estoque.\n")
    else:
        estoque[nome] -= quantidade
        print(f"'{nome}' atualizado. Quantidade atual: {estoque[nome]}\n")


def exibir_estoque():
    if not estoque:
        print("Estoque vazio.\n")
        return

    print("Estoque atual:")
    for item, quantidade in estoque.items():
        print(f"  - {item}: {quantidade}")
    print()


def ler_quantidade():
    while True:
        valor = input("Digite a quantidade: ").strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print("Quantidade inválida. Digite um número inteiro maior que zero.")


def main():
    print("=== Controle de Estoque ===")
    print("Comandos disponíveis: adicionar | remover | estoque | sair\n")

    while True:
        comando = input("Digite um comando: ").strip().lower()

        if comando == "sair":
            print("Programa encerrado.")
            break

        elif comando == "adicionar":
            item = input("Digite o nome do item: ").strip()
            quantidade = ler_quantidade()
            adicionar_item(item, quantidade)

        elif comando == "remover":
            item = input("Digite o nome do item: ").strip()
            quantidade = ler_quantidade()
            remover_item(item, quantidade)

        elif comando == "estoque":
            exibir_estoque()

        else:
            print("Comando não reconhecido. Use: adicionar | remover | estoque | sair\n")


if __name__ == "__main__":
    main()