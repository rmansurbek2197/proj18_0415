# 6-masala
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r**2

print("6:", Circle(5).area())


# 7-masala
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def bonus(self):
        return self.salary * 0.1

print("7:", Employee(1000).bonus())


# 8-masala
class Car:
    def __init__(self, speed):
        self.speed = speed

    def accelerate(self):
        self.speed += 10

car = Car(50)
car.accelerate()
print("8:", car.speed)


# 9-masala
class Person:
    def __init__(self, age):
        self.age = age

    def is_adult(self):
        return self.age >= 18

print("9:", Person(20).is_adult())


# 10-masala
class Temperature:
    def __init__(self, c):
        self.c = c

    def to_f(self):
        return self.c * 9/5 + 32

print("10:", Temperature(25).to_f())
