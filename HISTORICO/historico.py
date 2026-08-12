def listar_vendas(vendas):
    for venda in vendas:
        print(f"{venda.bolo.nome} - {venda.quantidade} | {venda.total}\n")
        
def calcular_faturamento(vendas):
    total_vendas=0
    for venda in vendas:
        total_vendas += venda.total
    return total_vendas

def qtd_bolos_vendidos(vendas):
    total_bolos_vendidos=0
    for venda in vendas:
        total_bolos_vendidos += venda.quantidade
    return total_bolos_vendidos

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
            listar_vendas()
        elif escolha ==2:
            calcular_faturamento()
            
        elif escolha == 3:
            qtd_bolos_vendidos()
        elif escolha == 0:
            print("Saindo\n\n")
           