# views/student_view.py
from flask import Blueprint, render_template
from services.student_service import get_students

student_bp = Blueprint('student_view_bp', __name__, url_prefix='/students')

@student_bp.route('/')
def list_students():
    students = get_students()
    return render_template('student_list.html', students=students)
