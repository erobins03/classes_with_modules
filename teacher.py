from person import Person

# subclass of person
class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        self.courses_taught = []

