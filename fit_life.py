# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30  # норма воды в миллилитрах на 1 кг
ML_IN_LITERS = 1000  # Константа для перевода миллилитров в литры


def calculate_bmi(user_weight: float, user_height: float):
    """Функция выполняет расчет ИМТ и нормы воды в день(в литрах)

    param:
    user_weight(float) - Вес
    user_height(float) - Рост

    return:
    bmi - Индекс массы тела
    water_needed_liters - Норма воды в день(В литрах)
    """
    bmi = round(user_weight / (user_height ** 2), 1)

    # Подсчет воды: вес * 30 мл(сразу делим на 1000 чтоб перевести в литры)
    water_needed_liters = round(user_weight * WATER_PER_KG / ML_IN_LITERS, 1)

    return bmi, water_needed_liters


if __name__ == '__main__':
    # 1. Знакомство с пользователем
    print('Добро пожаловать в Fit Life!')
    # Спрашиваем имя, приобразуем к верхнему регистру
    USER_NAME = input('Как мы можем к вам обращаться? ').title()
    while True:
        try:
            USER_AGE = int(input('Сколько вам полных лет?'
                                 '(укажите целое число) '))
            break
        except ValueError:
            print('Похоже вы ввели возраст не в том формате, \n'
                  'Нужно указать целое число, например: 18 \n')
    while True:
        try:
            # 2. Сбор данных
            user_weight = input('Ваш вес (в килограммах, напимер 80.5): ')
            user_weight = float(user_weight.replace(',', '.'))

            user_height = input('Ваш рост (в метрах, например 1.75): ')
            user_height = float(user_height.replace(',', '.'))
            break
        except ValueError:
            print('Похоже вы ввели данные не в том формате, \n'
                  'Нужно указать число, можно с точностью до сотых.'
                  'Например: 123.12 \n')

    bmi, water_needed_liters = calculate_bmi(user_weight, user_height)
    # 4. Вывод красивого результата
    print(
        f'\nОтчет для пользователя: {USER_NAME} ({USER_AGE} г.) \n'
        f'Ваш Индекс массы тела: {bmi} \n'
        f'Норма воды в день (в литрах): {water_needed_liters} л. в день \n'
        'Расчет окончен. Будьте здоровы! \n')
