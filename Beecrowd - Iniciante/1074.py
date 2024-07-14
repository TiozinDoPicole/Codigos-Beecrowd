N = int(input())
for x in range(0, N, 1):
    y = int(input())
    if y == 0:
        print('NULL')
    elif y > 0:
        if y % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    else:
        if y % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')
