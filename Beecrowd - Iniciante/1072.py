N = int(input())
inn = 0
out = 0
for x in range(0, N, 1):
    X = int(input())
    if X >= 10 and X <= 20:
        inn += 1
    else:
        out += 1
print(f'{inn} in')
print(f'{out} out')
