print('Программа выведет список неповторяющихся '
      'элементов исходной последовательности')
while True:
    numbers = input('Введите целые числа через пробел: ').split()
    for number in numbers:
        if not number.isdigit():
            print('Неверно введены числа!')
            break
        continue
    else:
        break

print(list(set(map(int, numbers))))
