entrada = input().split()

converter = [int(numero) for numero in entrada]

A, B = converter

if(A >= 12):
    duracao = (24 - A) + B
    print("O JOGO DUROU {0} HORA(S)".format(duracao))
elif(0 < A < 12):
    duracao = (B - A)
    print("O JOGO DUROU {0} HORA(S)".format(duracao))
else:
    duracao = 24
    print("O JOGO DUROU {0} HORA(S)".format(duracao))