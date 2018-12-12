
from No import No
from AVL import AVL
import os

run = True
biblioteca = AVL()

# Menu com as opções
# Condição para saber se a função está sendo executada dentro de execute()
def menu(cond=False):
    if cond:
        input('\nDigite qualquer coisa para continuar...')
    # Limpar a tela
    os.system('cls' if os.name=='nt' else 'clear')
    print('--- Biblioteca AVL ---\n')
    print('Menu:')
    print('\t(1) Inserir livro')
    print('\t(2) Buscar livro por título')
    print('\t(3) Buscar livros por ano')
    print('\t(4) Remover livro')
    print('\t(5) Listar livros em ordem alfabética')
    print('\t(6) Altura da árvore')
    print('\t(7) Sair do programa\n')

# Execução das opções
def execute():
    global run

    option = input('Digite a opção: ')

    # Inserir livro
    if option == '1':
        title = input('\nDigite o título do livro: ')
        year = int(input('Digite o ano do livro: '))
        biblioteca.insertBook(title, year)
        menu(True)
    
    # Buscar livro por título
    elif option == '2':
        title = input('\nDigite o título do livro: ')
        biblioteca.searchBook(title)
        menu(True)
    
    # Buscar livros por ano
    elif option == '3':
        year = int(input('\nDigite o ano a ser buscado: '))
        biblioteca.searchYear(year)
        menu(True)

    # Remover livro
    elif option == '4':
        title = input('\nDigite o título do livro: ')
        biblioteca.removeBook(title)
        menu(True)

    # Listar livros em ordem alfabética
    elif option == '5':
        biblioteca.listBook()
        menu(True)

    # Altura da árvore (raiz = 0)
    elif option == '6':
        biblioteca.getHeight()
        menu(True)

    # Sair do programa
    elif option == '7':
        print('\nAté mais!')
        run = False

menu()

while run:
    execute()