class Student:
    def __init__(self, name, marks):
        self.name = name
        self. marks = marks

    def is_passed(self) -> bool:
        result = self.marks > 50
        return result

    
student1 = Student("Adam", 60)
student2 = Student('Ola', 40)
print(Student.is_passed(student1))
print(Student.is_passed(student2))
