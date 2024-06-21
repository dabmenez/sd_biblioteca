import requests

BASE_URL = "http://localhost:5000"

def listar_livros():
    response = requests.get(f"{BASE_URL}/livros")
    if response.status_code == 200:
        livros = response.json()
        for livro in livros:
            print(f"ID: {livro['id']}, Título: {livro['titulo']}, Autor: {livro['autor']}")
    else:
        print("Erro ao obter livros")

def adicionar_livro(titulo, autor, edicao, ano_publicacao):
    payload = {
        "titulo": titulo,
        "autor": autor,
        "edicao": edicao,
        "ano_publicacao": ano_publicacao
    }
    response = requests.post(f"{BASE_URL}/livros", json=payload)
    if response.status_code == 201:
        print("Livro adicionado com sucesso")
    else:
        print("Erro ao adicionar livro")

# Outros métodos para gerenciar alunos e empréstimos...

if __name__ == "__main__":
    listar_livros()
    adicionar_livro("Livro Teste", "Autor Teste", "1ª Edição", 2023)
