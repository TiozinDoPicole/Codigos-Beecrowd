posmaior = 1
maior = 0
for i in range(1, 101, 1):
    a = int(input())
    if i == 1:
        maior = a
        posmaior = 1
    elif a > maior:
        maior = a
        posmaior = i
print(maior)
print(posmaior)
