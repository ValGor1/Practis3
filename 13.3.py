import random
X, Y = map(int, input().split())
x = X % Y
y = Y % X
print('1' if x == 0 or y == 0  else random.randint(0,10000))