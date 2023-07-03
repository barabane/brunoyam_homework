from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text, create_engine, Column, ForeignKey
from sqlalchemy.orm import Session, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db.db')
Base = declarative_base()
session = Session(engine)

class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    surname = Column(String(32), nullable=False)
    age = Column(Integer, nullable=False)
    city = Column(String(50), nullable=False)

class Courses(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    time_start = Column(DateTime, default=datetime.now())
    time_end = Column(DateTime, nullable=False)

class StudentCourses(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    students = relationship('Students')
    courses = relationship('Courses')

c1 = Courses(
    id = 1,
    name = 'python',
    time_start = datetime(21,7,21),
    time_end = datetime(21,8,21)
)

c2 = Courses(
    id = 2,
    name = 'java',
    time_start = datetime(21,7,13),
    time_end = datetime(21,8,16)
)

s1 = Students(
    id = 1,
    name = 'Max',
    surname = 'Brooks',
    age = 24,
    city = 'Spb'
)

s2 = Students(
    id = 2,
    name = 'John',
    surname = 'Stones',
    age = 15,
    city = 'Spb'
)

s3 = Students(
    id = 3,
    name = 'Andy',
    surname = 'Wings',
    age = 45,
    city = 'Manhester'
)

s4 = Students(
    id = 4,
    name = 'Kate',
    surname = 'Brooks',
    age = 34,
    city = 'Spb'
)

sc1 = StudentCourses(
    student_id = 1,
    course_id = 1
)

sc2 = StudentCourses(
    student_id = 2,
    course_id = 1
)

sc3 = StudentCourses(
    student_id = 3,
    course_id = 1
)

sc4 = StudentCourses(
    student_id = 4,
    course_id = 2
)

Base.metadata.create_all(engine)
session.add_all([c1,c2,s1,s2,s3,s4,sc1,sc2,sc3,sc4])
session.commit()

older_30 = session.query(Students).filter(Students.age > 30).all()
python_course = session.query(StudentCourses).filter(StudentCourses.course_id == 1).all()
python_spb = session.query(Students).join(StudentCourses).filter(Students.city == 'Spb', StudentCourses.course_id == 1).all()