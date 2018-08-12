peca1, qtd1, vUnit1 = map(float, input().split())
peca2, qtd2, vUnit2 = map(float, input().split())

valor1=(qtd1*vUnit1)
valor2=(qtd2*vUnit2)
valorfinal=(valor1+valor2)

print('VALOR A PAGAR: R$ %.2f' %valorfinal)