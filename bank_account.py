"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""
import json
import os

ACCOUNT_SUM_FILE = 'account.txt'
SHOPPING_HISTORY_FILE = 'shopping.txt'


def increase_account():
    return sum_input('пополнения')


def make_purchase(account_sum):
    purchase_sum = sum_input('покупки')
    if purchase_sum > account_sum:
        print(f'На счету не хватает {purchase_sum - account_sum}!')
    else:
        purchase_name = input('Введите название покупки: ')
        return {'purchase_name': purchase_name, 'purchase_sum': purchase_sum}


def purchase_history_decorator(fn):
    def inner_func(*args):
        print('История покупок')
        fn(*args)
    return inner_func


@purchase_history_decorator
def print_purchase_history(purchase_list):
    for purchase_data in purchase_list:
        print(f'Покупка: {purchase_data["purchase_name"]} Сумма: {purchase_data["purchase_sum"]}')


def sum_input(sum_type):
    while True:
        sum_string = input(f'Введите сумму {sum_type}: ').strip()
        result = string_to_float(sum_string)
        if result[1]:
            return result[0]
        else:
            print('Введена некорректная сумма!')


def string_to_float(sum_string):
    try:
        sum_float = float(sum_string)
        return sum_float, True
    except ValueError:
        return 0, False


def save_data(data, file_names):
    with open(file_names[0], 'w') as f:
        account_sum = str(data[0])
        f.write(account_sum)
    with open(file_names[1], 'w') as f:
        json.dump(data[1], f)


def load_data(file_names):
    account_sum = 0
    shopping_list = []
    if os.path.exists(file_names[0]):
        with open(file_names[0]) as f:
            file_line = f.readline()
            account_sum = float(file_line)
    if os.path.exists(file_names[1]):
        with open(file_names[1]) as f:
            shopping_list = json.load(f)
    return account_sum, shopping_list


def run_account():
    saved_files = (ACCOUNT_SUM_FILE, SHOPPING_HISTORY_FILE)
    saved_data = load_data(saved_files)
    account = saved_data[0]
    purchase_history = saved_data[1]
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            account += increase_account()
        elif choice == '2':
            purchase = make_purchase(account)
            if purchase:
                account -= purchase['purchase_sum']
                purchase_history.append(purchase)
        elif choice == '3':
            print_purchase_history(purchase_history)
        elif choice == '4':
            data_to_save = (account, purchase_history)
            save_data(data_to_save, saved_files)
            break
        else:
            print('Неверный пункт меню')
