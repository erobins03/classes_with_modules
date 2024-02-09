class Course:
    def __init__(current_course, name, teacher):
        current_course.teacher = teacher
        current_course.name = name
        teacher.courses_taught.append(current_course)