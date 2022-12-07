print('Программа составляет список простых множителей натурального числа N')

while True:
    number = input('Задайте натуральное число N: ')
    if number.isdigit():
        break
    print('Неверно введено число!')
number = int(number)

res = []
divider = 2

while divider**2 <= number:
    while not number % divider:
        res.append(divider)
        number //= divider
    divider += 1
if number > 1:
    res.append(number)

print(res)
