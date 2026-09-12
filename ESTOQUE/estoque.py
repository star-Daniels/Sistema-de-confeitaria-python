from MODELOS.item import Item
estoque = []

def add_item():
    print(f"\n\nQual item deseja adcionar ao estoque?")
    nome = input ("Nome:")
    quantidade = int(input("Quantidade:"))
    novo_item = Item(nome, quantidade)
    estoque.append(novo_item)

def remover_item():
    rem_item = input("\n\nQual item deseja retirar do estoque?")
    for item in estoque:
        if item.nome == rem_item:
            estoque.remove(item)
            return
    print("\n\nItem nao encontrado\n\n")

def listar_estoque():
    if not estoque:
        print("Estoque Vazio")
        return
    for item in estoque:
        print(item)

def menu_estoque():
    while True:
        opcao = input(" \n\n1-Listar Estoque\n 2-Adcionar item\n 3-Remover Item\n 4-Sair\n")
        match opcao: 
            case "1":
                print("\nAbrindo Estoque\n")   
                listar_estoque()
                print("\nFechando Estoque\n")
            case "2":
                add_item()

            case "3":
                remover_item()

            case "4":
                print("\n\nSaindo...\n\n")
                break

            case _:
                print("\n\nOpcao invalida\n\n")

