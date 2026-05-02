class Student:
    def __init__(self, name, surname, age, marks):
        self.name = name
        self.surname = surname
        self.age = age
        self.marks = marks
    def __str__(self) -> str:
        return f'Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}\nMarks: {self.marks}'
    
student = Student('Dmytro', 'Radchenko', '18', '12, 12, 11')

print(student)
print('---------------------------------')
class Car:
    def __init__(self, brand, model, speed, creation_date) -> None:
        self.brand = brand
        self.model = model
        self.speed = speed
        self.creation_date = creation_date
    def __str__(self) -> str:
        return f'Brand: {self.brand}\nModel: {self.model}\nSpeed: {self.speed}\nCreation date: {self.creation_date}'
    
car = Car('Toyota', 'Camry 3.5', '300', '2021')

print(car)