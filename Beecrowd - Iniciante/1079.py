N = int(input())
for x in range(0, N, 1):
    x1, x2, x3 = map(float, input().split(' '))
    m = (x1 * 2 + x2 * 3 + x3 * 5)/10
    print('%.1f' % m)
