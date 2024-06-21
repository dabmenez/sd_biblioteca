from flask import render_template
from app import app
import controller

@app.route('/')
def index():
    return controller.index()

@app.route('/livros', methods=['GET', 'POST'])
def livros():
    return controller.gerenciar_livros()

@app.route('/alunos', methods=['GET', 'POST'])
def alunos():
    return controller.gerenciar_alunos()

@app.route('/bibliotecarios', methods=['GET', 'POST'])
def bibliotecarios():
    return controller.gerenciar_bibliotecarios()

@app.route('/emprestimos', methods=['GET', 'POST'])
def emprestimos():
    return controller.gerenciar_emprestimos()

@app.route('/lista_alunos')
def lista_alunos():
    return controller.listar_alunos()

@app.route('/lista_emprestimos')
def lista_emprestimos():
    return controller.listar_emprestimos()

@app.route('/solicitacoes')
def solicitacoes():
    return controller.solicitacoes()

@app.route('/devolucao/<int:id>', methods=['POST'])
def devolucao(id):
    return controller.realizar_devolucao(id)

@app.route('/biblioteca')
def biblioteca():
    return controller.biblioteca()

@app.route('/livro/<int:id>', methods=['GET', 'POST'])
def livro(id):
    return controller.detalhes_livro(id)

@app.route('/meus_emprestimos/<int:aluno_id>')
def meus_emprestimos(aluno_id):
    return controller.meus_emprestimos(aluno_id)
