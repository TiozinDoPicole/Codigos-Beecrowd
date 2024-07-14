[A, B, C] = [float(x) for x in input().split(' ')]
Atri = (A * C)/2
Ac = 3.14159 * C ** 2
Atra = ((A+B)*C)/2
Aq = B * B
Ar = A * B
print(f'TRIANGULO: {Atri:.3f}')
print(f'CIRCULO: {Ac:.3f}')
print(f'TRAPEZIO: {Atra:.3f}')
print(f'QUADRADO: {Aq:.3f}')
print(f'RETANGULO: {Ar:.3f}')
