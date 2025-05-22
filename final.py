# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile

name = ''
age = 0
phone = ''
email = ''
adress = ''
index = ''
additional_information = ''

# bank details

ogrnip = ''
inn = ''
current_account = ''
bank_name = ''
bic = ''
correspondent_account = ''


def count_digits_from_numbers(number):

  last_number = 0
  count = 0

  while number > 0:
    last_number = number % 10
    count += 1
    number //= 10

  return count


def filter_and_then_return_a_new_index(old_index):

  new_index = ''

  for index_symbol in old_index:

    if index_symbol.isdigit():
      new_index += index_symbol

  return new_index


def display_user_information(name_parameter, age_parameter, phone_parameter, email_parameter, adress_parameter, index_parameter, additional_parameter):

    print(SEPARATOR)
    print(f'Имя:       {name_parameter}')

    if 11 <= age_parameter % 100 <= 19:
      years_parameter = 'лет'

    elif age_parameter % 10 == 1:
      years_parameter = 'год'

    elif 2 <= age_parameter % 10 <= 4:
      years_parameter = 'года'

    else:
      years_parameter = 'лет'

    print(f'Возраст:   {age_parameter, years_parameter}')
    print(f'Телефон:   {phone_parameter}')
    print(f'E-mail:    {email_parameter}')
    print(f'Индекс:    {index_parameter}')
    print(f'Адрес:     {adress_parameter}')

    if additional_parameter:
            print('')
            print('Дополнительная информация:')
            print(additional_parameter)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu

    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))

    if option == 0:
            break

    if option == 1:

        # submenu 1: edit info

        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))

            if option2 == 0:
                break

            if option2 == 1:
                # input general info
                name = input('Введите имя: ')

                while 1:
                        # validate user age

                        age = int(input('Введите возраст: '))

                        if age > 0:
                            break
                        print('Возраст должен быть положительным')

                update_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''

                for numbers in update_phone:

                    if numbers == '+' or ('0' <= numbers <= '9'):
                        phone += numbers

                email = input('Введите адрес электронной почты: ')
                index = input('Введите почтовый индекс: ')
                index = filter_and_then_return_a_new_index(index)
                adress = input('Введите почтовый адрес (без индекса): ')
                additional_information = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input bank details

                while True:
                  ogrnip = int(input('Введите ОГРНИП: '))
                  count_ogrnip = count_digits_from_numbers(ogrnip)

                  if count_ogrnip != 15:
                    print('ОГРНИП должен иметь 15 цифр.')

                  else:
                    break

                inn = int(input('Введите ИНН: '))

                while True:
                  current_account = int(input('Введите рассчётный счёт: '))
                  count_current_account = count_digits_from_numbers(current_account)

                  if count_current_account != 20:
                    print('Рассчётный счёт должен иметь 20 цифр.')

                  else:
                    break

                bank_name = input('Введите название банка: ')
                bic = int(input('Введите БИК: '))
                correspondent_account = int(input('Введите корреспондентский счёт: '))

            else:
              print('Введите корректный пункт меню')

    elif option == 2:
        # submenu 2: print info

        while True:

            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))

            if option2 == 0:
                break

            if option2 == 1:
                display_user_information(name, age, phone, email, adress, index, additional_information)

            elif option2 == 2:
                display_user_information(name, age, phone, email, adress, index, additional_information)

                # print social links

                print('')
                print('Информация о предпринимателе')
                print(f'ОГРНИП:   {ogrnip}')
                print(f'ИНН:      {inn}')
                print('Банковские реквизиты')
                print(f'Р/с:      {current_account}')
                print(f'Банк:     {bank_name}')
                print(f'БИК:      {bic}')
                print(f'К/с:      {correspondent_account}')

            else:
              print('Введите корректный пункт меню')

    else:
      print('Введите корректный пункт меню')


