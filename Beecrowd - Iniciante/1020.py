I = int(input())
a = I // 365
m = I % 365 // 30
d = I % 365 % 30
print(f'{a} ano(s)')
print(f'{m} mes(es)')
print(f'{d} dia(s)')
