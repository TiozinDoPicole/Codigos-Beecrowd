hi, mi, hf, mf = map(int, input().split(' '))
if hi == mi == hf == mf:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif hi < hf and mi < mf:
    Dh = hf - hi
    Dm = mf - mi
    print(f'O JOGO DUROU {Dh} HORA(S) E {Dm} MINUTO(S)')
elif hi > hf and mi > mf:
    Dh = hf - hi + 23
    Dm = mf - mi + 60
    print(f'O JOGO DUROU {Dh} HORA(S) E {Dm} MINUTO(S)')
elif hi < hf and mi > mf:
    Dm = mf - mi + 60
    Dh = hf - hi - 1
    print(f'O JOGO DUROU {Dh} HORA(S) E {Dm} MINUTO(S)')
elif hi > hf and mi < mf:
    Dh = hf - hi + 24
    Dm = mf - mi
    print(f'O JOGO DUROU {Dh} HORA(S) E {Dm} MINUTO(S)')
elif hf == hi and mi < mf:
    Dm = mf - mi
    print(f'O JOGO DUROU 0 HORA(S) E {Dm} MINUTO(S)')
elif hf == hi and mi > mf:
    Dm = mf - mi + 60
    Dh = hf - hi + 23
    print(f'O JOGO DUROU {Dh} HORA(S) E {Dm} MINUTO(S)')
