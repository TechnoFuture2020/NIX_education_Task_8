"""
    Task_8:
Есть список из случайных чисел и строк.
Создайте цикл, итерирующийся до тех пор, пока не встретится число "777".
Если в течении 100 попыток число не будет найдено — остановить цикл и вызвать ошибку с соответсвующим сообщением.
"""


def get_number_from_random_list(n, search_symb):  # n - максимальное число итераций для поиска символа search_symb
    import random
    random_list = [str(random.randint(0, 778)) for i in range(51, 101)] + [random.randint(0, 778) for i in range(51, 101)]
    random.shuffle(random_list)  # Создаём список случайных чисел и строк для тестирования
    i = 0
    print(random_list)

    while i < n:
        if random_list[i] == search_symb:
            return 'Everything is fine. Search_symb is in the list and equals - ' + str(random_list[i]) + ' with index ' + str(i)  # если нашли искомый символ то останавливаем цикл
        elif i == n - 1 and random_list[i] != search_symb:  # если дошли до конца диапазона поиска создаём исключение и вызываем его
            try:
                raise Exception('Error. Digit 777 not in random_list.')
            except Exception as e:
                return str(e)
        i += 1


print(get_number_from_random_list(100, 777))
