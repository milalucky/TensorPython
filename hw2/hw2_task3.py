'''
Дано 2 строки. Напишите программу, которая объединит эти две строки в одну и разделит их пробелом,
а также поменяет местами первые два символа первой строки на первые два символа второй строки и наоборот.
'''

a = "Heивет мир!"
b = "Прllo world!"
result = a.replace(a[:2], b[:2]) + " " + b.replace(b[:2], a[:2])
print(result)
