from person import Person

# subclass of person
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.courses_enrolled = []
