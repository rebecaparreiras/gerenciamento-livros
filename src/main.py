from cadastro import cadastrar_livro
from consulta import consultar_livro
from remocao import remover_livro
from persistencia import carregar_livros, salvar_livros

def main():
    print('Bem-vindo à Livraria da Rebeca Parreiras')
    lista_livro = carregar_livros()

    while True:
        print('MENU PRINCIPAL')
        print('1 - Cadastrar Livro')
        print('2 - Consultar Livro(s)')
        print('3 - Remover Livro')
        print('4 - Sair')
        opcao = input('>> ')

        if opcao == '1':
            cadastrar_livro(lista_livro)
            salvar_livros(lista_livro)
        elif opcao == '2':
            consultar_livro(lista_livro)
        elif opcao == '3':
            remover_livro(lista_livro)
            salvar_livros(lista_livro)
        elif opcao == '4':
            print('Encerrando o programa...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()
