# Задача 1 (Знакомство с декораторами)

"""
Дополнить декоратор сache поддержкой max_limit
"""


from datetime import datetime
from functools import wraps
from time import sleep


# ДЕКОРАТОР ЗАМЕРА ВРЕМЕНИ РАБОТЫ ФУНКЦИИ
def measure_time(func):
    def wrapper(*args, **kwargs):
        # start - cтарт моей программы
        start = datetime.now()
        res = func(*args, **kwargs)
        # Вывожу время работы программы
        print(datetime.now() - start)
        return res
    return wrapper


# ДЕКОРАТОР КЕШИРОВАНИЯ
def cache(max_limit=64):
    def cache_wraps(f):
        @wraps(f)
        def deco(arg):
            firstKey = 0
            # Проверяем есть ли такой ключ в словаре(значение ключей None)
            if arg in deco._cache:
                print('!!!Этот ключ уже присутствует в словаре!!!')
                return deco._cache[arg]

            # Если длина нашего словаря меньше лимита то добавляю ключ в словарь
            if len(deco._cache) < max_limit:
                result = f(arg)
                deco._cache[arg] = result
                # Print для того что бы увидить значения словаря
                print(deco._cache)
                return result

            # А если длина больше, удаляю первый елемент и добавляю новый в конец(что бы не привышать заданый лимит)
            else:
                # Через цикл получаю первый ключ словаря
                for key in deco._cache:
                    firstKey = key
                    break
                # Удаляю этот самый первый ключ из словаря!!!
                del deco._cache[firstKey]
                result = f(arg)
                # Добавляю новый ключ в этот словарь
                deco._cache[arg] = result
                # Print для того что бы убедится что первое значение удаляется и добавляется новое
                print('Тут произошла замена:', deco._cache)
                return result

        deco._cache = {}

        return deco

    return cache_wraps


# ФУНКЦИЯ КОТОРАЯ ПРОИЗВОДИТ ОБРАТНЫЙ ОТСЧЁТ ВРЕМЕНИ В СЕКУНДАХ
@measure_time
# ТУТ Я ВЫСТАВИЛ ЛИМИТ 5 ЧТО БЫ МОЖНО БЫЛО ЛЕГЧЕ ПРОТЕСТИРОВАТЬ ПРОГРАММУ
@cache(max_limit=5)
def foo(n):
    sleep(n)


# ТУТ МЫ ТЕСТИРУЕМ НАШУ ПРОГРАММУ
foo(1)
foo(2)
foo(3)
foo(3)
foo(4)
foo(2)
foo(5)
foo(6)
foo(7)
foo(1)
foo(2)
