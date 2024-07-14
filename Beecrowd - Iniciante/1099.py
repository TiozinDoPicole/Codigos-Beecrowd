n = int(input())
for c in range(0, n, 1):
    x, y = map(int, input().split(' '))
    som = 0
    if x > y:
        for i in range(y+1, x):
            if i % 2 == 1:
                som += i
    elif x < y:
        for i in range(x+1, y):
            if i % 2 == 1:
                som += i
    elif x == y:
        som = 0
    print(som)
