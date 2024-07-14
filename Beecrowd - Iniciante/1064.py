count = 0
p = 0
for x in range(0, 6, 1):
    n = float(input())
    if n > 0:
        count += 1
        p = p + n
med = p / count
print(f'{count} valores positivos')
print(f'{med:.1f}')
