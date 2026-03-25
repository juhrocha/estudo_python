from time import  sleep

class Livro:
    """Classe responsável por acompanhar a leitura do usuário"""
    def __init__(self, titulo = '', paginas = 0):
        #Necessário criar aqui a contagem inicial da página inicial
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f'Você acabou de abrir o livro {self.titulo} que tem o número total de {self.paginas} paginas')

    def avancar_paginas(self, qtd_lida):
        #Necessário determinar a página antiga, vulgo após a leitura, e página nova
        #O input aqui não escrito claramente, está definido no self
        pagina_antiga = self.pagina_atual
        nova_pagina = self.pagina_atual + qtd_lida
        self.pagina_atual = nova_pagina
        if self.pagina_atual <= self.paginas:
            for c in range (pagina_antiga, self.pagina_atual):
                sleep(0.7)
                print(f'Página {c} ->', end=' ')
            print(f'Você agora está na página {self.pagina_atual}')
        elif self.pagina_atual > self.paginas:
            for c in range (pagina_antiga, self.paginas):
                sleep(0.5)
                print(f'Página {c} ->', end=' ')
            print(f'Você terminou de ler o livro {self.titulo}')



l1 = Livro('Mundo de Sofia', 10)
l1.avancar_paginas(3)
l1.avancar_paginas(5)
l1.avancar_paginas(20)







