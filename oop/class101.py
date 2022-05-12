class Person:
    def __init__(self, x, y):
        print('A new class object is created!')
        self.extra1 = x
        self.extra2 = y

    def greet(self):
        print(f'Hellow {self.extra1}! You\'re age is {self.extra2}')

    def studInfo(self):
        print(f'Student: {self.extra1}; age: {self.extra2}')
    
    def gurdianInfo(self):
        print(f'Gurdian: {self.extra1}; age: {self.extra2}')

    def birthdayWish(self):
        print(f'Birthday Info: {self.extra1}; age: {self.extra2}')
    
    def employeeInfo(self):
        print(f'Employee Info: {self.extra1}; age: {self.extra2}')


    class ChildClass:
        def __init__(self):
            print("Child class is called!")

        def schoolInfo(self, schoolName):
            print("Your school:", schoolName)



xyz = Person('a', 'b')
# xyz.greet()
# xyz.schoolInfo()


x = xyz.ChildClass()
x.schoolInfo("asodiuasodiu")


# class className2(className):
#     def __init__(self):
#         className.__init__()
#         self.greet()

# obj_name2 = className2()

# # # instantiate a class-obj
# obj_name1 = className('asdoiuyasdo', 'asodiuasodiu')
# obj_name2 = className()
# obj_name3 = className()
# obj_name4 = className()

# obj_name1.greet()

# for i in dir(obj_name1):
#     print(i)

# obj_name.greet('Zamil Bhai', 400)   # always passing the name, age of persons

# obj_name.gurdianInfo('Ashik', '24')