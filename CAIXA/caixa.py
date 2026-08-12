from MODELOS.venda import Venda


def listar_bolos(bolos):
    print("\nBolos disponíveis\n")

    for bolo in bolos:
        print(
            f"{bolo.id} - {bolo.nome} : R${bolo.preco} | "
            f"qtd: {bolo.estoque}\n"
            "_________\n"
        )


def definir_quantidade(bolo):
    quantidade = int(input("\nDigite a quantidade: "))

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return None

    if quantidade > bolo.estoque:
        print(
            f"Estoque insuficiente. "
            f"Disponível: {bolo.estoque}"
        )
        return None

    return quantidade


def selecionar_bolo(bolos):
    listar_bolos(bolos)

    id_bolo = int(input("\nDigite o número do bolo: "))

    for bolo in bolos:
        if bolo.id == id_bolo:
            quantidade = definir_quantidade(bolo)

            if quantidade is None:
                return None

            return bolo, quantidade

    return None


def calcular_total(bolo, quantidade):
    return bolo.preco * quantidade


def realizar_venda(bolos, vendas):
    realizar_venda = True

    while realizar_venda:

        resultado = selecionar_bolo(bolos)

        if resultado:
            bolo_escolhido, quantidade_venda = resultado

            total = calcular_total(
                bolo_escolhido,
                quantidade_venda
            )

            print("\n===== RESUMO =====")
            print(f"Bolo: {bolo_escolhido.nome}")
            print(f"Quantidade: {quantidade_venda}")
            print(f"Total: R${total:.2f}")

            confirmacao = input(
                "\nDeseja confirmar a venda? S/N: "
            ).strip().upper()

            if confirmacao == "S":

                bolo_escolhido.estoque -= quantidade_venda

                venda = Venda(
                    bolo_escolhido,
                    quantidade_venda,
                    total
                )

                vendas.append(venda)

                print("\nVenda feita!")
                print(
                    f"Estoque restante: "
                    f"{bolo_escolhido.estoque}"
                )

            else:
                print("\nVenda cancelada.")

        else:
            print("\nVenda não realizada.")

        nova_venda = input(
            "\nRealizar nova venda? S/N: "
        ).strip().upper()

        if nova_venda == "N":
            realizar_venda = False