a, b, c = map(float, input().split(' '))
if a >= b and a >= c:
    maior = a
    if b >= c:
        meio = b
        menor = c
    else:
        meio = c
        menor = b
elif b >= a and b >= c:
    maior = b
    if a >= c:
        meio = a
        menor = c
    else:
        meio = c
        menor = a
elif c >= a and c >= b:
    maior = c
    if a >= b:
        meio = a
        menor = b
    else:
        meio = b
        menor = a
elif a == b and a == c:
    maior = a
    meio = b
    menor = c
a = maior
b = meio
c = menor
if a >= b+c:
    print('NAO FORMA TRIANGULO')
else:
    if a * a == b * b + c * c:
        print('TRIANGULO RETANGULO')
    if a * a > b * b + c * c:
        print('TRIANGULO OBTUSANGULO')
    if a * a < b * b + c * c:
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    if a == b != c or b == c != a or a == c != b:
        print('TRIANGULO ISOSCELES')
