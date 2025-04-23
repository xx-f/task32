import math_func

a = float(input("Укажите, чему равно ребро куба "))
print("Объем куба равен ", math_func.cube(a))

a, b = input("Укажите катеты прямоуг. треуг. через пробел ").strip().split()
print("Гипотенуза ", math_func.hipot(float(a), float(b)))

a, b, c = input('Укажите стороны треугольника через пробел').strip().split()
print("Площадь ", math_func.GerArea(a, b, c))

a, b = input("Укажите стороны прямоугольника через пробел ").strip().split()
print('Площадь ', math_func.abArea(a, b))
