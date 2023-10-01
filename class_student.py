class Student:
    def __init__(self, name, surname, age, student_id,direction,average_mark):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.direction = direction
        self.average_mark = average_mark

    def update_name(self, new_name):
        self.name = new_name

    def update_surname(self, new_surname):
        self.surname = new_surname

    def update_age(self, new_age):
        self.age = new_age

    def update_student_id(self, new_id):
        self.student_id = new_id
    
    def update_direction(self, new_direction):
        self.student_direction = new_direction

    def update_average_mark(self, new_average_mark):
        self.student_average_mark = new_average_mark

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}, Direction: {self.direction}, Average mark: {self.average_mark}"

student1 = Student("John","Don",20, 12345, "Computer Science", 3.8)
student2 = Student("Janeth","Smith", 22, 67890, "Mathematics", 3.6)

print(student1)
print(student2)

student1.update_age(21)
student2.update_student_id(67891)

print(f"\nUpdated information:\n{student1}")
print(student2)

