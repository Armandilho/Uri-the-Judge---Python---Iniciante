entrada = input().split()

convert = [float(numero) for numero in entrada]

a, b, c = convert

Perimetro = (a + b + c)
Area = (((a+b)/2)*c)

if((b - c < a < b + c) and (a - c < b < a + c) and (a - b < c < a + b)):
    print("Perimetro = {:.1f}".format(Perimetro))
else:
    print("Area = {:.1f}".format(Area))