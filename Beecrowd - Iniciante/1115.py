while True:
    x, y = map(int, input().split(' '))
    if x == 0 or y == 0:
        break
    elif x >= 1 and y >= 1:
        print('primeiro')
    elif x >= 1 and y <= 1:
        print('quarto')
    elif x <= 1 and y >= 1:
        print('segundo')
    elif x <= 1 and y <= 1:
        print('terceiro')
