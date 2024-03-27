import os
import sys
import main


def test_create_folder():
    test_folder_name = 'test_create'
    if os.path.exists(test_folder_name):
        assert main.create_folder(test_folder_name) == 'Папка с таким именем уже существует'
    else:
        assert main.create_folder(test_folder_name) == 'Папка создана' and os.path.exists(test_folder_name)


def test_delete_item():
    test_folder_name = 'test_delete'
    if os.path.exists(test_folder_name):
        assert main.delete_item(test_folder_name) == 'Объект удален' and not os.path.exists(test_folder_name)
    else:
        assert main.delete_item(test_folder_name) == 'Объекта с таким именем не существует!'


def test_copy_item():
    test_copy_from = 'test_copy'
    test_copy_to = 'test_copy_to'
    if not os.path.exists(test_copy_from):
        os.mkdir(test_copy_from)
    if os.path.exists(test_copy_to):
        assert main.copy_item(test_copy_from, test_copy_to) == 'Указанное имя уже используется!'
    else:
        assert main.copy_item(test_copy_from, test_copy_to) == 'Копирование выполнено' and os.path.exists(test_copy_to)


def test_author():
    assert main.author() == 'Степанов'

