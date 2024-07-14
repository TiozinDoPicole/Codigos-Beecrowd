n1 = [float(x) if '.' in x else int(x) for x in input().split(' ')]
n2 = [float(x) if '.' in x else int(x) for x in input().split(' ')]
p = n1[1] * n1[2] + n2[1] * n2[2]
print(f'VALOR A PAGAR: R$ {p:.2f}')
