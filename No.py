class No:
    def __init__(self, title, year, left=None, right=None):
        self.__title = title
        self.__year = year
        self.__left = left
        self.__right = right

    def getTitle(self):
        return self.__title

    def getYear(self):
        return self.__year

    def getLeft(self):
        return self.__left

    def getRight(self):
        return self.__right

    def setTitle(self, newTitle):
        self.__title = newTitle

    def setYear(self, newYear):
        self.__year = newYear

    def setLeft(self, left):
        self.__left = left

    def setRight(self, right):
        self.__right = right

    def __str__(self):
        result = 'Nome: ' +  str(self.getTitle()) + '\nAno: ' + str(self.getYear()) + '\n-----------'
        return result