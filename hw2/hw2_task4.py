'''
Дан абсолютный путь до файла. Вывести название файла без расширения, названия диска и корневую папку.
'''

file = "C:\python3\m.ail.txt"
full_name = file.split('\\')[-1]
name = full_name[:full_name.rfind('.')]
print(name)