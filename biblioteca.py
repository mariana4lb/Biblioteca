livros_d = []
livros_e = []

class Biblioteca:

    def adicionar (livro):
        livros_d.append(livro)
    
    def emprestar (livro):
        livros_d.remove(livro)
        livros_e.append(livro)
    
    def devolver (livro):
        livros_e.remove(livro)
        livros_d.append(livro)

    def imprimir_biblioteca (livros_d):
        print (livros_d)
