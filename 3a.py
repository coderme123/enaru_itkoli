class Student:
    def _init_(self, name="prajna", marks=50):
        self.name = name
        self.marks = marks

s1 = Student()
s2 = Student("goutami", 50)

print("name: {} marks: {}".format(s1.name, s1.marks))
print("name: {} marks: {}".format(s2.name, s2.marks))
