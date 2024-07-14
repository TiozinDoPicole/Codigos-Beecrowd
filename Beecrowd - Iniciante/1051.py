sal = float(input())
if sal <= 2000:
    print('Isento')
elif sal <= 3000:
    Im = (sal - 2000) * 0.08
    print('R$ %.2f' % Im)
elif sal <= 4500:
    Im = (sal - 2000 - 1000) * 0.18 + \
        ((sal - 2000 - (sal - 2000 - 1000)) * 0.08)
    print('R$ %.2f' % Im)
else:
    Im = ((sal - 2000 - 1000 - 1500) * 0.28) + ((sal - 2000 - 1000 - (sal -
                                                                      2000 - 1000 - 1500)) * 0.18) + ((sal - 2000 - (sal - 2000 - 1000)) * 0.08)
    print('R$ %.2f' % Im)
