num = 5
print(num + 5)

print(num.__add__(6))

# src/distance.py

# class Distance:
#     def __init__(self, x=None, y=None):
#         self.ft = x
#         self.inch = y

#     def __add__(self, x):
#         temp = Distance()
#         temp.ft = self.ft + x.ft
#         temp.inch = self.inch + x.inch
#         if temp.inch >= 12:
#             temp.ft += 1
#             temp.inch -= 12
#             return temp

#     def __str__(self):
#         return 'ft:' + str(self.ft) + ' in:' + str(self.inch)


# d1 = Distance(3, 10)
# d2 = Distance(4, 4)
# print("d1= {} d2={}".format(d1, d2))
# d3 = d1 + d2
# print(d3)

# src/distance.py

class Distance:
    def __init__(self, x=None, y=None):
        self.ft = x
        self.inch = y

    def __add__(self, x):
        temp = Distance()
        temp.ft = self.ft + x.ft
        temp.inch = self.inch + x.inch
        if temp.inch >= 12:
            temp.ft += 1
            temp.inch -= 12
            return temp

    def __ge__(self, x):
        val1 = self.ft * 12 + self.inch
        val2 = x.ft * 12 + x.inch
        if val1 >= val2:
            return True
        else:
            return False

    def __str__(self):
        return 'ft:' + str(self.ft) + ' in:' + str(self.inch)


d1 = Distance(3, 10)
d2 = Distance(4, 4)
print("d1= {} d2={}".format(d1, d2), "line 62" "")
d3 = d1 + d2
print(d3)
print(d1 >= d2)

class Student:
    __school_name = 'General Assembly'

    def __init__(self, name, age):
        self.__name = name  # private instance attribute
        self.__salary = age  # private instance attribute

    def __display(self):  # private method
        print('This is private method.')
    
    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    @classmethod
    def test_class(self):
        return Student.__school_name


student = Student("Suresh", 22)
# print(student.__school_name)
# print(student.__name)
# print(student.__display)
# print(Student.__school_name, "line 82")

# print(student.test_class())
# print(Student.test_class())
print(student.gather_requirement("TEST"))