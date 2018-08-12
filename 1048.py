salario = round(float(input()),2)

if(0 < salario <= 400.00):
    aumento = ((salario * 15)/100)
    novosalario = salario + aumento
    print("Novo salario: {0:.2f}".format(novosalario))
    print("Reajuste ganho: {0:.2f}".format(aumento))
    print("Em percentual: 15 %")
elif(400.00 < salario <= 800.00):
    aumento = ((salario * 12)/100)
    novosalario = salario + aumento
    print("Novo salario: {0:.2f}".format(novosalario))
    print("Reajuste ganho: {0:.2f}".format(aumento))
    print("Em percentual: 12 %")
elif(800.00 < salario <= 1200.00):
    aumento = ((salario * 10)/100)
    novosalario = salario + aumento
    print("Novo salario: {0:.2f}".format(novosalario))
    print("Reajuste ganho: {0:.2f}".format(aumento))
    print("Em percentual: 10 %")
elif(1200.00 < salario <= 2000.00):
    aumento = ((salario * 7)/100)
    novosalario = salario + aumento
    print("Novo salario: {0:.2f}".format(novosalario))
    print("Reajuste ganho: {0:.2f}".format(aumento))
    print("Em percentual: 7 %")
else:
    aumento = ((salario * 4)/100)
    novosalario = salario + aumento
    print("Novo salario: {0:.2f}".format(novosalario))
    print("Reajuste ganho: {0:.2f}".format(aumento))
    print("Em percentual: 4 %")