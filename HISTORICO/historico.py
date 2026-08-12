def listar_vendas(vendas):
    for venda in vendas:
        print(f"{venda.bolo.nome} - {venda.quantidade} | {venda.total}\n")
        
def calcular_faturamento(vendas):
    total_vendas=0
    for venda in vendas:
        total_vendas += venda.total
    print(f"Valor total : {total_vendas} \n")

def qtd_bolos_vendidos(vendas):
    total_bolos_vendidos=0
    for venda in vendas:
        total_bolos_vendidos += venda.quantidade
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
           