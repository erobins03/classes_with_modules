class Course:
    def __init__(current_course, name, teacher):
        current_course.teacher = teacher
        current_course.name = name
        current_course.student = []
        teacher.courses_taught.append(current_course)

    def enroll_student(self, student):
        self.student.append(student)
        student.courses_enrolled.append(self)
