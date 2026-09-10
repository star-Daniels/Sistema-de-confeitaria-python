from LOGIN.login import cadastrar_user, realizar_login
from COZINHA.cozinha import menu_cozinha, lista_bolo
from ESTOQUE.estoque import listar_estoque
from CAIXA.caixa import menu_caixa
from HISTORICO.historico import menu_historico


usuarios = []
vendas = []


def menu_principal(usuario):

    escolha = 1

    while escolha != 0:

        print("\n========== MENU PRINCIPAL ==========")
        print(f"Usuário: {usuario.nome}")
        print(f"Tipo: {usuario.tipo}\n")

        if usuario.tipo == "ADM":

            print("1 - Cozinha")
            print("2 - Estoque")
            print("3 - Caixa")
            print("4 - Histórico")
            print("0 - Sair")

        else:

            print("1 - Caixa")
            print("2 - Histórico")
            print("0 - Sair")

        escolha = int(input("\nEscolha uma opção: "))

        if usuario.tipo == "ADM":

            if escolha == 1:

                menu_cozinha()

            elif escolha == 2:

                listar_estoque()

            elif escolha == 3:

                menu_caixa(lista_bolo, vendas)

            elif escolha == 4:

                menu_historico(vendas)

            elif escolha == 0:

                print("\nSaindo do sistema...")

            else:

                print("\nOpção inválida.")

        else:

            if escolha == 1:

                menu_caixa(lista_bolo, vendas)

            elif escolha == 2:

                menu_historico(vendas)

            elif escolha == 0:

                print("\nSaindo do sistema...")

            else:

                print("\nOpção inválida.")


def menu_login():

    escolha = 1

    while escolha != 0:

        print("\n========== SISTEMA DE CONFEITARIA ==========")
        print("1 - Entrar")
        print("2 - Cadastrar usuário")
        print("0 - Sair")

        escolha = int(input("\nEscolha uma opção: "))

        if escolha == 1:

            usuario = realizar_login(usuarios)

            if usuario:

                menu_principal(usuario)

        elif escolha == 2:

            cadastrar_user(usuarios)

        elif escolha == 0:

            print("\nSistema encerrado.")

        else:

            print("\nOpção inválida.")


menu_login()

