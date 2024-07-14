a, d1 = input().split(' ')
h1, m1, s1 = map(int, input().split(' : '))
b, d2 = input().split(' ')
h2, m2, s2 = map(int, input().split(' : '))
d1 = int(d1)
d2 = int(d2)
ts1 = d1 * 86400 + h1 * 3600 + m1 * 60 + s1
ts2 = d2 * 86400 + h2 * 3600 + m2 * 60 + s2
if ts1 < ts2:
    T = ts2 - ts1
    D = T // 86400
    Th = T % 86400 // 3600
    Tm = T % 86400 % 3600 // 60
    Ts = T % 86400 % 3600 % 60
    print(f'{D} dia(s)\n{Th} hora(s)\n{Tm} minuto(s)\n{Ts} segundo(s)')
