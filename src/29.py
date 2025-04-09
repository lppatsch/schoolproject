class SimpleSchoolProject:
    def __init__(self):
        self.students = []

    def add_student(self, student_name):
        if len(self.students) < 10:
            self.students.append(student_name)
            print(f"Student added: {student_name}")

# Example usage
project = SimpleSchoolProject()
add_student(project, "Alice")
print("Students:")
for student in project.students:
    print(student)
