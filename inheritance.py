#parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_data(self):
        return 'my name is ' + self.name + ', I am ' + str(self.age) + ' years old'

#child class
class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    #overriding method
    def show_data(self):
        return 'my name is ' + self.name + ', I am ' + str(self.age) + ' years old and my salary is ' + str(self.salary) 

#parent object 
p1 = Person("Dhruv", 19)
print(p1.show_data())

#child object inheriting properties from parent
t1 = Teacher("Dhruv", 19, 20000)
print(t1.show_data())