a, b, c = map(float, input().split())
MaiorAB = (a + b + abs(a - b)) / 2
MaiorABC = (MaiorAB + c + abs(MaiorAB - c)) / 2
print ("%d eh o maior" % MaiorABC)