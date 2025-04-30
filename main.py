import math_func
import new

'''
a = float(input("Укажите, чему равно ребро куба "))
print("Объем куба равен ", math_func.cube(a))

a, b = input("Укажите катеты прямоуг. треуг. через пробел ").strip().split()
print("Гипотенуза ", math_func.hipot(float(a), float(b)))

a, b, c = input('Укажите стороны треугольника через пробел ').strip().split()
print("Площадь ", math_func.GerArea(float(a), float(b), float(c)))

a, b = input("Укажите стороны прямоугольника через пробел ").strip().split()
print('Площадь ', math_func.abArea(float(a), float(b)))
'''




a = int(input('Хотите сгенерировать случайный пароль? 0-Yes, 1-No'))


if a == 0:
    b=int(input('Какой длинны вы хотите пароль?'))
    print(generate_password(b))