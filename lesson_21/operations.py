from models import SessionLocal, Student, Course


def add_student_to_course(student_name: str, course_title: str) -> None:
    session = SessionLocal()

    course = session.query(Course).filter(Course.title == course_title).first()
    if course is None:
        print(f"Курс '{course_title}' не знайдено")
        session.close()
        return

    student = Student(name=student_name)
    student.courses.append(course)

    session.add(student)
    session.commit()
    print(f"Курсанта '{student_name}' додано на курс '{course_title}'")

    session.close()


def get_students_by_course(course_title: str) -> None:
    session = SessionLocal()

    course = session.query(Course).filter(Course.title == course_title).first()
    if course is None:
        print(f"Курс '{course_title}' не знайдено")
        session.close()
        return

    print(f"\n Курсанти на курсі '{course_title}':")
    for student in course.students:
        print(f"   - {student.name}")

    session.close()


def get_courses_by_student(student_name: str) -> None:
    session = SessionLocal()

    student = session.query(Student).filter(Student.name == student_name).first()
    if student is None:
        print(f"Курсанта '{student_name}' не знайдено")
        session.close()
        return

    print(f"\n Курси курсанта '{student_name}':")
    for course in student.courses:
        print(f"   - {course.title}")

    session.close()


def update_student_name(old_name: str, new_name: str) -> None:
    session = SessionLocal()

    student = session.query(Student).filter(Student.name == old_name).first()
    if student is None:
        print(f"Курсанта '{old_name}' не знайдено")
        session.close()
        return

    student.name = new_name
    session.commit()
    print(f"Ім'я змінено: '{old_name}' → '{new_name}'")

    session.close()


def delete_student(student_name: str) -> None:

    session = SessionLocal()

    student = session.query(Student).filter(Student.name == student_name).first()
    if student is None:
        print(f"Курсанта '{student_name}' не знайдено")
        session.close()
        return

    session.delete(student)
    session.commit()
    print(f"Курсанта '{student_name}' видалено")

    session.close()


if __name__ == "__main__":

    add_student_to_course("Олег Дубенко", "Навігація та лоція")

    get_students_by_course("Навігація та лоція")
    get_courses_by_student("Олег Дубенко")

    update_student_name("Олег Дубенко", "Олег Дубенко-Морський")
    get_courses_by_student("Олег Дубенко-Морський")

    delete_student("Олег Дубенко-Морський")