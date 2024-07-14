while True:
    m, n = map(int, input().split(' '))
    som = 0
    if m <= 0 or n <= 0:
        break
    if m > n:
        texto = ''
        for i in range(n, m+1):
            texto += str(i) + ' '
            som += i
    if m < n:
        texto = ''
        for i in range(m, n+1):
            som += i
            texto += str(i) + ' '
    print(f'{texto}Sum={som}')