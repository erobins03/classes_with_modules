import module
from module import say_hello
from person import Person
from teacher import Teacher
from course import Course

if __name__ == '__main__':
    # print(module.API_KEY)
    # say_hello()
    # module.say_hello()

    # a_person = Person("Fred Smith")
    # print(a_person.name)
    hcde_teacher = Teacher("Adrian")
    hcde_class = Course("HCDE 310", hcde_teacher)
    print(hcde_class.teacher.name)
    for course in hcde_teacher.courses_taught:
        print(course.name)
    print(f"Teacher: {hcde_teacher.name} is teaching {hcde_teacher.courses_taught[0].name}")