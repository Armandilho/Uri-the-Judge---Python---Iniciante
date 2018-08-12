i = 1
j = 1
k = 7
for i in range(1, 10, 2):
    for j in range(7, 4, -1):
        print("I={0} J={1}".format(i,k))
        k = k - 1
    k = k + 5