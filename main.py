from MODELOS.bolo import Bolo
from MODELOS.usuario import Usuario
from MODELOS.venda import Venda 
from CAIXA.caixa import menu_caixa
from HISTORICO.historico import menu_historico
from LOGIN.login import cadastrar_user, realizar_login


usuarios = []
usuarios.append(Usuario("Daniel", "daniel", "123", "ADM"))

bolos = [
    Bolo(1, "Bolo de Café", 25.00, 3),
    Bolo(2, "Bolo de Chocolate", 30.00, 5),
    Bolo(3, "Bolo de Morango", 35.00, 2)
]
vendas=[]



usuario_logado = realizar_login(usuarios)



    
if usuario_logado!= False:
    if usuario_logado.tipo == "ADM":
        
        while True:
            print("\n\n========== SISTEMA DE CONFEITARIA ==========")
            print("1 - Cozinha")
            print("2 - Estoque")
            print("3 - Caixa")
            print("4 - Histórico")
            print("5 - Cadastrar funcionario")
            print("0 - Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                print("cozinha")
            elif opcao == "2":
                print("estoque")

            elif opcao == "3":
                menu_caixa(bolos, vendas)

            elif opcao == "4":
                menu_historico(vendas)
            elif opcao == "5":
                cadastrar_user(usuarios)

            elif opcao == "0":
                print("\nSistema encerrado.")
                break
                

            else:
                print("\nOpção inválida.")
    else:
        while True:
                print("\n\n========== SISTEMA DE CONFEITARIA ==========")
                print("1 - Cozinha")
                print("2 - Estoque")
                print("3 - Caixa")
                print("4 - Histórico")
                print("0 - Sair")
        
                opcao = input("\nEscolha uma opção: ")
        
                if opcao == "1":
                       print("cozinha")
                elif opcao == "2":
                    print("estoque")
        
                elif opcao == "3":
                    menu_caixa(bolos, vendas)
        
                elif opcao == "4":
                    menu_historico(vendas)
        
                elif opcao == "0":
                    print("\nSistema encerrado.")
                    break
                        
        
                else:
                    print("\nOpção inválida.")
        
                