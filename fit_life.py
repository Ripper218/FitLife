# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30  # норма воды в миллилитрах на 1 кг
ML_IN_LITERS = 1000  # Константа для перевода миллилитров в литры

# 1. Знакомство с пользователем
print('Добро пожаловать в Fit Life!')
# Спрашиваем имя, приобразуем к верхнему регистру
USER_NAME = input('Как мы можем к вам обращаться? ').title()
USER_AGE = int(input('Сколько вам лет? '))

# 2. Сбор данных
user_weight = float(input('Ваш вес (в килограммах, напимер 80.5) '))
user_height = float(input('Ваш рост (в метрах, например 1.75) '))


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# на входе - рост и вес
# на выходе - индекс массы тела с одним знаком после запятой
def _calculate_bmi(user_weight, user_height):
    bmi = round(user_weight / (user_height ** 2), 1)
    return bmi


# Подсчет воды: вес * 30 мл(сразу делим на 1000 чтоб перевести в литры)
water_needed_liters = round(user_weight * WATER_PER_KG / ML_IN_LITERS, 1)
bmi = _calculate_bmi(user_weight, user_height)

# Обрамление для отчета
Framing = '=' * 30

# 4. Вывод красивого результата
print(Framing)
print(f'Отчет для пользователя: {USER_NAME} ({USER_AGE} г.)')
print(f'Ваш Индекс массы тела: {bmi}')
print(f'Норма воды в день (в литрах): {water_needed_liters} л. в день')
print(Framing)
print("Расчет окончен. Будьте здоровы!")
