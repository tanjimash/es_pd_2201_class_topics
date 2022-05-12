class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        # print(f"Name: {self.name}; Age: {self.age}, Email:{self.email}")
    
    # def info(self):
    #     print(f"Name: {self.name}")
    #     print(f"Age: {self.age}")
    #     print(f"Email: {self.email}")
    



# create object
# person_obj = Person('Jakir', '24', 'jakir@gmail.com')


class Student(Person):
    pass

stud_obj = Student('Jakir',  24, 'jakir@gmail.com')
# jodi account successfully create korte pare, then call the "greet_after_reg()" func.
stud_obj.info()


class Teacher(Person):
    pass

teacher_obj = Teacher('Neela',  26, 'neela@gmail.com')
teacher_obj.info()


class Admin(Person):
    pass


admin_obj = Admin("Rabiul", 45, 'rabiul@gmail.com')
admin_obj.info()