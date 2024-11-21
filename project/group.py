from student import Student

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if isinstance(student, Student):
            self.group.add(student)
        else:
            raise ValueError("Тільки екземпляри класу Student можна додати до групи")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        students = "\n".join(str(student) for student in self.group)
        return f"Group {self.number}:\n{students}"