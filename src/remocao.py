def remover_livro(lista_livro):
    id_remover = int(input('Digite o ID do livro a ser removido: '))
    for livro in lista_livro:
        if livro['id'] == id_remover:
            lista_livro.remove(livro)
            print('Livro removido com sucesso!')
            return
    print('ID não encontrado.')
