from flask import render_template, request, redirect, url_for, flash
from app import db
from models import Livro, Aluno, Bibliotecario, Emprestimo
from datetime import datetime

def index():
    return render_template('index.html')

def gerenciar_livros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        categoria = request.form['categoria']
        resumo = request.form['resumo']
        ano_publicacao = request.form['ano_publicacao']
        qt_total = request.form['qt_total']
        novo_livro = Livro(titulo=titulo, autor=autor, categoria=categoria, resumo=resumo, ano_publicacao=ano_publicacao, qt_total=qt_total, qt_emprestada=0)
        db.session.add(novo_livro)
        db.session.commit()
        flash('Livro adicionado com sucesso!')
        return redirect(url_for('livros'))
    livros = Livro.query.all()
    return render_template('livros.html', livros=livros)

def gerenciar_alunos():
    if request.method == 'POST':
        nome_completo = request.form['nome_completo']
        apelido = request.form['apelido']
        matricula = request.form['matricula']
        celular = request.form['celular']
        email = request.form['email']
        novo_aluno = Aluno(nome_completo=nome_completo, apelido=apelido, matricula=matricula, celular=celular, email=email)
        db.session.add(novo_aluno)
        db.session.commit()
        flash('Aluno adicionado com sucesso!')
        return redirect(url_for('alunos'))
    alunos = Aluno.query.all()
    return render_template('alunos.html', alunos=alunos)

def gerenciar_bibliotecarios():
    if request.method == 'POST':
        nome_completo = request.form['nome_completo']
        apelido = request.form['apelido']
        email = request.form['email']
        novo_bibliotecario = Bibliotecario(nome_completo=nome_completo, apelido=apelido, email=email)
        db.session.add(novo_bibliotecario)
        db.session.commit()
        flash('Bibliotecário adicionado com sucesso!')
        return redirect(url_for('bibliotecarios'))
    bibliotecarios = Bibliotecario.query.all()
    return render_template('bibliotecarios.html', bibliotecarios=bibliotecarios)

def gerenciar_emprestimos():
    if request.method == 'POST':
        livro_id = request.form['livro_id']
        aluno_id = request.form['aluno_id']
        data_inicio = datetime.now()
        novo_emprestimo = Emprestimo(livro_id=livro_id, aluno_id=aluno_id, data_inicio=data_inicio)
        db.session.add(novo_emprestimo)
        db.session.commit()
        flash('Empréstimo registrado com sucesso!')
        return redirect(url_for('emprestimos'))
    livros = Livro.query.all()
    alunos = Aluno.query.all()
    emprestimos = Emprestimo.query.all()
    return render_template('emprestimos.html', livros=livros, alunos=alunos, emprestimos=emprestimos)

def listar_alunos():
    alunos = Aluno.query.all()
    emprestimos_por_aluno = {aluno.id: Emprestimo.query.filter_by(aluno_id=aluno.id, data_entrega=None).count() for aluno in alunos}
    return render_template('lista_alunos.html', alunos=alunos, emprestimos_por_aluno=emprestimos_por_aluno)

def listar_emprestimos():
    emprestimos = Emprestimo.query.all()
    return render_template('lista_emprestimos.html', emprestimos=emprestimos)

def solicitacoes():
    emprestimos_pendentes = Emprestimo.query.filter_by(data_entrega=None).all()
    return render_template('solicitacoes.html', emprestimos=emprestimos_pendentes)

def realizar_devolucao(id):
    emprestimo = Emprestimo.query.get(id)
    emprestimo.data_entrega = datetime.now()
    db.session.commit()
    flash('Devolução registrada com sucesso!')
    return redirect(url_for('emprestimos'))

def biblioteca():
    livros = Livro.query.all()
    return render_template('biblioteca.html', livros=livros)

def detalhes_livro(id):
    livro = Livro.query.get(id)
    if request.method == 'POST':
        aluno_id = request.form['aluno_id']
        data_inicio = datetime.now()
        novo_emprestimo = Emprestimo(livro_id=id, aluno_id=aluno_id, data_inicio=data_inicio)
        db.session.add(novo_emprestimo)
        db.session.commit()
        flash('Empréstimo solicitado com sucesso!')
        return redirect(url_for('livro', id=id))
    return render_template('livro.html', livro=livro)

def meus_emprestimos(aluno_id):
    emprestimos = Emprestimo.query.filter_by(aluno_id=aluno_id).all()
    return render_template('meus_emprestimos.html', emprestimos=emprestimos)
