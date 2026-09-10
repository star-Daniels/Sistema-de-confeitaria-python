
from MODELOS.venda import Venda
from MODELOS.item_venda import ItemVenda
from COZINHA.cozinha import quantidade_bolos_possiveis, retirar_ingredientes


def listar_bolos(bolos):

    print("\nBolos disponíveis\n")

    for bolo in bolos:

        quantidade = quantidade_bolos_possiveis(bolo)

        print(
            f"{bolo.nome} : R${bolo.preco:.2f} | "
            f"qtd: {quantidade}\n"
            "_________________\n"
        )


def definir_quantidade(bolo):

    quantidade_disponivel = quantidade_bolos_possiveis(bolo)

    if quantidade_disponivel == 0:

        print("Ingredientes insuficientes.")
        return None

    quantidade = int(input("\nDigite a quantidade: "))

    if quantidade <= 0:

        print("A quantidade deve ser maior que zero.")
        return None

    if quantidade > quantidade_disponivel:

        print(
            f"Quantidade insuficiente. "
            f"Disponível: {quantidade_disponivel}"
        )

        return None

    return quantidade


def selecionar_bolo(bolos):

    listar_bolos(bolos)

    nome_bolo = input("\nDigite o nome do bolo: ")

    for bolo in bolos:

        if bolo.nome == nome_bolo:

            quantidade = definir_quantidade(bolo)

            if quantidade is None:
                return None

            return bolo, quantidade

    return None


def quantidade_na_venda(itens_venda, bolo):

    quantidade = 0

    for item in itens_venda:

        if item.bolo.nome == bolo.nome:
            quantidade += item.quantidade

    return quantidade


def calcular_total(bolo, quantidade):

    return bolo.preco * quantidade


def realizar_venda(bolos, vendas):

    itens_venda = []
    continuar = True

    while continuar:

        resultado = selecionar_bolo(bolos)

        if resultado:

            bolo_escolhido, quantidade_venda = resultado

            quantidade_existente = quantidade_na_venda(
                itens_venda,
                bolo_escolhido
            )

            quantidade_total = (
                quantidade_existente + quantidade_venda
            )

            if quantidade_total > quantidade_bolos_possiveis(bolo_escolhido):

                print("\nQuantidade insuficiente para esta venda.")
                continue

            total = calcular_total(
                bolo_escolhido,
                quantidade_venda
            )

            item = ItemVenda(
                bolo_escolhido,
                quantidade_venda,
                total
            )

            itens_venda.append(item)

            print("\nBolo adicionado à venda!")

            adicionar = input(
                "\nDeseja adicionar outro bolo? S/N: "
            ).strip().upper()

            if adicionar == "N":
                continuar = False

        else:

            print("\nVenda não realizada.")

            tentar_novamente = input(
                "\nDeseja tentar novamente? S/N: "
            ).strip().upper()

            if tentar_novamente == "N":
                return

    print("\n===== RESUMO DA VENDA =====")

    total_venda = 0

    for item in itens_venda:

        print(
            f"{item.bolo.nome} | "
            f"Quantidade: {item.quantidade} | "
            f"Total: R${item.total:.2f}"
        )

        total_venda += item.total

    print("---------------------------")
    print(f"TOTAL: R${total_venda:.2f}")

    confirmacao = input(
        "\nDeseja confirmar a venda? S/N: "
    ).strip().upper()

    if confirmacao == "S":

        for item in itens_venda:

            retirar_ingredientes(
                item.bolo,
                item.quantidade
            )

        venda = Venda(
            itens_venda,
            total_venda
        )

        vendas.append(venda)

        print("\nVenda feita!")

    else:

        print("\nVenda cancelada.")


def menu_caixa(bolos, vendas):

    escolha = 1

    while escolha != 0:

        print("\n\n========== CAIXA ==========")
        print("1 - Realizar nova venda")
        print("0 - Sair")

        escolha = int(input("\nEscolha uma opção: "))

        if escolha == 1:

            realizar_venda(bolos, vendas)

        elif escolha == 0:

            print("Saindo\n\n")

