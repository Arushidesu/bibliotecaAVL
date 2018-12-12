from No import No
from AVL import AVL

biblioteca = AVL()

biblioteca.insertBook("A", 2000)
biblioteca.insertBook("C", 2002)
biblioteca.insertBook("B", 2005)
print(biblioteca.getRoot())
print(biblioteca.getRoot().getLeft())
print(biblioteca.getRoot().getRight())
# biblioteca.insertBook("K", 2006)
# biblioteca.insertBook("F", 2001)
# print(biblioteca.getRoot().getRight().getRight())
print('-------------')
# biblioteca.removeBook("H")
# print(biblioteca.getRoot().getRight().getLeft())