from flask import Blueprint, request, jsonify
from models.student import Student
from app import db

bp = Blueprint('students', __name__, url_prefix='/students')

@bp.route('/', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(
        name=data['name'],
        registration_number=data['registration_number'],
        course=data['course'],
        email=data['email']
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student added successfully'}), 201

@bp.route('/', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.as_dict() for student in students])

@bp.route('/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    student = Student.query.get_or_404(id)
    student.name = data['name']
    student.registration_number = data['registration_number']
    student.course = data['course']
    student.email = data['email']
    db.session.commit()
    return jsonify({'message': 'Student updated successfully'})

@bp.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully'})
