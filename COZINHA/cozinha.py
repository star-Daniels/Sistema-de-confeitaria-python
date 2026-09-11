from MODELOS.bolo import Bolo
from MODELOS.item import Item
from ESTOQUE.estoque import estoque

from ESTRUTURAS.fila_prioridade import FilaPrioridade


fila_producao = FilaPrioridade()
lista_bolo = []


def adicionar_fila():
    bolo = buscar_bolo()

    if not bolo:
        print("Bolo não encontrado\n\n")
        return

    prioridade = int(input("Digite a prioridade (1 a 5): "))

    if prioridade < 1 or prioridade > 5:
        print("Prioridade inválida\n\n")
        return

    fila_producao.adicionar(bolo, prioridade)

    print(f"{bolo.nome} adicionado à fila!\n\n")


def ver_fila():
    if fila_producao.vazia():
        print("\nFila de produção vazia.\n\n")
        return

    print("\n===== FILA DE PRODUÇÃO =====")

    for prioridade, bolo in fila_producao.itens:
        print(
            f"Bolo: {bolo.nome} | "
            f"Prioridade: {prioridade}"
        )


def add_bolo():
    nome = input("Nome:")

    preco = float(input("Preco:"))

    lista_ing = []

    while True:
        ing_nome = input("Ingrediente:")

        if ing_nome == "":
            break

        ing_qtd = float(
            input(f"Quantidade de {ing_nome}:")
        )

        lista_ing.append(
            Item(ing_nome, ing_qtd)
        )
        
    id = len(lista_bolo) + 1

    novo_bolo = Bolo(
        id,
        nome,
        preco,
        lista_ing
        
    )

    lista_bolo.append(novo_bolo)


def remover_bolo():
    rem_bolo = input(
        "Qual bolo deseja remover:"
    )

    for bolo in lista_bolo:

        if bolo.nome == rem_bolo:

            lista_bolo.remove(bolo)

            print("Bolo removido\n\n")

            return

    print("Bolo nao encontrado\n\n")


def listar_bolos():

    if not lista_bolo:

        print("Lista vazia\n\n")

        return

    for bolo in lista_bolo:

        print(bolo.nome)


def buscar_bolo():

    nome = input(
        "Pesquisar bolo:"
    )

    for bolo in lista_bolo:

        if bolo.nome == nome:

            return bolo

    return None


def buscar_item(nome):

    for item in estoque:

        if item.nome == nome:

            return item

    return None


def quantidade_bolos_possiveis(bolo):

    quantidades = []

    for ingrediente in bolo.ingredientes:

        item = buscar_item(ingrediente.nome)

        if item is None:

            return 0

        quantidade = (
            item.quantidade // ingrediente.quantidade
        )

        quantidades.append(quantidade)

    if not quantidades:

        return 0

    menor = quantidades[0]

    for quantidade in quantidades:

        if quantidade < menor:

            menor = quantidade

    return int(menor)

def adicionar_ingrediente(bolo):

    nome = input("Nome do ingrediente: ")

    quantidade = float(
        input("Quantidade: ")
    )

    novo_item = Item(nome, quantidade)

    bolo.ingredientes.append(novo_item)

    print("Ingrediente adicionado!")


def retirar_ingredientes(bolo, quantidade): 

    for ingrediente in bolo.ingredientes:

        item = buscar_item(ingrediente.nome)

        if item is not None:

            item.quantidade -= (
                ingrediente.quantidade * quantidade
                
    
            )
            
def remover_ingrediente(bolo):
    nome = input("Nome do ingrediente: ")

    for ingrediente in bolo.ingredientes:
        if ingrediente.nome == nome:
            bolo.ingredientes.remove(ingrediente)
            print("Ingrediente removido!\n\n")
            return

    print("Ingrediente não encontrado!\n\n")


def menu_cozinha():
    opcao = ""
    
    while opcao != "8":
    
    
        opcao = input(
            "\n\n1-Listar Bolos\n"
            "2-Adicionar Bolo\n"
            "3-Remover Bolo\n"
            "4-Editar Bolo\n"
            "5-Adicionar à fila de produção\n"
            "6-Ver fila de produção\n"
            "7-Produzir próximo bolo\n"
            "8-Sair\n\n"
        )

        match opcao:

            case "1":
                listar_bolos()

            case "2":
                add_bolo()

            case "3":
                remover_bolo()

            case "4":

                bolo = buscar_bolo()

                if not bolo:

                    print("Bolo nao Encontrado")

                else:

                    sub_opcao = input(
                        "\n\n1-Ver lista de Ingredientes\n"
                        "2-Adicionar Ingredientes\n"
                        "3-Remover Ingredientes\n"
                        "4-Sair\n\n"
                    )

                    match sub_opcao:

                        case "1":
                            for ingrediente in bolo.ingredientes:
                                print(
                                    f"Ingrediente: {ingrediente.nome} | "
                                    f"Quantidade: {ingrediente.quantidade}"
                                )

                        case "2":
                            adicionar_ingrediente(bolo)

                        case "3":
                            remover_ingrediente(bolo)

                        case "4":
                            print("Saindo...\n\n")

                        case _:
                            print("Opcao Invalida\n\n")

            case "5":
                adicionar_fila()

            case "6":
                ver_fila()

            case "7":

                if fila_producao.vazia():

                    print("\nNão há bolos na fila.\n\n")

                else:

                    prioridade, bolo = fila_producao.remover()

                    print(
                        f"\nProduzindo: {bolo.nome} "
                        f"(Prioridade: {prioridade})"
                    )

                    quantidade = quantidade_bolos_possiveis(bolo)

                    if quantidade == 0:

                        print(
                            "\nNão há ingredientes suficientes "
                            "para produzir esse bolo.\n\n"
                        )

                    else:

                        retirar_ingredientes(
                            bolo,
                            quantidade
                        )

                        print(
                            f"\n{quantidade} bolo(s) produzido(s)!\n\n"
                        )

            case "8":
                print("Saindo...\n\n")

            case _:
                print("Opcao Invalida")