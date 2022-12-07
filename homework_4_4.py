from random import randint

print('Программа формирует случайным образом '
      'список коэффициентов (значения от 0 до 100) многочлена '
      'и записывет в файл file.txt многочлен степени k')
while True:
    number = input('Введите натуральную степень k (до 6 степени): ')
    if number.isdigit():
        if 1 <= int(number) <= 6:
            break
    print('Неверно введено число k!')
list_x = ['', 'x', 'x^2', 'x^3', 'x^4', 'x^5', 'x^6']
coeff = [str(randint(-100, 100)) for _ in range(int(number)+1)]

list_cort = list(zip(coeff, list_x))
list_cort.reverse()


def get_polynomial(res=''):
    for i in range(len(list_cort)):
        if list_cort[i][0] != '0':
            res += list_cort[i][0] + '*' + list_cort[i][1] + ' + '
    if res[0] == '-':
        res = '- ' + res[1:]
    return res[:-4].replace('+ -', '- ') + ' = 0'


with open('file.txt', 'a') as f:
    f.write(f'{get_polynomial()}\n')

print(f'В file.txt добавлен многочлен: {get_polynomial()}')
