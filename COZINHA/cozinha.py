class Bolos:
    def __init__(self, nome, ingredientes):
        self.nome = nome
        self.ingredientes = ingredientes

    def __str__(self):
        return f"{self.nome} ingredientes: {', '.join(self.ingredientes)}"

    def adicionar_items(self):
        add_ing = input("Digite o item a ser adicionado:")
        if add_ing not in self.ingredientes:
            self.ingredientes.append(add_ing)
        else:
            print(f"'{add_ing}' ja esta na lista")

    def remover_items(self):
        rem_ing = input("Digite o item a ser retirado:")
        if rem_ing in self.ingredientes:
            self.ingredientes.remove(rem_ing)
        else:
            print("Ingrediente nao encontrado")

def adicionar_bolo():
    nome = input("Nome:")
    ingredientes = []
    novo_bolo = Bolos(nome, ingredientes)

    while True:
        novo_bolo.adicionar_items()
        continuar = input("Adcionar outro ingrediente?:").lower()
        if continuar != "sim":
            break

    lista_bolos.append(novo_bolo) 
    print(f"Bolo '{nome}' adcionado")

def remover_bolo():
    rem_bolo = input("Nome do Bolo:")
    for bolo in lista_bolos:
        if bolo.nome == rem_bolo:
            lista_bolos.remove(bolo)
            print(f"Bolo '{rem_bolo}' removido")
            break
    else:
        print(f"Bolo '{rem_bolo}' não encotrado ")

def listar_bolos():
    if not lista_bolos:
        print("Lista vazia")
        return
    for bolo in lista_bolos:
        print(bolo)

def buscar_bolo():
    nome = input("Pesquisar bolo:")
    for bolo in lista_bolos:
        if bolo.nome == nome:
            return bolo
    return None


lista_bolos = []

while True:
    opcao = int(input("Oque deseja fazer?\n 1-Listar Bolos\n 2-Adicionar Bolo\n 3-Remover Bolo\n 4-Editar Bolo\n 5-Sair\n"))
    match opcao:
        case 1:
            print("Listando Bolos")
            listar_bolos()
        case 2:
            adicionar_bolo()
        case 3:
            remover_bolo()
        case 4:
            bolo = buscar_bolo()
            if not bolo:
                print("Bolo não encontrado")
            else:
                sub_opcao = int(input("\n 1-Ver Lista de Ingredientes\n 2-Adicionar Ingredientes\n 3-Remover Ingredientes\n 4-Sair\n"))
                match sub_opcao:
                    case 1:
                        print(bolo.ingredientes)
                    case 2:
                        print(bolo.ingredientes)
                        bolo.adicionar_items()
                        print(bolo.ingredientes)
                    case 3:
                        print(bolo.ingredientes)
                        bolo.remover_items()
                        print(bolo.ingredientes)

                    case 4:
                        print("Saindo...")

                    case _:
                        print("Opção Invalida")

        case 5: 
            print("Saindo...")
            break
        case _:
            print("Opção invalida")