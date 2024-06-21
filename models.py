from app import db
from datetime import datetime

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(100), nullable=False)
    apelido = db.Column(db.String(50))
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    celular = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True, nullable=False)

class Bibliotecario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(100), nullable=False)
    apelido = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True, nullable=False)

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50))
    resumo = db.Column(db.Text)
    ano_publicacao = db.Column(db.Integer)
    qt_total = db.Column(db.Integer)
    qt_emprestada = db.Column(db.Integer)

class Emprestimo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    livro_id = db.Column(db.Integer, db.ForeignKey('livro.id'), nullable=False)
    data_inicio = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    data_entrega = db.Column(db.DateTime)
    aluno = db.relationship('Aluno', backref=db.backref('emprestimos', lazy=True))
    livro = db.relationship('Livro', backref=db.backref('emprestimos', lazy=True))
