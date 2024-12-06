
#crio laço while para manter o programa em execucao - dentro do loop devo ter algo que pare o programa, no caso,
#a entrada do digito 9 pelo usuario

while True:
    #Impressao do menu de opcoes:
    print("\nMenu de Opções:")
    print("1 - Incluir usuário")
    print("2 - Excluir usuário")
    print("3 - Consultar usuário")
    print("4 - Alterar usuário")
    print("5 - Listar todos os usuários cadastrados")
    print("9 - Sair")

    #Solicito que o usuario digite a opcao desejada:
    x = int(input("Digite o número correspondente à opcao desejada: "))

    #impressao da opcao escolhida de acordo com o menu
    if x == 1:
        print("Opção 1: Incluir usuário")
    elif x == 2:
        print("Opção 2: Excluir usuário")
    elif x == 3:
        print("Opção 3: Consultar usuário")
    elif x == 4:
        print("Opção 4: Alterar usuário")
    elif x == 5:
        print("Opção 5: Listar todos os usuários cadastrados")
    elif x == 9:
        print("Saindo do programa...")
        break  #Encerra o loop - TEM QUE TER para que o programa nao entre em loop infinito
    else:
        print("Opção inválida! Tente novamente.")

        

