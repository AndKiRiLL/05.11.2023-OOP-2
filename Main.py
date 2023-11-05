# Задание 1

# import random
# class MusicAlbum:
#
#     def __init__(self, title, artist, release_year, genre, tracklist):
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#         self.genre = genre
#         self.tracklist = tracklist
#
#     def get_info(self):
#         print(f'''
# Название: {self.title}
# Исполнитель: {self.artist}
# Год выпуска: {self.release_year}
# Жанр: {self.genre}
# Список треков {self.tracklist}
# ''')
#
#     def play_random_track(self):
#         return random.choice(self.tracklist)
#
# album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
#                     ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
#                      "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
#                      "Hallomann"])
#
# album4.get_info()
# print(album4.play_random_track())


# Задание 2
'''
class Student:
    def __init__(self, name, age, grade, scores):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def info(self):
        print('Имя', self.name)
        print('Возраст', self.age)
        print('Класс', self.grade)
        print('Оценки', self.scores)

    def average_score(self):
        return sum(self.scores) / len(self.scores)

student2 = Student("Егор Данилов", 12, '58', [5, 4, 4, 5])
student2.info()
print('Средний бал', student2.average_score())
'''

# Задание 3
'''
class Recipe:
    def __init__(self, name, recipe_list):
        self.name = name
        self.recipe_list = recipe_list

    def print_ingredients(self):
        print(f'Ингредиенты для {self.name}:')
        for i in self.recipe_list:
            print(f'- {i}')

    def cook(self):
        print(f'Сегодня мы готовим {self.name}.')
        print(f'Выполняем инструкцию по приготовлению блюда {self.name}...')
        print(f'Блюдо {self.name} готово!')


spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
spaghetti.print_ingredients()
spaghetti.cook()
print()
cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
cake.print_ingredients()
cake.cook()
'''

# Задание 4
'''
class Publisher:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        print(f'Название компании {self.name}')
        print(f'Компания распологается {self.location}')

    def publish(self, message):
        self.message = message
        print(f'Готовим "{self.message}" к публикации в {self.name} ({self.location})')

class BookPublisher(Publisher):

    def __init__(self, name, location, num_authors):
        super().__init__(name, location)
        self.num_authors = num_authors

    def publish(self, name_book, book_author):
        self.name_book = name_book
        self.book_author = book_author
        print(f"Передаём рукопись '{self.name_book}', написанную автором {self.book_author} в издательство {self.name} ({self.location})")

class NewspaperPublisher(Publisher):

    def __init__(self, name, location, num_pages):
        super().__init__(name, location)
        self.num_pages = num_pages

    def publish(self, message):
        self.message = message
        print(f'Печатаем свежий номер со статьёй "{self.message}" на главной странице в издательстве {self.name} ({self.location})')


publisher = Publisher("АБВГД Пресс", "Москва")
publisher.publish("Справочник писателя")

book_publisher = BookPublisher("Важные Книги", "Самара", 52)
book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")

newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
newspaper_publisher.publish("Новая версия Midjourney будет платной")
'''

# Задание 5
'''
class BankAccount:

    def __init__(self, balance=0, interest_rate=0, transactions=[]):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = transactions

    def deposit(self, amount):
        self.amount = amount
        print(f'Внесение наличных на счёт: {self.amount}')
        self.balance += self.amount
        print(f'На вашем счету: {self.balance}\n')
        self.transactions.append(f'Внесение наличных на счёт: {self.amount}')

    def withdraw(self, amount):
        self.amount = amount
        print(f'Снятие наличных: {self.amount}')
        self.balance -= self.amount
        print(f'На вашем счету: {self.balance}\n')
        self.transactions.append(f'Снятие наличных: {self.amount}')

    def add_interest(self):
        print(f'Начислены проценты по вкладу: {self.balance * 0.05}')
        self.balance += self.balance * 0.05
        print(f'На вашем счету: {int(self.balance)}\n')
        self.transactions.append(f'Начислены проценты по вкладу: {self.balance * 0.05}')

    def history(self):
        print('История операций:')
        for i in range(0, len(self.transactions)):
            print(f'{i+1}: {self.transactions[i]}')


account = BankAccount(100000, 0.05)

account.deposit(15000)
account.withdraw(7500)
account.add_interest()
account.history()
'''

# Задание 6
'''
class Employee:

    def __init__(self, name='', age=0, salary=0, bonus=0):
        self.name = name
        self.age = age
        self.salary = salary
        self.bonus = bonus

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_salary(self):
        return self.salary

    def set_bonus(self, bonus):
        self.bonus = bonus

    def get_bonus(self):
        return self.bonus

    def get_total_salary(self):
        return self.salary + self.bonus

employee = Employee("Марина Арефьева", 30, 90000)

employee.set_bonus(15000)

print("Имя:", employee.get_name())
print("Возраст:", employee.get_age())
print("Зарплата:", employee.get_salary())
print("Бонус:", employee.get_bonus())
print("Итого начислено:", employee.get_total_salary())
'''

# Задание 7
'''
class Animal:
    def __init__(self, name='', species='', legs=0):
        self.name = name
        self.species = species
        self.legs = legs

    def voice(self):
        print(f'{self.name} подаёт голос')

    def move(self):
        print(f'{self.name} дёргает хвостом')

class Dog(Animal):

    def __init__(self, name, breed='', legs=0):
        super().__init__(name)
        self.breed = breed
        self.legs = legs

    def bark(self):
        print(f'{self.breed} {self.name} лает')


class Bird(Animal):

    def __init__(self, name, species='', legs=0, wingspan=0):
        super().__init__(name)
        self.species = species
        self.legs = legs
        self.wingspan = wingspan

    def fly(self):
        print(f'{self.species} {self.name} летает')


dog = Dog('Геральт', "доберман", 4)
bird = Bird('Вася', "попугай", 2)

dog.voice()
bird.voice()
dog.move()
bird.move()
dog.bark()
bird.fly()
'''

# Задание 8
'''
class Shape:

    def __init__(self, name='', color=''):
        self.name = name
        self.color = color

    def describe(self):
        print(f'Это геометрическая фигура, цвет - {self.color}')

class Circle(Shape):

    def __init__(self, color, radius=0):
        self.color = color
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def describe(self):
        super().describe()
        print(f'Это окружность. Радиус - {self.radius} см, цвет - {self.color}.')

class Rectangle(Shape):

    def __init__(self, color, lenght, width):
        self.color = color
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width

    def describe(self):
        super().describe()
        print(f'Это {self.color} прямоугольник. Длина - {self.lenght} см , ширина - {self.width} см.')


class Triangle(Shape):

    def __init__(self, color, base, height):
        self.color = color
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def describe(self):
        super().describe()
        print(f'Это {self.color} треугольник с основание {self.base} см и высотой {self.height} см.')


circle = Circle("красный", 5)
rectangle = Rectangle("синий", 3, 4)
triangle = Triangle("фиолетовый", 6, 8)

circle.describe()
rectangle.describe()
triangle.describe()
print(f"Площадь треугольника {triangle.area()}, окружности {circle.area()}, прямоугольника {rectangle.area()} см.")
'''


# Задание 9
'''
class Candy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

class Chocolate(Candy):
        def __init__(self, name, price, weight, cocoa_percentage, chocolate_type):
            super().__init__(name, price, weight)
            self.cocoa_percentage = cocoa_percentage
            self.chocolate_type = chocolate_type

class Gummy(Candy):
        def __init__(self, name, price, weight, flavor, shape):
            super().__init__(name, price, weight)
            self.flavor = flavor
            self.shape = shape

class HardCandy(Candy):
        def __init__(self, name, price, weight, flavor, filled):
            super().__init__(name, price, weight)
            self.flavor = flavor
            self.filled = filled

chocolate = Chocolate("Швейцарские луга", 325.50, 220, 40, "молочный")
gummy = Gummy("Жуй-жуй", 76.50, 50, "вишня", "медведь")
hard_candy = HardCandy("Crazy Фрукт", 35.50, 25, "манго", True)

print("Шоколадные конфеты:")
print(f"Название конфет: {chocolate.name}")
print(f"Стоимость: {chocolate.price} руб")
print(f"Вес брутто: {chocolate.weight} г")
print(f"Процент содержания какао: {chocolate.cocoa_percentage}")
print(f"Тип шоколада: {chocolate.chocolate_type}")
print("\nМармелад жевательный:")
print(f"Название конфет: {gummy.name}")
print(f"Стоимость: {gummy.price} руб")
print(f"Вес брутто: {gummy.weight} г")
print(f"Вкус: {gummy.flavor}")
print(f"Форма: {gummy.shape}")
print("\nФруктовые леденцы:")
print(f"Название конфет: {hard_candy.name}")
print(f"Стоимость: {hard_candy.price} руб")
print(f"Вес брутто: {hard_candy.weight} г")
print(f"Вкус: {hard_candy.flavor}")
print(f"Начинка: {hard_candy.filled}")
'''

# Задание 10
'''
class Soldier:
    def __init__(self, name='', rank='', service_number=0):
        self.name = name
        self.rank = rank
        self.service_number = service_number
        print(f"Создан новый игровой персонаж типа Soldier с атрибутами:\n{{'name':'{self.name}', '_Soldier__rank':'{self.rank}', '_Soldier__service_number':'{self.service_number}'}}")

    def get_rank(self):
        print(f'Персонаж {self.name} имеет звание {self.rank}')

    def promote(self):
        print(f'{self.name} повышен в звании, он теперь ефрейтор')

    def demote(self):
        print(f'{self.name} понижен в звании, он теперь рядовой')

soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")
soldier1.get_rank()
soldier1.promote()
soldier1.demote()
'''