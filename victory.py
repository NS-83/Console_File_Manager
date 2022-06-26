import random
# Чтоб много не писать в словарях только дни и месяца из вопросов лотереи)
DAY_STRINGS = {'03': 'третьего',
              '05': 'пятого',
              '06': 'шестого',
              '09': 'девятого',
              '10': 'десятого',
              '13': 'тринадцатого',
              '15': 'пятнадцатого',
              '29': 'двадцать девятого',}

MONTHS_STRINGS = {'01': 'января',
                  '02': 'февраля',
                  '06': 'июня',
                  '09': 'сентября',
                  '10': 'октября',
                  '11': 'ноября',
                  '12': 'декабря'}
PERSONS_LIST = {'А. С. Пушкин': '06.06.1799',
                  'М. Ю. Лермонтов': '15.10.1814',
                  'А. В. Жуковский': '09.02.1783',
                  'Н. А. Некрасов': '10.12.1821',
                  'А. А. Фет': '05.12.1820',
                  'И. С. Тургенев': '09.11.1818',
                  'И. А. Крылов': '13.02.1769',
                  'С. А. Есенин': '03.10.1895',
                  'Л. Н. Толстой': '09.09.1828',
                  'А. П. Чехов': '29.01.1860'}


def get_birthday_data(birthdays_list, chosen_person):
    birthday_string = birthdays_list[chosen_person]
    data_parts = birthday_string.split('.')
    return {'birthday_string': birthday_string,
            'birthday_parts': data_parts}


def run_victory():
    while True:
        persons = random.sample(PERSONS_LIST.keys(), 5)
        right_answers = 0
        wrong_answers = 0
        for person in persons:
            answer = input(f'Введите дату рождения писателя: {person}: ')
            birthday_data = get_birthday_data(PERSONS_LIST, person)
            if answer == birthday_data['birthday_string']:
                right_answers += 1
            else:
                wrong_answers += 1
                birthday_parts = birthday_data['birthday_parts']
                print(f'{person} родился {DAY_STRINGS[birthday_parts[0]]} '
                      f'{MONTHS_STRINGS[birthday_parts[1]]} {birthday_parts[2]}')
        print(f'Правильных ответов: {right_answers}')
        print(f'Неправильных ответов: {wrong_answers}')
        play_again = None
        while play_again not in ['да', 'нет']:
            play_again = input('Сыграть ещё раз? (да/нет):')
        if play_again == 'нет':
            break
