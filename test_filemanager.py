import os
import main
import bank_account
import json
import victory


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


def test_load_data():
    test_files_names = ('test load account.txt', 'test load history.txt')
    for file_name in test_files_names:
        if os.path.exists(file_name):
            os.remove(file_name)
    test_data = bank_account.load_data(test_files_names)
    assert test_data[0] == 0
    assert test_data[1] == []
    with open('test load account.txt', 'w') as f:
        f.write(str(1000))
    purchase_history = [{'purchase_name': 'стол', 'purchase_sum': 100}, {'purchase_name': 'стул', 'purchase_sum': 50}]
    with open('test load history.txt', 'w') as f:
        json.dump(purchase_history, f)
    test_data = bank_account.load_data(test_files_names)
    assert test_data[0] == 1000
    assert test_data[1] == purchase_history


def test_save_data():
    test_files_names = ('test load account.txt', 'test load history.txt')
    for file_name in test_files_names:
        if os.path.exists(file_name):
            os.remove(file_name)
    account_sum = 1000
    purchase_history = [{'purchase_name': 'стол', 'purchase_sum': 100}, {'purchase_name': 'стул', 'purchase_sum': 50}]
    save_data = (account_sum, purchase_history)
    bank_account.save_data(save_data, test_files_names)
    with open('test load account.txt') as f:
        file_sum = int(f.readline())
    assert file_sum == account_sum
    with open('test load history.txt') as f:
        history_string = f.readline()
    assert json.loads(history_string) == purchase_history


def test_save_working_dir():
    file_name = 'test working dir'
    if os.path.exists(file_name):
        os.remove(file_name)
    main.save_working_dir_content(file_name)
    folder_content = os.listdir()
    dir_filter = filter(lambda x: os.path.isdir(x), folder_content)
    files_filter = filter(lambda x: os.path.isfile(x) and x != 'test working dir', folder_content)
    dir_str = ', '.join(dir_filter)
    dir_str = f'dirs: {dir_str}'
    files_str = ', '.join(files_filter)
    files_str = f'files: {files_str}'
    with open(file_name) as f:
        file_lines = f.readlines()
    assert file_lines[0].strip() == files_str
    assert file_lines[1].strip() == dir_str


def test_string_to_float():
    assert not bank_account.string_to_float('некорректная строка')[1]
    result = bank_account.string_to_float('1.5')
    assert result[0] == 1.5 and result[1]


def test_generate_questions_list():
    persons_list = {'Н. В. Гоголь': '10.03.1809',
                    'М. Е. Салтыков-Щедрин': '27.01.1826'}
    day_strings = {'10': 'десятого',
                   '27': 'двадцать седьмого'}
    month_strings = {'03': 'марта',
                     '01': 'января'}
    result = victory.generate_questions_list(persons_list, day_strings, month_strings)
    assert result == [('Н. В. Гоголь', '10.03.1809', 'десятого', 'марта'),
                      ('М. Е. Салтыков-Щедрин', '27.01.1826', 'двадцать седьмого', 'января')]
