import random
print('Добро пожаловать в игру')
dificult = input('Выбери сложность(1,2,3,4(Свой режим)):')
check = '0' #Данные от пользователя
min_range = 0 #Минимальное число генерации
max_range = 0 #Максимальное число генерации

if dificult == '1': #Настройки сложности №1
    count = 5
    min_range = 1
    max_range = 11
elif dificult == '2': #Настройки сложности №2
    count = 5
    min_range = 1
    max_range = 21
elif dificult == '3': #Настройки сложности №3
    count = 5
    min_range = 1
    max_range = 31
elif dificult == '4': #Настройки сложности №4
    count = int(input('Введите количество попыток:'))
    min_range = int(input('Введите минимальное число:'))
    max_range = int(input('Введите максимальное число:')) + 1
else:
    print ('Вы ввели неверные данные') #Отлавливаем ошибку

number = random.randrange(min_range,max_range) #Генерируем число
print(f'Я загадал число от {min_range} до {max_range - 1}.\nУ вас есть {count} попыток.')

while count > 0: #Основной цикл
    check = input('Введите число:')
    if int(check) > number:
        print('Ваше число больше')
    elif int(check) < number:
        print('Моё число больше')
    elif int(check) == number:
        print('Вы угадали моё число !')
        count = 1
        break
    count -= 1
    print(f'У вас осталось {count} попыток.')