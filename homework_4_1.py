import math

print('Программа вычисляет число ПИ c заданной точностью d')
while True:
    number_of_characters = input(
        'Введите точность d (количество знаков после запятой от 1 до 10): '
    )
    if number_of_characters.isdigit():
        if 1 <= int(number_of_characters) <= 10:
            break
    print('Неверно введено число!')
noc = int(number_of_characters)
accuracy = f'{10**(-noc):.{noc}f}'


def get_pi(res='', pi=str(math.pi)):
    for i in range(len(accuracy)):
        res += pi[i]
    return res


print(f'Число ПИ = {get_pi()} при заданной точности {accuracy}.')

