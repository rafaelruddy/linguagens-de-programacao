# 8. Classe com Métodos Especiais (__str__ e __len__)
# Crie uma classe Livro com atributos titulo, autor e paginas. Implemente os
# métodos:
# • __str__(): Retorna uma string formatada com as informações do livro.
# • __len__(): Retorna o número de páginas.
# No programa principal, instancie um objeto da classe e exiba seus detalhes.

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}"
        
    def __len__(self):
        return self.paginas
    
livro = Livro("Dom Casmurro", "Machado de Assis", 256)

print(livro)