x, y = int(input()), int(input())
som = 0
if x > y:
    for a in range(y, x+1):
        if a % 13 != 0:
            som += a
            a += 1
        else:
            a += 1
elif x < y:
    for a in range(x, y+1):
        if a % 13 != 0:
            som += a
            a += 1
        else:
            a += 1
print(som)
