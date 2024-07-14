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