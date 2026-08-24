class Item:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def __str__(self):
        return f"Nome:{self.nome} & Quantidade:{self.quantidade}"
estoque = []

def add_item():
    print(f"Qual item deseja adcionar ao estoque?")
    nome = input ("Nome:")
    quantidade = int(input("Quantidade:"))
    novo_item = Item(nome, quantidade)
    estoque.append(novo_item)

def remover_item():
    rem_item = input("Qual item deseja retirar do estoque?")
    for item in estoque:
        if item.nome == rem_item:
            estoque.remove(item)
            return
    print("Item nao encontrado")

def listar_estoque():
    if not estoque:
        print("Estoque Vazio")
        return
    for item in estoque:
        print(item)

if __name__ == "__main__":
    while True:
        opcao = input(" 1-Abrir Estoque\n 2-Adcionar item\n 3-Remover Item\n 4-Sair\n")
        match opcao: 
            case "1":
                print("Abrindo Estoque")   
                listar_estoque()
                print("Fechando Estoque")
            case "2":
                add_item()

            case "3":
                remover_item()

            case "4":
                print("Saindo...")
                break

            case _:
                print("Opcao invalida")

