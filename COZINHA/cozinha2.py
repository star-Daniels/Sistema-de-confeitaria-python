from ESTOQUE.estoque import Item
from ESTOQUE.estoque import add_item
from ESTOQUE.estoque import remover_item 

class Bolo:
    def __init__(self, nome, preco, ingredientes):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes

    def __str__(self):
        return f"{self.nome} preco: {self.preco} ingredientes: {', '.join(self.ingredientes)}"

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
        lista_ing.append(Item(ing_nome, lista_ing))

    novo_bolo = Bolo(nome, preco, ingredientes)
    lista_bolo.append(novo_bolo)

def remover_bolo():
    rem_bolo = input("Qual bolo deseja remover:")
    for bolo in lista_bolo:
        if bolo.nome == rem_bolo:
            lista_bolo.remove(bolo)
            print("Bolo removido")
            return
    print("Bolo nao encontrado")

opcao = input(" 1-Adicionar Bolo\n 2-Remover Bolo")
match opcao:
    case "1":
        add_bolo()
    case "2":
        remover_bolo()