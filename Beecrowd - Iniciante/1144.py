n = int(input())
a = 1
qa = a ** 2
ca = a ** 3
for x in range(0, n):
    print(a, qa, ca)
    print(a, qa+1, ca+1)
    a += 1
    qa = a ** 2
    ca = a ** 3
