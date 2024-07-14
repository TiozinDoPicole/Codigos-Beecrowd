i = 0
j1, j2, j3 = 1, 2, 3
for x in range(0, 11, 1):
    if i == 0.0 or i == 1.0 or i == 2.0:
        print(f'I={int(i)} J={j1:.0f}')
        print(f'I={int(i)} J={j2:.0f}')
        print(f'I={int(i)} J={j3:.0f}')
        i += 0.2
        j1 += 0.2
        j2 += 0.2
        j3 += 0.2
    else:
        print(f'I={i:.1f} J={j1:.1f}')
        print(f'I={i:.1f} J={j2:.1f}')
        print(f'I={i:.1f} J={j3:.1f}')
        i += 0.2
        j1 += 0.2
        j2 += 0.2
        j3 += 0.2
