import os
import shutil
import sys
from victory import run_victory
from bank_account import run_account


def create_folder():
    folder_name = input('Введите название папки: ')
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    else:
        print('Папка с таким именем уже существует!')


def delete_item():
    item_name = input('Введите имя файла или папки: ')
    if os.path.exists(item_name):
        if os.path.isdir(item_name):
            shutil.rmtree(item_name)
        else:
            os.remove(item_name)
    else:
        print('Файла или папки с таким именем не существует!')


def copy_item():
    copy_from = input('Введите имя копируемого файла или папки: ')
    if os.path.exists(copy_from):
        copy_to = input('Введите имя нового файла или папки: ')
        if os.path.exists(copy_to):
            print('Указанное имя уже используется!')
        else:
            shutil.copytree(copy_from, copy_to)
    else:
        print('Указанного файла не существует!')


def view_all():
    print(os.listdir())


def view_folders():
    folder_content = os.listdir()
    folders_list = filter(lambda x: os.path.isdir(x), folder_content)
    print(list(folders_list))


def view_files():
    folder_content = os.listdir()
    files_list = filter(lambda x: os.path.isfile(x), folder_content)
    print(list(files_list))


def system_info():
    print(f'ОС: {sys.platform} Версия python:{sys.version}')


def author():
    print('Степанов')


def change_working_dir():
    if sys.platform == 'linux':
        new_working_dir = input('Введите путь: ')
        current_user = os.environ.get('USER')
        user_path = f'/home/{current_user}/'
        if not new_working_dir.startswith(user_path):
            new_working_dir = os.path.join(user_path, new_working_dir)
        if os.path.exists(new_working_dir):
            os.chdir(new_working_dir)
        else:
            print('Указанный путь не найден!')
    else:
        print('Функция работает только в ОС Linux')


def find_item():
    file_list = []
    search_name = input('Введите имя для поиска: ')
    result = os.walk(os.getcwd())
    for root, dirs, files in result:
        if search_name in files or search_name in dirs:
            file_list.append(os.path.join(root, search_name))
    print(file_list)


def menu_item_input(menu_length):
    """
    Ищем файл или папку по имени.
    """
    while True:
        user_input_string = input('Введите номер пункта меню: ')
        if user_input_string.isdigit():
            user_input = int(user_input_string)
            if user_input in range(1, menu_length + 2):
                return user_input


menu_list = [('Создать папку', create_folder),
             ('Удалить папку или файл', delete_item),
             ('Копировать папку или файл', copy_item),
             ('Показать содержимое текущей папки', view_all),
             ('Показать папки', view_folders),
             ('Показать файлы', view_files),
             ('Информация о системе', system_info),
             ('Создатель программы', author),
             ('Запустить викторину', run_victory),
             ('Банковский счет', run_account),
             ('Смена рабочей директории', change_working_dir),
             ('Поиск файла или папки', find_item)]
menu_List_length = len(menu_list)
while True:
    for menu_item in menu_list:
        print(f'{menu_list.index(menu_item) + 1}) {menu_item[0]}')
    print(f'{menu_List_length + 1}) Выход')
    menu_item_number = menu_item_input(menu_List_length)
    if menu_item_number == menu_List_length + 1:
        break
    else:
        menu_list[menu_item_number - 1][1]()












