# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('file_1.txt', 'r') as f1:
    str_1 = f1.read().rstrip('= 0\n')

with open('file_2.txt', 'r') as f2:
    str_2 = f2.read().rstrip('= 0\n')

list_x = ['x^6', 'x^5', 'x^4', 'x^3', 'x^2', 'x', '']


def delete_character(lst):
    length = len(lst)
    i = 0
    while i < length:
        if lst[i] == '-' or lst[i] == '+':
            lst[i+1] = lst[i] + lst[i+1]
            del lst[i]
            length -= 1
        i += 1
    return lst


def create_new_list(lst):
    list_res = ['0' for _ in range(len(list_x))]
    for i in range(len(list_res)):
        for j in range(len(lst)):
            if 'x' in lst[j]:
                if list_x[i] == lst[j][lst[j].index('x'):]:
                    coeff = lst[j][:lst[j].index('x')]
                    if not coeff.isdigit() and len(coeff) == 1:
                        list_res[i] = coeff + '1'
                    else:
                        list_res[i] = coeff
    if 'x' not in lst[-1]:
        list_res[-1] = lst[-1]
    return list_res


lst_1 = create_new_list(delete_character(str_1.replace('*', '').split()))
lst_2 = create_new_list(delete_character(str_2.replace('*', '').split()))


def get_result(lst1 , lst2):
    res = []
    for i in range(len(lst1)):
        sum_ = int(lst1[i]) + int(lst2[i])
        if str(sum_) != '0':
            if str(sum_)[0] == '-':
                res.append(str('-'))
                res.append(str(sum_)[1:] + list_x[i])
            else:
                res.append(str('+'))
                res.append(str(sum_) + list_x[i])
    if res[0] == '+':
        res.pop(0)
    return ' '.join(res) + ' = 0'


with open('file_sum.txt', 'w') as f:
    f.write(f'{get_result(lst_1, lst_2)}\n')
