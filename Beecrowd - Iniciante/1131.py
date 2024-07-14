grenal = 1
vi = 0
vg = 0
e = 0
i, g = map(int, input().split(' '))
if i > g:
    vi += 1
elif g > i:
    vg += 1
elif g == i:
    e += 1
while True:
    x = int(input('Novo grenal (1-sim 2-nao)\n'))
    if x == 2:
        break
    elif x == 1:
        i, g = map(int, input().split(' '))
        grenal += 1
    if i > g:
        vi += 1
    elif g > i:
        vg += 1
    elif g == i:
        e += 1
print(f'{grenal} grenais')
print(f'Inter:{vi}')
print(f'Gremio:{vg}')
print(f'Empates:{e}')
if vg < vi:
    print('Inter venceu mais')
elif vg > vi:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
