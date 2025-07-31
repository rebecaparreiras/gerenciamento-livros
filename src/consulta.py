def consultar_livro(lista_livro):
    while True:
        print('MENU CONSULTAR LIVRO')
        print('1 - Consultar todos os livros')
        print('2 - Consultar livro por id')
        print('3 - Consultar livro(s) por autor')
        print('4 - Retornar')
        opcao = input('>> ')

        if opcao == '1':
            if lista_livro:
                for livro in lista_livro:
                    print(f"\nId: {livro['id']}\nNome: {livro['nome']}\nAutor: {livro['autor']}\nEditora: {livro['editora']}")
            else:
                print('Nenhum livro foi cadastrado.')
        elif opcao == '2':
            id_consulta = int(input('Digite o id do livro: '))
            for livro in lista_livro:
                if livro['id'] == id_consulta:
                    print(f"\nId: {livro['id']}\nNome: {livro['nome']}\nAutor: {livro['autor']}\nEditora: {livro['editora']}")
                    break
            else:
                print('Id não encontrado.')
        elif opcao == '3':
            autor = input('Digite o nome do autor: ')
            encontrados = [l for l in lista_livro if l['autor'] == autor]
            if encontrados:
                for livro in encontrados:
                    print(f"\nId: {livro['id']}\nNome: {livro['nome']}\nAutor: {livro['autor']}\nEditora: {livro['editora']}")
            else:
                print('Autor não encontrado.')
        elif opcao == '4':
            break
        else:
            print('Opção inválida.')
