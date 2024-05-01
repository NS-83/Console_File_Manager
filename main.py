import os
import shutil
import sys
from victory import run_victory
from bank_account import run_account

MENU_LIST = ['Создать папку', 'Удалить папку или файл', 'Копировать папку или файл',
             'Показать содержимое текущей папки', 'Показать папки', 'Показать файлы', 'Информация о системе',
             'Создатель программы', 'Запустить викторину', 'Банковский счет', 'Смена рабочей директории',
             'Поиск файла или папки', 'Сохранить содержимое рабочей директории в файл', 'Выход']
WORKING_DIR_CONTENT_FILE_NAME = 'workingdir.txt'


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


def save_working_dir_content(file_name):
    folder_content = os.listdir()
    dir_filter = filter(lambda x: os.path.isdir(x), folder_content)
    files_filter = filter(lambda x: os.path.isfile(x), folder_content)
    dir_str = ', '.join(dir_filter)
    dir_str = f'dirs: {dir_str}\n'
    files_str = ', '.join(files_filter)
    files_str = f'files: {files_str}\n'
    file_data = [files_str, dir_str]
    with open(file_name, 'w') as f:
        f.writelines(file_data)


def print_menu():
    for menu_item in MENU_LIST:
        print(f'{MENU_LIST.index(menu_item) + 1}) {menu_item}')


def get_menu_item_number():
    while True:
        user_input_string = input('Введите номер пункта меню: ')
        if user_input_string.isdigit():
            user_input = int(user_input_string)
            if user_input in range(1, len(MENU_LIST) + 1):
                return user_input


if __name__ == '__main__':
    while True:
        print_menu()
        chosen_item = get_menu_item_number()
        print(chosen_item)
        if chosen_item == 1:
            new_folder = input('Введите имя новой папки: ')
            create_folder(new_folder)
        elif chosen_item == 2:
            item_to_delete = input('Введите имя удаляемого элемента: ')
            delete_item(item_to_delete)
        elif chosen_item == 3:
            copy_from = input('Введите копируемый элемент: ')
            copy_to = input('Введите новый элемент: ')
            copy_item(copy_from, copy_to)
        elif chosen_item == 4:
            view_all()
        elif chosen_item == 5:
            view_folders()
        elif chosen_item == 6:
            view_files()
        elif chosen_item == 7:
            system_info()
        elif chosen_item == 8:
            author()
        elif chosen_item == 9:
            run_victory()
        elif chosen_item == 10:
            run_account()
        elif chosen_item == 11:
            new_dir = input('Введите новую рабочую директорию: ')
            change_working_dir(new_dir)
        elif chosen_item == 12:
            item_to_search = input('Введите имя для поиска: ')
            find_item(item_to_search)
        elif chosen_item == 13:
            save_working_dir_content(WORKING_DIR_CONTENT_FILE_NAME)
        elif chosen_item == 14:
            sys.exit(0)
