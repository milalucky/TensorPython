'''
Дано 2 строки из неповторяющихся символов: первая строка длиной 3 символа,
вторая точно содержит символы первой строки в любом порядке. Напишите программу,
не используя циклы и условия, которая находит срез минимальной длины во второй строке,
который будет содержать все символы первой строки. Например,
first_string = ‘wtf’ и second_string = ‘brick quzjmpy veldt whangs fox’, срез минимальной длины: ‘t whangs f’
'''

first_string = "wtf"
second_string = "brick quzjmpy veldt whangs fox"
s1 = second_string.find(first_string[0])
s2 = second_string.find(first_string[1])
s3 = second_string.find(first_string[2])
s_min = min(s1, s2, s3)
s_max = max(s1, s2, s3)
print(second_string[s_min:s_max + 1])