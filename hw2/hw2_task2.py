'''
Дано квадратное уравнение x^2+bx+c=0.
Дискриминант уравнения должен быть больше 0. Напишите программу,
которая найдет корни квадратного уравнения и округлит их до 2 знаков после запятой.
'''

a = 5
b = 3
c = -77
d = b ** 2 - 4 * a * c
x1 = round(((-b) + (d ** 0.5)) / (2 * a), 2)
x2 = round(((-b) - (d ** 0.5)) / (2 * a), 2)
print(f"Первый корень:{x1}\nВторой корень:{x2}")
