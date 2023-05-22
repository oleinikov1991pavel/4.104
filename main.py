number = int(input('Введите номер дня\n'))

if number % 7 == 1:
    print('понедельник')
    if number % 7 == 2:
        print('вторник')
    if number % 7 == 3:
        print('среда')
    if number % 7 == 4:
        print('четверг')
    if number % 7 == 5:
        print('пятница')
    if number % 7 == 6:
        print('суббота')
    if number % 7 == 0:
        print('воскресенье')
