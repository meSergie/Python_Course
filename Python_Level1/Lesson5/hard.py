
# coding: utf-8

# In[4]:

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
print('sys.argv = ', sys.argv)
def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print('cp <file_name> - копирование файла')
    print('rm <file_name> - удаляет указанный файл')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('ls - отображение полного пути текущей директории')
    
def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))
        
def ping():
    print("pong")
    
def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    name, ext = dir_name.split('.')
    name = name + '_copy'
    copy_name = '.'.join([name, ext])
    #dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        with open(dir_name, 'rb') as source:
            source_text = source.read()
            with open(copy_name, 'wb') as dst:
                dst.write(source_text)
    except FileNotFoundError:
        print('Файла {} не существует', dir_name)
        
def remove_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    accept = input('Удалить файл? Y/N:')
    if accept == 'N':
        return
    if accept == 'Y':
        try:
            os.remove(dir_name)
            print('Файл успешно удален: ', dir_name)
        except FileNotFoundError:
            print('Невозможно удалить файл')
            print('Такого файла не существует')
            
def change_dir():
    if not dir_name:
        print("Необходимо указать путь вторым параметром")
        return    
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print('Успешно перешел в ', os.getcwd())
    except FileNotFoundError:
        print('Невозможно перейти')

def full_path():
    print('Полный путь текущей директории',os.getcwd())
            
do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    'cp': copy_file,
    'rm': remove_file,
    'cd': change_dir,
    'ls': full_path
}
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

