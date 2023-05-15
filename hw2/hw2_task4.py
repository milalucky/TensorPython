'''
Дан абсолютный путь до файла. Вывести название файла без расширения, названия диска и корневую папку.
'''

file = "C:\python3\m.ail.txt"
full_name = file.split('\\')[-1]
name = full_name[:full_name.rfind('.')]
disk_name = file.split(':')[0]
directory = file.split('\\')[1]
print(f'Имя файла: {name}\nИмя диска: {disk_name}\nКорневая папка: {directory}')