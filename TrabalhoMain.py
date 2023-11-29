import TrabalhoFuncoes as funcoes

jogo_iniciado = 0
nome_salvo = ""
tentativa_salva = 0
funcoes.boas_vindas()
while (True):
    funcoes.menu()
    opcao = int(input("Selecione a opção desejada: "))

    if 1 < opcao > 3:
        print("\nInfelizmente, essa dimensão não existe! Por favor, selecione uma opção existente.\n")
    elif opcao == 3:
        print("\nAdeus, Aventureiro!\nQue a força esteja com você!\n")
        break
    elif opcao == 1:
        jogo_iniciado = 1
        nome_salvo = funcoes.saudacoes()
        tentativa_salva = funcoes.jogo()
    elif opcao == 2:
        funcoes.registro(jogo_iniciado,nome_salvo,tentativa_salva)
