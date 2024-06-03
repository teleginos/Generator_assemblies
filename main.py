from Function_factory.function_factory import create_operation
from Lambda_functions import lambda_functions
from Callables.callables import Rect

case = int(input("""1. Фабрика функций
2. Лямбда функции
3. Вызываемые объекты
Выберете номер задачи которую Вам запустить: """))
try:
    match case:
        case 1:
            print("\nЗадача 1: Фабрика Функций\nНаписать функцию, которая возвращает различные математические функции\n"
                  "(например, деление, умножение) в зависимости от переданных аргументов.\n")

            operation = input("Введите операцию(add, subtract): ")
            result_function = create_operation(operation)
            num_1 = int(input("Введите первое число: "))
            num_2 = int(input("Введите второе число: "))

            print(f"Результат выполнения {'сложения' if operation == 'add' else 'вычитания'} = "
                  f"{result_function(num_1, num_2)}")

        case 2:
            print("\nЗадача 2: Лямбда-Функции\nИспользовать лямбда-функцию для реализации простой операции и написать "
                  "такую же функцию с использованием def.\nНапример, возведение числа в квадрат"
                  "(Возводим первое число в степень второго)\n")

            num_1 = int(input("Введите первое число: "))
            num_2 = int(input("Введите второе число: "))

            print(f"Результат работы lambda-функции = {lambda_functions.exponentiation(num_1, num_2)}")
            print(f"Результат работы обычной функции = {lambda_functions.exponentiation_def(num_1, num_2)}")

        case 3:
            print("\nЗадача 3: Вызываемые Объекты\nСоздать класс с Rect c полями a, b которые задаются в __init__ и "
                  "методом __call__, который возвращает площадь прямоугольника, то есть a*b.")

            num_1 = int(input("Введите первую сторону прямоугольника: "))
            num_2 = int(input("Введите вторую сторону прямоугольника: "))

            rect = Rect(num_1, num_2)
            print(f"{rect} имеет площадь = {rect()}")
except (ValueError, TypeError) as exc:
    print("Ошибка! Ведите числа!")
