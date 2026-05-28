from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    courses = relationship(
        "Course", secondary=student_course, back_populates="students"
    )

    def __repr__(self) -> str:
        return f"<Student(id={self.id}, name='{self.name}')>"


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)

    students = relationship(
        "Student", secondary=student_course, back_populates="courses"
    )

    def __repr__(self) -> str:
        return f"<Course(id={self.id}, title='{self.title}')>"


engine = create_engine("sqlite:///school.db", echo=False)
SessionLocal = sessionmaker(bind=engine)


def init_db() -> None:
    Base.metadata.create_all(engine)
    print("Таблиці створено")