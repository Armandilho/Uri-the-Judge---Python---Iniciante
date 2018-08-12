j = 1
for i in range(0, 21, 2):
    for k in range(1, 4):
        if(i == 0 or i == 10 or i == 20):
            print("I={:.0f} J={:.0f}".format(i/10,j))
        else:
            print("I={:.1f} J={:.1f}".format(i/10,j))
        j = j + 1
    j = j - 2.8