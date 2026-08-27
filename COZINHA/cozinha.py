from ESTOQUE.estoque import Item
from ESTOQUE.estoque import add_item
from ESTOQUE.estoque import remover_item

class Bolo:
    def __init__(self, nome, preco, ingredientes):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes

    def __str__(self):
        return f"{self.nome} preco: {self.preco} ingredientes: {', '.join(str(i) for i in self.ingredientes)}"

lista_bolo = []

def add_bolo():
    nome = input("Nome:")
    preco = float(input("Preco:"))

    lista_ing = []
    while True:
        ing_nome = input("Ingrediente:")
        if ing_nome =="":
            break
        ing_qtd = float(input(f"Quantidade de {ing_nome}:"))
        lista_ing.append(Item(ing_nome, ing_qtd))

    novo_bolo = Bolo(nome, preco, lista_ing)
    lista_bolo.append(novo_bolo)

def remover_bolo():
    rem_bolo = input("Qual bolo deseja remover:")
    for bolo in lista_bolo:
        if bolo.nome == rem_bolo:
            lista_bolo.remove(bolo)
            print("Bolo removido")
            return
    print("Bolo nao encontrado")

def listar_bolos():
    if not lista_bolo:
        print("Lista vazia")
        return
    for bolo in lista_bolo:
        print(bolo)

def buscar_bolo():
    nome = input("Pesquisar bolo:")
    for bolo in lista_bolo:
        if bolo.nome == nome:
            return bolo
    return None
def menu_cozinha() :
    opcao = input(" 1-Listar Bolos\n 2-Adicionar Bolo\n 3-Remover Bolo\n 4-Editar Bolo\n 5-Sair")
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
                sub_opcao = input(" 1-Ver lista de Ingredientes\n 2-Adicionar Ingredientes\n 3-Remover Ingredientes\n 4-Sair\n")
                match sub_opcao:
                    case "1":
                        print(bolo.ingredientes)
                    case "2":
                        add_item(bolo)
                    case "3":
                        remover_item(bolo)
                    case "4":
                        print("Saindo...")
                    case _:
                        print("Opcao Invalida")
        case "5":
            print("Saindo...")
        case _:
            print("Opcao Invalida")