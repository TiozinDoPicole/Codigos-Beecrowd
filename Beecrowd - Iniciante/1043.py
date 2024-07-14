a, b, c = map(float, input().split(' '))
if a > abs(b - c) and a < b + c and b > abs(a - c) and b < a + c and c > abs(b - c) and c < a + b:
    p = a + b + c
    print('Perimetro = %.1f' % p)
else:
    A = ((a + b) * c)/2
    print('Area = %.1f' % A)
