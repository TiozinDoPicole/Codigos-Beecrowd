A = 0
T = int(input())
for x in range(0, T, 1):
    PA, PB, G1, G2 = map(float, input().split(' '))
    PA = int(PA)
    PB = int(PB)
    if G2 == 0:
        while PA <= PB:
            PA = int(PA * (G1/100))
            A = A + 1
        if A > 100:
            print('Mais de 1 seculo')
        else:
            print(f'{A} anos')
    else:
        while PA <= PB:
            PA = int(PA * (G1/100))
            PB = int(PB * (G2/100))
            A = A + 1
        if A > 100:
            print('Mais de 1 seculo')
        else:
            print(f'{A} anos')
