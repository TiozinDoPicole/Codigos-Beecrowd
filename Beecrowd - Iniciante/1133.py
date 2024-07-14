x = int(input())
y = int(input())
if x > y:
    for a in range(y+1, x):
        if a % 5 == 2 or a % 5 == 3:
            print(a)
            a += 1
        else:
            a += 1
elif x < y:
    for a in range(x+1, y):
        if a % 5 == 2 or a % 5 == 3:
            print(a)
            a += 1
        else:
            a += 1