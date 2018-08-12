Valores = {1:4,2:4.5,3:5,4:2,5:1.5}

Desejo, quantidade = [int(x) for x in input().split(" ")]

Total = Valores[Desejo]*quantidade

print("Total: R$ %.2f" %Total )