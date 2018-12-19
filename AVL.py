
from No import No

# Variável para descobrir se foram encontradas ocorrências com aquele ano
# (Para imprimir que não houve)
contYear = 0

class AVL:
    def __init__(self, root=None):
        self.__root = root

    def getRoot(self):
        return self.__root

    def setRoot(self, newRoot):
        self.__root = newRoot

    # Altura da árvore
    def getHeight(self):
        if self.getRoot() == None:
            print('\nÁrvore vazia.')
        else:
            print('\nA árvore possui altura', self.height(self.getRoot()) - 1)

    # Cálculo da altura
    def height(self, root):
        heightLeft = 0
        if root.getLeft():
            heightLeft = self.height(root.getLeft())
        
        heightRight = 0
        if root.getRight():
            heightRight = self.height(root.getRight())

        # Retorna 1 + a maior altura encontrada entre os filhos esquerdo e direito
        return 1 + max(heightLeft, heightRight)

    # Cálculo do fator de balanceamento
    def balanceFactor(self, root):
        heightLeft = 0
        if root.getLeft():
            heightLeft = self.height(root.getLeft())

        heightRight = 0
        if root.getRight():
            heightRight = self.height(root.getRight())

        return heightLeft - heightRight

    # Rotação Simples a Esquerda
    def rotationLeft(self, root):
        tempTitle, tempYear = root.getTitle(), root.getYear()
        root.setTitle(root.getRight().getTitle())
        root.setYear(root.getRight().getYear())
        root.getRight().setTitle(tempTitle)
        root.getRight().setYear(tempYear)

        oldLeft = root.getLeft()
        root.setLeft(root.getRight())
        root.setRight(root.getRight().getRight())
        root.getLeft().setRight(root.getLeft().getLeft())
        root.getLeft().setLeft(oldLeft)

    # Rotação Simples a Direita
    def rotationRight(self, root):
        tempTitle, tempYear = root.getTitle(), root.getYear()
        root.setTitle(root.getLeft().getTitle())
        root.setYear(root.getLeft().getYear())
        root.getLeft().setTitle(tempTitle)
        root.getLeft().setYear(tempYear)

        oldRight = root.getRight()
        root.setRight(root.getLeft())
        root.setLeft(root.getLeft().getLeft())
        root.getRight().setLeft(root.getRight().getRight())
        root.getRight().setRight(oldRight)

    # Rotação Dupla a Direita
    def rotationDoubleRight(self, root):
        self.rotationLeft(root.getLeft())
        self.rotationRight(root)

    # Rotação Dupla a Esquerda
    def rotationDoubleLeft(self, root):
        self.rotationRight(root.getRight())
        self.rotationLeft(root)

    # Listar livros em ordem alfabética, chama a função que percorre em ordem
    def listBook(self):
        self.inOrder(self.getRoot())

    # Percorrer a árvore em ordem
    # Condição para saber se é para buscar livros por ano (True) ou buscar em ordem alfabética (False)
    def inOrder(self, root, cond=False, year=None):
        global contYear
        if cond:
            if root != None:
                self.inOrder(root.getLeft(), True, year)
                if root.getYear() == year:
                    print(root)
                    contYear += 1
                self.inOrder(root.getRight(), True, year)
        else:
            if root == self.getRoot() and root == None:
                print('\nBiblioteca vazia.')
            elif root != None:
                self.inOrder(root.getLeft())
                print(root)
                self.inOrder(root.getRight())

    # Percorrer a árvore em pós-ordem para balancear
    def postOrder(self, root):
        if root != None:
            self.postOrder(root.getLeft())
            self.postOrder(root.getRight())
            self.tryBalance(root)

    # Aciona as rotações caso a árvore esteja desbalanceada
    def tryBalance(self, root):
        balance = self.balanceFactor(root)
        if balance > 1:
            if self.balanceFactor(root.getLeft()) > 0:
                self.rotationRight(root)
            else:
                self.rotationDoubleRight(root)
        elif balance < -1:
            if self.balanceFactor(root.getRight()) < 0:
                self.rotationLeft(root)
            else:
                self.rotationDoubleLeft(root)

    # Inserir livro, chama a função insert()
    def insertBook(self, title, year):
        self.insert(self.getRoot(), title, year)

    # Condições de inclusão
    def insert(self, root, title, year):
        if root == None:
            self.setRoot(No(title, year))
            print("\nLivro inserido com sucesso!")
        elif title < root.getTitle():
            if root.getLeft() == None:
                root.setLeft(No(title, year))
                print("\nLivro inserido com sucesso!")
            else:
                self.insert(root.getLeft(), title, year)
        elif title > root.getTitle():
            if root.getRight() == None:
                root.setRight(No(title, year))
                print("\nLivro inserido com sucesso!")
            else:
                self.insert(root.getRight(), title, year)
        elif title == root.getTitle():
            print('\nO livro já foi inserido!')

        self.postOrder(self.getRoot())
    
    # Buscar livros por ano
    # Resolve o contYear para descobrir se a quantidade de ocorrências foi igual a 0
    def searchYear(self, year):
        global contYear
        self.inOrder(self.getRoot(), True, year)
        if contYear == 0:
            print("\nNenhum registro desse ano foi encontrado.")
        contYear = 0
        
    # Buscar livro por título, chama a função search()
    def searchBook(self, title):
        if self.getRoot() != None:
            self.search(self.getRoot(), title)
        else:
            print('\nLivro não encontrado, biblioteca está vazia.')

    # Condições de busca
    def search(self, root, title):
        if root == None:
            print("\nO livro não foi encontrado na biblioteca!")
        elif root.getTitle() == title:
            result = '\nO livro foi encontrado!\n\n\tTítulo: ' + root.getTitle() + '\n\tAno: ' + str(root.getYear())
            print(result)
        elif title < root.getTitle():
            return self.search(root.getLeft(), title)
        elif title > self.getRoot().getTitle():
            return self.search(root.getRight(), title)

    # Descobrir se um nó é folha
    def isLeaf(self, root):
        if root.getLeft() == None and root.getRight() == None:
            return True
        return False

    # Descobrir se um nó possui apenas um filho
    def oneChild(self, root):
        if root.getLeft() != None and root.getRight() == None:
            return True
        elif root.getLeft() == None and root.getRight() != None:
            return True
        return False

    # Remover livro, chama a função remove
    def removeBook(self, title):
        self.remove(self.getRoot(), title)
    
    # Condições de remoção
    def remove(self, root, title, pai=None):
        if root == None:
            print("\nO livro não foi encontrado na biblioteca.")
        elif root.getTitle() == title:
            if self.isLeaf(root) and pai == None:
                self.setRoot(None)
            elif self.isLeaf(root):
                if pai.getLeft() == root:
                    pai.setLeft(None)
                else:
                    pai.setRight(None)
            elif self.oneChild(root):
                if root == self.getRoot():
                    if root.getLeft() == None:
                        self.setRoot(root.getRight())
                    else:
                        self.setRoot(root.getLeft()) # < O problema da remoção estava aqui, o getLeft() estava errado. Só isso.
                elif root.getLeft() == None:
                    if pai.getLeft() == root:
                        pai.setLeft(root.getRight())
                    else:
                        pai.setRight(root.getRight())
                else:
                    if pai.getLeft() == root:
                        pai.setLeft(root.getLeft())
                    else:
                        pai.setRight(root.getLeft())
            else:
                tempTitle = root.getTitle()
                tempYear = root.getYear()
                child = root.getRight()

                while child.getLeft() != None:
                    child = child.getLeft()

                root.setTitle(child.getTitle())
                root.setYear(child.getYear())
                child.setTitle(tempTitle)
                child.setYear(tempYear)
                self.remove(root.getRight(), child.getTitle(), root)
            self.postOrder(self.getRoot())

            print('\nLivro removido!')
        elif title < root.getTitle():
            self.remove(root.getLeft(), title, root)
        elif title > root.getTitle():
            self.remove(root.getRight(), title, root)
