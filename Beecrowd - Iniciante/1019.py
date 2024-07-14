N = int(input())
h = N // 3600
m = N % 3600 // 60
s = N % 3600 % 60
print(f'{h}:{m}:{s}')
