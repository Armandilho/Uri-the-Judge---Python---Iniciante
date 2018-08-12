import math

A, B, C = map(float, input().split())
Delta = (B**2-4*A*C)


if(A==0 or Delta<0):
    print("Impossivel calcular")
else:
    OperaçãoR1 = (-B+math.sqrt(Delta))/(2*A)
    OperaçãoR2 = (-B-math.sqrt(Delta))/(2*A)
    print('R1 = %.5f' %OperaçãoR1)
    print('R2 = %.5f' %OperaçãoR2)
