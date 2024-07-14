a, b, c = map(float, input().split())
delta = (b) * (b) - 4 * a * c
if delta > 0 and a != 0:
    r1 = (-b + (delta ** 0.5))/(2 * a)
    r2 = (-b - (delta ** 0.5))/(2 * a)
    print('R1 = %.5f' % r1)
    print('R2 = %.5f' % r2)
else:
    print('Impossivel calcular')
