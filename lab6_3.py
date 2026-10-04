import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

spisok = []

x = a

while x <= b:
    y = 7 - math.cos(2 * x - 1) + math.sqrt(abs(x))
    spisok.append(round(y, 4))
    x += h

print("Список значень функції:")
print(spisok)

print("Значення, які повторюються:")

повторені = []

for y in spisok:
    if spisok.count(y) > 1 and y not in повторені:
        повторені.append(y)
        print(y)