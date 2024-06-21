from app import app, db
from models import Aluno, Bibliotecario, Livro

def populate_db():
    # Adicionando Alunos
    alunos = [
        Aluno(nome_completo='João da Silva', apelido='João', matricula='2021001', celular='999999999', email='joao@example.com'),
        Aluno(nome_completo='Maria Souza', apelido='Maria', matricula='2021002', celular='888888888', email='maria@example.com'),
        Aluno(nome_completo='Carlos Pereira', apelido='Carlos', matricula='2021003', celular='777777777', email='carlos@example.com')
    ]

    for aluno in alunos:
        db.session.add(aluno)

    # Adicionando Bibliotecários
    bibliotecarios = [
        Bibliotecario(nome_completo='Ana Silva', apelido='Ana', email='ana@example.com'),
        Bibliotecario(nome_completo='Pedro Oliveira', apelido='Pedro', email='pedro@example.com')
    ]

    for bibliotecario in bibliotecarios:
        db.session.add(bibliotecario)

    # Adicionando Livros
    livros = [
        Livro(titulo='Introdução à Programação', autor='John Doe', categoria='Programação', resumo='Livro de introdução à programação.', ano_publicacao=2020, qt_total=5, qt_emprestada=0),
        Livro(titulo='Algoritmos Avançados', autor='Jane Doe', categoria='Programação', resumo='Livro sobre algoritmos avançados.', ano_publicacao=2019, qt_total=3, qt_emprestada=0),
        Livro(titulo='Banco de Dados', autor='Alice Silva', categoria='Banco de Dados', resumo='Livro sobre banco de dados.', ano_publicacao=2018, qt_total=4, qt_emprestada=0)
    ]

    for livro in livros:
        db.session.add(livro)

    # Commit dos dados no banco de dados
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        populate_db()
        print('Banco de dados populado com sucesso!')
