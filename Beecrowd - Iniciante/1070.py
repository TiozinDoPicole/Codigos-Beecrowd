x = int(input())
for i in range(0, 12, 2):
    if x % 2 == 0:
        i += x + 1
        print(i)
    else:
        i += x
        print(i)