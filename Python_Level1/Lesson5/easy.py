
# coding: utf-8

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
for i in range(1,10):
    try:
        os.mkdir('dir_' + str(i))
    except FileExistsError:
        print('Папка уже существует')
for i in range(1,10):
    try:
        os.removedirs('dir_' + str(i))
    except FileNotFoundError:
        print('Не удается найти указанную папку')
        
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os
files_and_dirs = os.listdir()
for i in files_and_dirs:
    if os.path.isdir(i):
        print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
# 1st way 
with open('easy.py', 'rb') as source:
    source_text = source.read()
    with open('easy__copy.py', 'wb') as dst:
        dst.write(source_text)
# 2nd way      
shutil.copy('easy.py', 'easy_copy.py', follow_symlinks=True)

