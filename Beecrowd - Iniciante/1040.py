n1, n2, n3, n4 = map(float, input().split())
med = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1)/10
print('Media: %.1f' % med)
if med >= 7:
    print('Aluno aprovado.')
elif med < 5:
    print('Aluno reprovado.')
elif med >= 5 and med <= 6.9:
    print('Aluno em exame.')
    N = float(input())
    print('Nota do exame:', N)
    medf = (med + N)/2
    if medf >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f' % medf)
