# services/student_service.py
from models.student import Student
from app import db

def add_student(data):
    new_student = Student(
        name=data['name'],
        registration_number=data['registration_number'],
        course=data['course'],
        email=data['email']
    )
    db.session.add(new_student)
    db.session.commit()
    return new_student

def get_students():
    return Student.query.all()

def update_student(id, data):
    student = Student.query.get_or_404(id)
    student.name = data['name']
    student.registration_number = data['registration_number']
    student.course = data['course']
    student.email = data['email']
    db.session.commit()
    return student

def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return student
