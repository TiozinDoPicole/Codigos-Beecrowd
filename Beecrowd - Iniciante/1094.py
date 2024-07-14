n = int(input())
tot = 0
Ctot = 0
Rtot = 0
Stot = 0
for i in range(0, n, 1):
    q, t = input().split(' ')
    q = int(q)
    if t == 'C':
        Ctot += q
        tot += q
    elif t == 'R':
        Rtot += q
        tot += q
    elif t == 'S':
        Stot += q
        tot += q
pC = (Ctot * 100)/tot
pR = (Rtot * 100)/tot
pS = (Stot * 100)/tot
print(f'Total: {tot} cobaias')
print('Total de coelhos:', Ctot)
print('Total de ratos:', Rtot)
print('Total de sapos:', Stot)
print(f'Percentual de coelhos: {pC:.2f} %')
print(f'Percentual de ratos: {pR:.2f} %')
print(f'Percentual de sapos: {pS:.2f} %')
