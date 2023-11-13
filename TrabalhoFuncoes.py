
def boas_vindas():
    print("     Bem vindo aventureiro!      \n")

def menu():
    print("     Menu interdimensional       \n\n"
          "1.Embarcar em uma Nova Missão\n"
            "2.Explorar o último desafio\n"
            "3.Abandonar a Convenção (Sair)\n")

def jogo():
    def comeco():
        print("\n"
          "O número secreto escolhido pelo computador está entre 1 e 100.\n"
          "E é um numero inteiro\n"
          "Use sua astúcia para advinhar o número entre as estrelas\n")

    def numero_aleatorio():
        import random
        return random.randrange(1, 101)
    
    def pede_chute():
        chute = int(input("Digite seu chute: "))
        while chute > 100 or chute < 1:
            chute = input("Entrada Inválida - Digite um numero inteiro entre 1 e 100: ")
        return chute
    
    def vitoria(aux):
        print("\nParabéns! Você acertou!\nO numero de tentativas para acertar o numero foi:{:d}\n".format(aux))
    
    numero_secreto = numero_aleatorio()
    acertou = False
    tentativa = 0
    comeco()
    while not acertou:
        tentativa += 1
        chute = pede_chute()
        if chute > numero_secreto:
            print("O número secreto é menor do que o seu chute! Tente novamente.\n")

        elif chute < numero_secreto:
            print("O número secreto é maior que o seu chute! Tente novamente.\n")
        else:
            vitoria(tentativa)
            acertou = True
    return tentativa


def registro(jogo_iniciado,nome_salvo,tentativa_salva):
    if(jogo_iniciado == 0):
      print("\nNenhum aventureiro foi corajoso o bastante ainda para encarar esse desafio\n"
            "Não há registros de aventuras anteriores para mostrar aqui\n")
    else:
      print("O ultimo aventureiro que venceu esse desafio foi:\n")
      print("Nome do Aventureiro: {:s}    Numero de vezes que tentou adivinhar: {:d}\n".format(nome_salvo, tentativa_salva))

def saudacoes():
    print("Você é novo por aqui\n")
    nome = input("Por favor diga seu nome, bravo aventureiro:\n")
    return nome
