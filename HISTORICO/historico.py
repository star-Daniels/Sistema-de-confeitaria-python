def listar_vendas(vendas):
    id = 1
    for venda in vendas:
        
        print(f"==========VENDA | {id}\n")
        id += 1
        for item in venda.itens:
            print(f"{item.bolo.nome} - {item.quantidade} | R$ {item.total}\n_________\n")

def listar_vendas_por_valor(vendas):

    for i in range(len(vendas)):
        maior = i

        for j in range(i + 1, len(vendas)):

            if vendas[j].preco_total > vendas[maior].preco_total:
                maior = j

        vendas[i], vendas[maior] = vendas[maior], vendas[i]

    id = 1

    for venda in vendas:
        print(f"{id} - R$ {venda.preco_total:.2f}")
        id += 1
        
        
        
    
        
def calcular_faturamento(vendas):
    total_vendas=0
    for venda in vendas:
        for item in venda.itens:
          total_vendas += item.total  
        
    print(f"\nValor total : {total_vendas} \n")

def qtd_bolos_vendidos(vendas):
    total_bolos_vendidos=0
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
        print("0 - Sair")
        
        escolha = int(input("\nEscolha uma opção: "))
        
        if escolha == 1:
            listar_vendas(vendas)
        elif escolha ==2:
            calcular_faturamento(vendas)
            
        elif escolha == 3:
            qtd_bolos_vendidos(vendas)
        elif escolha == 0:
            print("Saindo\n\n")
           