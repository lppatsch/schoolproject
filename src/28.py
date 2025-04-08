class SimpleSchoolProject:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def remove_student(self, name):
        if name in self.students:
            self.students.remove(name)
