import random

from models import SessionLocal, Student, Course, init_db


FIRST_NAMES = [
    "Іван Коваленко", "Олена Шевченко", "Петро Бондаренко", "Марія Ткаченко",
    "Андрій Мельник", "Софія Кравченко", "Дмитро Олійник", "Анна Поліщук",
    "Сергій Гриценко", "Наталія Савченко", "Олександр Руденко", "Юлія Марченко",
    "Максим Левченко", "Тетяна Захарченко", "Артем Лисенко", "Вікторія Павленко",
    "Назар Карпенко", "Оксана Романенко", "Богдан Тимошенко", "Ірина Василенко",
]

# Курси морської академії
COURSE_TITLES = [
    "Навігація та лоція",
    "Судноводіння",
    "Морське право",
    "Будова судна",
    "Англійська для моряків (Maritime English)",
]


def seed_data() -> None:
    init_db()
    session = SessionLocal()

    session.query(Student).delete()
    session.query(Course).delete()
    session.commit()


    courses = [Course(title=title) for title in COURSE_TITLES]
    session.add_all(courses)
    session.commit()
    print(f"Створено {len(courses)} курсів")


    students = []
    for name in FIRST_NAMES:
        student = Student(name=name)
        student.courses = random.sample(courses, random.randint(1, 3))
        students.append(student)

    session.add_all(students)
    session.commit()
    print(f"Створено {len(students)} курсантів з рандомним розподілом по курсах")

    session.close()


if __name__ == "__main__":
    seed_data()