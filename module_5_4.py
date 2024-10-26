# ЗАДАНИЕ ПО ТЕМЕ "Различие атрибутов класса и экземпляра"

class House:
    houses_history = []

    # Метод, который вызывается перед созданием объекта класса.
    # Он создает и возвращает объект класса
    def __new__(cls, *args, **kwargs):
        # Добавление в список houses_history значения первого аргумента (name) объекта класса
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    # Метод, который вызывается сразу после создания объекта класса.
    # Методу передаются аргументы, с которыми был создан объект
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor >= 1 and new_floor <= self.number_of_floors:
            for i in range(new_floor):
                print(i + 1)
        else:
            print("Такого этажа не существует")

    # Метод, позволяющий применять функцию len для объекта класса
    def __len__(self):
        return self.number_of_floors

    # Метод для отображения информации об объекте класса для пользователей,
    # например, для функций print, str
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    # Метод, позволяющий применять оператор сравнения РАВНО для двух объектов класса
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    # Метод, позволяющий применять оператор сравнения НЕ РАВНО для двух объектов класса
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return False

    # Метод, позволяющий применять оператор сравнения БОЛЬШЕ для двух объектов класса
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    # Метод, позволяющий применять оператор сравнения МЕНЬШЕ для двух объектов класса
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    # Метод, позволяющий применять оператор сравнения БОЛЬШЕ ИЛИ РАВНО для двух объектов класса
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    # Метод, позволяющий применять оператор сравнения МЕНЬШЕ ИЛИ РАВНО для двух объектов класса
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    # Метод, позволяющий применять оператор СЛОЖЕНИЯ,
    # когда объект класса находится СЛЕВА от знака ПЛЮС (obj + a)
    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        raise TypeError("Сложение возможно только с целым числом")

    # Метод, позволяющий применять оператор СЛОЖЕНИЯ,
    # когда объект класса находится СПРАВА от знака ПЛЮС (a + obj)
    def __radd__(self, value):
        return self.__add__(value)

    # Метод, позволяющий применять оператор СЛОЖЕНИЯ
    # c изменением объекта класса (obj += a ==> obj = obj + a)
    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        raise TypeError("Сложение возможно только с целым числом")

    # Метод, который вызывается непосредственно перед удалением объекта класса
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
