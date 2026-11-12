from MODELOS.item import Item
from ESTRUTURAS.tabela_hash import TabelaHash

estoque = TabelaHash()

def add_item():
    print(f"\n\nQual item deseja adcionar ao estoque?")
    nome = input ("Nome:")
    quantidade = int(input("Quantidade:"))
    novo_item = Item(nome, quantidade)
    
    if estoque.inserir(novo_item):
        print("\nitem cadastrado\n")
    else:
        print("\nEsse item ja esta no estoque\n")
    

def remover_item():
    rem_item = input("\n\nQual item deseja retirar do estoque?")
    
    if estoque.remover(rem_item):
        print("Item removido!")
    else:
        print("Item não encontrado!")

def listar_estoque():
    itens = estoque.listar()

    if not itens:
        print("Estoque vazio!")
        return

    for item in itens:
        print(f"Nome: {item.nome} | Quantidade: {item.quantidade}")
        
def editar_item():
    item_escolhido = input("\nQual item deseja editar\n")
    item = estoque.buscar(item_escolhido)
    
    if item is None:
        print("Item não encontrado!")
        return
    
    nova_qtd  = int(input("Quantidade para adicionar: "))
     
    item.quantidade += nova_qtd
    print("Estoque atualizado!")
    
   


def menu_estoque():
    while True:
        opcao = input(
            " \n\n1-Listar Estoque\n"
            "2-Adcionar item\n"
            "3-Remover item\n"
            "4-Editar quantidade item\n"
            "0-Sair\n"
            )
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
                editar_item()

            case "0":
                print("\n\nSaindo...\n\n")
                break

            case _:
                print("\n\nOpcao invalida\n\n")

