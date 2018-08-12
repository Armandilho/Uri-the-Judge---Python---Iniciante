Numero = float(input())

if(Numero<0 or Numero>100):
    print("Fora de intervalo")
elif(0<=Numero<=25):
    print("Intervalo [0,25]")
elif(25< Numero<=50):
    print("Intervalo (25,50]")
elif(50< Numero<=75):
    print("Intervalo (50,75]")
elif(75< Numero<=100):
    print("Intervalo (75,100]")