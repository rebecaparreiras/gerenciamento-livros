def cadastrar_livro(lista_livro):
    id = int(input('Por favor, entre com o ID do livro: '))
    nome = input('Por favor, entre com o nome do livro: ')
    autor = input('Por favor, entre com o autor do livro: ')
    editora = input('Por favor, entre com a editora do livro: ')
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)
