
from No import No


class AVL:
    def __init__(self, root=None):
        self.__root = root

    def getRoot(self):
        return self.__root

    def setRoot(self, newRoot):
        self.__root = newRoot

    def height(self, root):
        heightLeft = 0
        if root.getLeft():
            heightLeft = self.height(root.getLeft())
        
        heightRight = 0
        if root.getRight():
            heightRight = self.height(root.getRight())

        return 1 + max(heightLeft, heightRight)

    def balanceFactor(self, root):
        heightLeft = 0
        if root.getLeft():
            heightLeft = self.height(root.getLeft())

        heightRight = 0
        if root.getRight():
            heightRight = self.height(root.getRight())

        return heightLeft - heightRight

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

    def rotationDoubleRight(self, root):
        self.rotationLeft(root.getLeft())
        self.rotationRight(root)

    def rotationDoubleLeft(self, root):
        self.rotationRight(root.getRight())
        self.rotationLeft(root)

    def listBook(self):
        self.inOrder(self.getRoot())

    def inOrder(self, root, cond=False, year=None):
        if cond:
            if root != None:
                self.inOrder(root.getLeft(), True, year)
                if root.getYear() == year:
                    print(root)
                self.inOrder(root.getRight(), True, year)
        else:
            if root != None:
                self.inOrder(root.getLeft())
                print(root)
                self.inOrder(root.getRight())

    def postOrder(self, root):
        if root != None:
            self.postOrder(root.getLeft())
            self.postOrder(root.getRight())
            self.tryBalance(root)

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

    def insertBook(self, title, year):
        self.insert(self.getRoot(), title, year)

    def insert(self, root, title, year):
        if root == None:
            self.setRoot(No(title, year))
        elif title < root.getTitle():
            if root.getLeft() == None:
                root.setLeft(No(title, year))
            else:
                self.insert(root.getLeft(), title, year)
        elif title > root.getTitle():
            if root.getRight() == None:
                root.setRight(No(title, year))
            else:
                self.insert(root.getRight(), title, year)

        self.postOrder(self.getRoot())
    
    def searchYear(self, year):
        self.inOrder(self.getRoot(), True, year)

    def searchBook(self, title):
        if self.getRoot() != None:
            self.search(self.getRoot(), title)
        else:
            return "Árvore vazia!"

    def search(self, root, title):
        if root.getTitle() == title:
            result = 'O livro foi encontrado!\n\tNome: ' + root.getTitle() + '\n\tAno: ' + str(root.getYear())
            return result
        elif title < root.getTitle():
            return self.search(root.getLeft(), title)
        elif title > self.getRoot().getTitle():
            return self.search(root.getRight(), title)
        elif root == None:
            return "O livro não foi encontrado na biblioteca!"

    def isLeaf(self, root):
        if root.getLeft() == None and root.getRight() == None:
            return True
        return False

    def oneChild(self, root):
        if root.getLeft() != None and root.getRight() == None:
            return True
        elif root.getLeft() == None and root.getRight() != None:
            return True
        return False

    def removeBook(self, title):
        self.remove(self.getRoot(), title)
    
    def remove(self, root, title, pai=None):
        if root.getTitle() == title:
            if self.isLeaf(root):
                if pai.getLeft() == root:
                    pai.setLeft(None)
                else:
                    pai.setRight(None)
            elif self.oneChild(root):
                if root.getLeft() == None:
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

            return "Livro removido!"
        elif title < root.getTitle():
            self.remove(root.getLeft(), title, root)
        elif title > root.getTitle():
            self.remove(root.getRight(), title, root)
        elif self.getRoot().getTitle() == None:
            return "O livro não foi encontrado na biblioteca!"


            