a, b, c = map(int, input().split(' '))
maiorAB = (a+b+abs(a-b))//2
Maior = (maiorAB+c+abs(maiorAB-c))//2
print(f'{Maior} eh o maior')
