import math

a,b,c=map(int,input().split())
def Angles(a, b, c):
    A = math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
    B = math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
    C = 180 - A - B
    return A, B, C
if a + c > b and a + b > c and b + c > a:
    angles = Angles(a, b, c)
    print("Угол A = {}".format(angles[0]))
    print("Угол B = {}".format(angles[1]))
    print("Угол C = {}".format(angles[2]))
else:
    print("Такого треугольника не существует")