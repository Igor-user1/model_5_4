class House:
    houses_history = []

    def __new__(cls, name, number_of_floors):
        cls.houses_history.append(name)
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if isinstance(new_floor, int):
            if new_floor >= 1:
                if new_floor <= self.number_of_floors:
                    for i in range(new_floor + 1):
                        if i == 0:
                            continue
                        print(i)
                else:
                    return print('Такого этажа не существует')
            else:
                return print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other

    def __lt__(self, other):
        return self.number_of_floors < other

    def __le__(self, other):
        return self.number_of_floors <= other

    def __gt__(self, other):
        return self.number_of_floors > other

    def __ge__(self, other):
        return self.number_of_floors >= other

    def __ne__(self, other):
        return self.number_of_floors != other

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        f'Название: {self.name}, количество этажей: {self.number_of_floors}'
        return self

    def __radd__(self, value):
        self.number_of_floors = value + self.number_of_floors
        f'Название: {self.name}, количество этажей: {self.number_of_floors}'
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        f'Название: {self.name}, количество этажей: {self.number_of_floors}'
        return self

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __del__(self):
        print(f"{self.name} снесен, но он останется в истории")


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
