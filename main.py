import os
import shutil
import sys
from victory import run_victory
from bank_account import run_account


def create_folder(new_folder_name):
    if not os.path.exists(new_folder_name):
        os.mkdir(new_folder_name)
        return 'Папка создана'
    else:
        return 'Папка с таким именем уже существует'


def delete_item(item_name):
    if os.path.exists(item_name):
        if os.path.isdir(item_name):
            shutil.rmtree(item_name)
        else:
            os.remove(item_name)
        return 'Объект удален'
    else:
        return 'Объекта с таким именем не существует!'


def copy_item(item_from, item_to):
    if os.path.exists(item_from):
        if os.path.exists(item_to):
            return 'Указанное имя уже используется!'
        else:
            shutil.copytree(item_from, item_to)
            return 'Копирование выполнено'
    else:
        return 'Указанного файла не существует!'


def view_all():
    return os.listdir()


def view_folders():
    folder_content = os.listdir()
    folders_list = filter(lambda x: os.path.isdir(x), folder_content)
    return list(folders_list)


def view_files():
    folder_content = os.listdir()
    files_list = filter(lambda x: os.path.isfile(x), folder_content)
    return list(files_list)


def system_info():
    return f'ОС: {sys.platform} Версия python:{sys.version}'


def author():
    return 'Степанов'


def change_working_dir(new_working_dir):
    if sys.platform == 'linux':
        current_user = os.environ.get('USER')
        user_path = f'/home/{current_user}/'
        if not new_working_dir.startswith(user_path):
            new_working_dir = os.path.join(user_path, new_working_dir)
        if os.path.exists(new_working_dir):
            os.chdir(new_working_dir)
        else:
            return 'Указанный путь не найден!'
    else:
        return 'Функция работает только в ОС Linux'


def find_item(search_name):
    file_list = []
    result = os.walk(os.getcwd())
    for root, dirs, files in result:
        if search_name in files or search_name in dirs:
            file_list.append(os.path.join(root, search_name))
    return file_list


# def menu_item_input(menu_length):
#     while True:
#         user_input_string = input('Введите номер пункта меню: ')
#         if user_input_string.isdigit():
#             user_input = int(user_input_string)
#             if user_input in range(1, menu_length + 2):
#                 return user_input


# menu_list = [('Создать папку', create_folder),
#              ('Удалить папку или файл', delete_item),
#              ('Копировать папку или файл', copy_item),
#              ('Показать содержимое текущей папки', view_all),
#              ('Показать папки', view_folders),
#              ('Показать файлы', view_files),
#              ('Информация о системе', system_info),
#              ('Создатель программы', author),
#              ('Запустить викторину', run_victory),
#              ('Банковский счет', run_account),
#              ('Смена рабочей директории', change_working_dir),
#              ('Поиск файла или папки', find_item)]
# menu_List_length = len(menu_list)
# while True:
#     for menu_item in menu_list:
#         print(f'{menu_list.index(menu_item) + 1}) {menu_item[0]}')
#     print(f'{menu_List_length + 1}) Выход')
#     menu_item_number = menu_item_input(menu_List_length)
#     if menu_item_number == menu_List_length + 1:
#         break
#     else:
#         menu_list[menu_item_number - 1][1]()

menu_list = ['Создать папку', 'Удалить папку или файл', 'Копировать папку или файл',
             'Показать содержимое текущей папки', 'Показать папки', 'Показать файлы', 'Информация о системе',
             'Создатель программы', 'Запустить викторину', 'Банковский счет', 'Смена рабочей директории',
             'Поиск файла или папки', 'Выход']
if __name__ == '__main__':
    for menu_item in menu_list:
        print(f'{menu_list.index(menu_item) + 1}) {menu_item}')
    while True:
        menu_number_string = input('Введите номер пункта меню: ')
        if menu_number_string.isdigit():
            menu_number = int(menu_number_string) - 1
            if menu_number in range(len(menu_list)):
                if menu_number == 0:
                    folder_name = input('Введите название папки: ')
                    print(create_folder(folder_name))
                elif menu_number == 1:
                    item_to_delete = input('Введите имя удаляемого объекта: ')
                    print(delete_item(item_to_delete))
                elif menu_number == 2:
                    old_item = input('Введите имя копируемого объекта: ')
                    new_item = input('Введите имя нового объекта:')
                    print(copy_item(old_item, new_item))
                elif menu_number == 3:
                    print(view_all())
                elif menu_number == 4:
                    print(view_folders())
                elif menu_number == 5:
                    print(view_files())
                elif menu_number == 6:
                    print(system_info())
                elif menu_number == 7:
                    print(author())
                elif menu_number == 8:
                    run_victory()
                elif menu_number == 9:
                    run_account()
                elif menu_number == 10:
                    working_dir = input('Введите путь: ')
                    print(change_working_dir(working_dir))
                elif menu_number == 11:
                    item_to_find = input('Введите имя для поиска: ')
                    print(find_item(item_to_find))
                else:
                    sys.exit(0)
