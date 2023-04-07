"""
Задание 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""


# рекурсивная функция поиска суммы четных и нечетных чисел
def reverse_num(num):
    # Проверяем базовое значение, возвращаем цифру
    if num // 10 == 0:
        return num
        # В ином случае прибавляем цифру и запускаем рекурсию
    else:
        return str(num % 10) + str(reverse_num(num // 10))


try:  # Валидация введенного числа
    number = int(input("Введите целое число: "))
except ValueError:
    print("Введено неверное число")
else:
    rev_num = reverse_num(number)
    print("перевернутое число {} ".format(rev_num))