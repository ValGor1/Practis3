raw = input('Enter number:')
try:
    num = int(raw)
    print(num)
except ValueError:
    print("Это не число")
