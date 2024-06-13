# controllers/student_controller.py
from flask import Blueprint, request, jsonify
from services.student_service import add_student, get_students, update_student, delete_student

student_bp = Blueprint('student_bp', __name__, url_prefix='/students')

@student_bp.route('/', methods=['POST'])
def add_student_view():
    data = request.get_json()
    new_student = add_student(data)
    return jsonify({'message': 'Student added successfully', 'student': new_student.as_dict()}), 201

@student_bp.route('/', methods=['GET'])
def get_students_view():
    students = get_students()
    return jsonify([student.as_dict() for student in students])

@student_bp.route('/<int:id>', methods=['PUT'])
def update_student_view(id):
    data = request.get_json()
    updated_student = update_student(id, data)
    return jsonify({'message': 'Student updated successfully', 'student': updated_student.as_dict()})

@student_bp.route('/<int:id>', methods=['DELETE'])
def delete_student_view(id):
    deleted_student = delete_student(id)
    return jsonify({'message': 'Student deleted successfully', 'student': deleted_student.as_dict()})
