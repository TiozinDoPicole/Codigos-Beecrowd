n = int(input())
for x in range(0, n):
    x, y = map(int, input().split(' '))
    if x == 0:
        print(0.0)
    elif y == 0:
        print('divisao impossivel')
    else:
        d = x / y
        print('%.1f' % d)