from MODELOS.usuario import Usuario


def cadastrar_user(usuarios):
    print("\n====Cadastro====\n\n")
    
    print("Coloque os dados")
    
    nome = input("Nome : ")
    user = input("Usuario : ").strip()
    senha = input("Senha : ").strip()
    
    escolha = 0 
    while escolha != 1 and escolha != 2:
        
        print("\nTipo de usuário\n")
        print("1 - Administrador\n")
        print("2 - Funcionário\n")
        
        escolha = int(input("Escolha: "))
        
        if escolha == 1:
            tipo = "ADM"
        elif escolha == 2:
            tipo = "FUNC"
        else:
            print("\nEscolha uma opcao valida\n\n")
    
    novo_user = Usuario(nome, user, senha, tipo)
    
    usuarios.append(novo_user)
    print(f"\nUsuário {nome} cadastrado com sucesso")
    
def buscar_usuario(usuarios, nome_usuario):
    for usuario in usuarios:
        if usuario.usuario == nome_usuario:
            return usuario

    return None



def realizar_login(usuarios):

    print("\n========== LOGIN ==========\n\n")

    continuar = True
    while continuar:
        
        
        nome_usuario = input("Usuário: ")
        senha = input("Senha: ")
        
        realizar = input("Deseja continuar [S/N]: ").strip().upper()
        if realizar == "N":
            continuar = False
            return False

        usuario_encontrado = buscar_usuario(usuarios,nome_usuario)

        if usuario_encontrado is None:
            print("\nUsuário não encontrado.")
        elif usuario_encontrado.senha != senha:
            print("\nSenha incorreta.")
        else:
            continuar = False
        

    print(
        f"\nLogin realizado com sucesso!"
        f"\nBem-vindo, {usuario_encontrado.nome}!"
    )

    return usuario_encontrado
    
    
    