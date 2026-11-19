
import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть крок h: "))

n = int((b - a) / h) + 1

for i in range(n):
    x = a + i * h
    y = 7 - math.cos(2 * x - 1) + math.sqrt(abs(x))
    print("x =", round(x, 2), "y =", round(y, 4))
