import math
print('''Вам необходимо ввести количество критериев для сравнения (целое, положительное число)
Далее введите весовые коэффициенты (От 1 до 9):
1 - равная важность
3 - умеренное превосходство одного над другим
5 - существенное превосходство одного над другим
7 - значительное превосходство одного над другим
9 - очень сильное превосходство одного над другим
2, 4, 6, 8 - соответствующие промежуточные значения''')

while True:
    try:
        n = abs(int(input('\nВведите целое, положительное число равное количеству критериев: ')))
    except ValueError:
        print('Введено некорректное значение. Попробуйте снова')
        continue
    if n == 0:
        print('Введен ноль. Попробуйте снова.')
        continue
    elif n == 1:
        print('Критериев должно быть не менее двух. \nКоэффициент у единственного критерия будет равен 1\n')
        break

    t = [[1.0] * n for i in range(n)] 

    try:
        for i in range(n - 1):
            for j in range(i + 1, n):
                t[i][j] = float(input(f'Насколько критерий {i+1} важнее критерия {j+1}: '))
                t[j][i] = 1 / t[i][j]
                if t[i][j] > 1:
                    t[i][j] = float(math.floor(t[i][j]))
                else:
                    t[i][j] = float(math.floor(t[i][j] * 100)/100)
                if t[j][i] > 1:
                    t[j][i] = float(math.floor(t[j][i]))
                else:
                    t[j][i] = float(math.floor(t[j][i] * 100)/100)
    except ValueError:
        print('Введено некорректное значение. Попробуйте снова.')
        continue
    except ZeroDivisionError:
        print('Введен ноль. Попробуйте снова.')
        continue

    spisoksum = list() 

    for i in range(n):
        s = 0
        for j in range(n):
            s += t[i][j]
        spisoksum.append(s)

    spisokkaf = list() 

    for i in range(n):
        spisokkaf.append(math.floor((spisoksum[i]/sum(spisoksum)) * 100) / 100)

    spisokkaff = round(sum(spisokkaf), 2) 

    while spisokkaff > 1:
        for i in range(n):
            if spisokkaf[i] == min(spisokkaf):
                spisokkaf[i] -= 0.01
        spisokkaff = round(sum(spisokkaf), 2)
    while spisokkaff < 1:
        for i in range(n):
            if spisokkaf[i] == max(spisokkaf):
                spisokkaf[i] += 0.01
        spisokkaff = round(sum(spisokkaf), 2)

    print('\nТаблица попарного сравнения')
    for i in range(n):
        for j in range(n):
            print(t[i][j], end=' \t')
        print('')

    print('\nКоэффициенты')
    for i in range(n):
        print(f'Коэффициент критерия {i+1}: {round(spisokkaf[i], 2)}')
    break