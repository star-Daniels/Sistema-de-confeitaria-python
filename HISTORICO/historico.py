from ESTRUTURAS.pilha import Pilha
from ESTRUTURAS.merge_sort import merge_sort
from MODELOS.venda import Venda

vendas_organizadas = False


pilha_vendas = Pilha()


def listar_vendas(vendas):

    pilha_vendas.itens = []

    for venda in vendas:
        pilha_vendas.empilhar(venda)

    if pilha_vendas.vazia():
        print("\n\nNenhuma venda registrada.\n\n")
        return

    id = 0
    vendas_temporarias = []

    while not pilha_vendas.vazia():
        venda = pilha_vendas.desempilhar()

        print(f"\n\n========== VENDA | {len(vendas) - id}\n")

        for item in venda.itens:
            print(
                f"{item.bolo.nome} - "
                f"{item.quantidade} | "
                f"R$ {item.total}\n"
                "___________________\n"
            )

        vendas_temporarias.append(venda)
        id += 1

    for venda in vendas_temporarias:
        pilha_vendas.empilhar(venda)


def listar_vendas_por_valor(vendas):
    
    global vendas_organizadas, vendas_ordenadas 
     
    if not vendas_organizadas:
     vendas_ordenadas = merge_sort(vendas.copy())
     vendas_organizadas = True

    id = 1

    for venda in vendas_ordenadas:
        print(f"{id} - R$ {venda.total_venda:.2f}")
        id += 1
        
        
        
    
        
def calcular_faturamento(vendas):
    total_vendas=0
    for venda in vendas:
        for item in venda.itens:
          total_vendas += item.total  
        
    print(f"\nValor total : {total_vendas} \n")

def qtd_bolos_vendidos(vendas):

    total_bolos_vendidos = 0

    for venda in vendas:
        for item in venda.itens:
            
            total_bolos_vendidos += item.quantidade
    print(f"Quantidade total de bolos vendidos : {total_bolos_vendidos} \n")

def menu_historico(vendas):
    escolha =1
    while escolha != 0:
        
        print("\n\n========== HISTORICO ==========")
        print("1 - Listar Vendas")
        print("2 - Calcular Faturamento")
        print("3 - Total de bolos vendidos")
        print("4 - listar Vendas por valor")
        print("0 - Sair\n\n")
        
        escolha = int(input("\nEscolha uma opção: "))
        
        if escolha == 1:
            listar_vendas(vendas)

        elif escolha == 2:
            calcular_faturamento(vendas)
            
        elif escolha == 3:
            qtd_bolos_vendidos(vendas)
        elif escolha == 4:
            listar_vendas_por_valor(vendas)
        elif escolha == 0:
            print("\nSaindo\n\n")
