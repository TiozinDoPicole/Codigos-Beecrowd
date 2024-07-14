x = int(input())
y = int(input())
som = 0
if x > y:
    i = y + 1
    f = x - 1
    for n in range(i, f+1, 1):
        if i % 2 == 1:
            som += i
            i += 1
        else:
            i += 1
else:
    i = x + 1
    f = y - 1
    for n in range(i, f+1, 1):
        if i % 2 == 1:
            som += i
            i += 1
        else:
            i += 1
print(som)
