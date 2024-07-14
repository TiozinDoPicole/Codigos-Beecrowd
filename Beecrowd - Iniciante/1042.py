a, b, c = map(int, input().split(' '))
if a > b and a > c:
    maior = a
    if b > c:
        meio = b
        menor = c
    else:
        meio = c
        menor = b
elif b > a and b > c:
    maior = b
    if a > c:
        meio = a
        menor = c
    else:
        meio = c
        menor = a
elif c > a and c > b:
    maior = c
    if a > b:
        meio = a
        menor = b
    else:
        meio = b
        menor = a
print(f'{menor}\n{meio}\n{maior}\n')
print(f'{a}\n{b}\n{c}')
