count = 2
v = 0
while count != 0:
    x = float(input())
    if x >= 0 and x <= 10:
        v += x
        count -= 1
    else:
        print('nota invalida')
med = v / 2
print('media = %.2f' % med)
while True:
    x = int(input('novo calculo (1-sim 2-nao)\n'))
    if x == 2:
        break
    elif x == 1:
        count = 2
        v = 0
        while count != 0:
            x = float(input())
            if x >= 0 and x <= 10:
                v += x
                count -= 1
            else:
                print('nota invalida')
        med = v / 2
        print('media = %.2f' % med)
