import random


def creating_records_for_tables_students():

    random_name_list = ['Анна', 'Пётр', 'Валерий', 'Дмитрий', 'Наталья', 'Александр',
                        'Александра', 'Оксана', 'Елена', 'Алёна', 'Алла', 'Илья', 'Никита',
                        'Алексей', 'Фёдор']

    random_surname_list = ['Шмидт', 'Бутько', 'Алексеенко', 'Вуд', 'Дудь', 'Андрушко',
                           'Поплевко', 'Иванов(а)', 'Петров(а)']

    random_patronymic_list = ['Сергеевич(-на)', 'Анатольевич(-на)', 'Валерьвевич(-на)',
                              'Александрович(-на)', 'Дмитриевич(-на)']

    while True:

        number_of_records = int(input('Сколько записей Вы хотите внести? '))

        if number_of_records > 0:
            number_of_records -= 1
            break

        else:
            print('Неверное число. Попробуйте снова')

    print()
    print('insert into students(name, start_year)')
    print('values')

    for i in range(1, number_of_records + 1):
        name = random.choice(random_name_list)
        surname = random.choice(random_surname_list)
        patronymic = random.choice(random_patronymic_list)
        print(f'({name} {surname} {patronymic}),')
        if i == number_of_records:
            print(f'({name} {surname} {patronymic});')

    print()
    print('Для выполнения запроса его надо скопировать, вставить в поле СУБД и выполнить.')
    print('Запрос начинается со слова "insert" и заканчивается на ";"')


def creating_records_for_tables_courses():

    first_word_list = ['Автоматизация.Базовая часть', 'Программирование.Базовая Часть',
                       'Автоматизация.Продвинутая часть', 'Программирование.Продвинутая часть']

    second_word_list = ['JavaScript', 'Python', 'Java', 'С#']

    while True:

        number_of_records = int(input('Сколько записей Вы хотите внести? '))

        if number_of_records > 0:
            number_of_records -= 1
            break

        else:
            print('Неверное число. Попробуйте снова')

    print()
    print('insert into courses (title, hours)')
    print('values')

    for i in range(1, number_of_records + 1):
        first_word = random.choice(first_word_list)
        second_word = random.choice(second_word_list)
        print(f"('{first_word} на {second_word}', {random.randint(50, 250)}),")
        if i == number_of_records:
            print(f"('{first_word} на {second_word}', {random.randint(50, 250)});")

    print()
    print('Для выполнения запроса его надо скопировать, вставить в поле СУБД и выполнить.')
    print('Запрос начинается со слова "insert" и заканчивается на ";"')


def creating_entries_for_tables_exams():

    score_random_list = ['5', '6', '7', '8', '9', '10', 'null']

    while True:
        quantity_students = int(input('Сколько студентов сейчас зарегестрировано в таблице "Students"? '))
        quantity_courses = int(input('Сколько курсов сейчас зарегестрировано в таблице "Courses"? '))

        if quantity_students > 0 and quantity_courses > 0:
            break
        else:
            print('Введены неверные значения. Повторите снова')

    while True:

        number_of_records = int(input('Сколько записей Вы хотите внести? '))

        if number_of_records > 0:
            number_of_records -= 1
            break
        else:
            print('Неверное число. Попробуйте снова')

    print()
    print('insert into exams (s_id, c_no, score)')
    print('values')

    for i in range(1, number_of_records + 1):
        id_student = random.randint(1, quantity_students)
        id_courses = random.randint(1, quantity_courses)
        score = random.choice(score_random_list)
        print(f'({id_student}, {id_courses}, {score}),')
        if i == number_of_records:
            print(f'({id_student}, {id_courses}, {score});')

    print()
    print('Для выполнения запроса его надо скопировать, вставить в поле СУБД и выполнить.')
    print('Запрос начинается со слова "insert" и заканчивается на ";"')


def menu():

    print('Здраствуйте!')
    print('Введите "1" для таблицы "students"')
    print('Введите "2" для таблицы "courses"')
    print('Введите "3" для таблицы "exams"')

    while True:

        question = int(input('В какую из 3 таблиц вы хотите внести записи? '))

        if question == 1:
            creating_records_for_tables_students()
            break
        elif question == 2:
            creating_records_for_tables_courses()
            break
        elif question == 3:
            creating_entries_for_tables_exams()
            break
        else:
            print('Введите пожалуйста 1, 2 либо 3.')


menu()