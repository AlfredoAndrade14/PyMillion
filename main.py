import pygame

# Importa uma classe para importar sons e tocar a musica
from audios import Audios

# Importa uma classe para cirar textos na tela
from textos import Texto

# Importa a classe que cria o menu principal
from menu import Menu

# Inicia o pygame
pygame.init()

from caixa import Caixa

# Inicializa os audios do jogo
audios = Audios()

# Objetos
objectGroup = pygame.sprite.Group()

# Configura a janela
SCREEN_SIZE = (600, 695)
menu_display = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('PyMillion')

# Inica o menu
Gameloop = Menu.main_menu()

if __name__ == "__main__":
    while Gameloop:
        # Define objetos da janela
        menu_display.fill((68, 73, 80))

        for event in pygame.event.get():
            # Fecha a janela
            if event.type == pygame.QUIT:
                Gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Gameloop = False


        Texto('Py',30,(30,144,255), 275, 10, menu_display, "8-Bit")
        Texto('Million',30,(251, 236, 93), 205, 60, menu_display, "8-Bit")

        # Pergunta
        Caixa(0, 120, 600, 90, menu_display, [25, 25, 112, 10], '')

        # Alternativa A
        Caixa(70, 270, 500, 35, menu_display, [30,144,255, 10], 'A')

        # Alternativa B
        Caixa(70, 335, 500, 35, menu_display, [178, 34, 34, 10], 'B')

        # Alternativa c
        Caixa(70, 400, 500, 35, menu_display, [251, 236, 93, 10], 'C')
        
        # Alternativa D
        Caixa(70, 465, 500, 35, menu_display, [60, 179, 113, 10], 'D')

        objectGroup.draw(menu_display)

        pygame.display.update()