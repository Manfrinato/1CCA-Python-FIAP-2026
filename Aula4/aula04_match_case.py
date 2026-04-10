#imagina um programa... que recebe a escolha do usuario
#escolha-usuario
#0--->sair do programa
#1---> entrar no programa
#--->Erro

escolha_usuario = 0
match escolha_usuario:
    case 0:
        print("Sair do programa")
    case 1:
        print("entrar no programa")
    case 2:
        print("ERRO")