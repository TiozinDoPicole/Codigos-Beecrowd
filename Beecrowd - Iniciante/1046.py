hi, hf = map(int, input().split(' '))
if hi == hf:
    print('O JOGO DUROU 24 HORA(S)')
elif hi > hf:
    D = hf - hi + 24
    print(f'O JOGO DUROU {D} HORA(S)')
else:
    D = hf - hi
    print(f'O JOGO DUROU {D} HORA(S)')
