import pygame

# Importa uma classe para importar sons e tocar a musica
from audios import Audios

# Importa uma classe para cirar textos na tela
from textos import Texto

# Importa a classe que cria o menu principal
from menu import Menu

pygame.init()
Gameloop = Menu.main_menu()

# Inicializa os audios do jogo
audios = Audios()

# Configura a janela
SCREEN_SIZE = (600, 695)
menu_display = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('PyMillion')

# Define sprites
drawGroup = pygame.sprite.Group()
python = pygame.sprite.Sprite(drawGroup)
python.image = pygame.image.load('src/img/PythonImg.png')
python.image = pygame.transform.scale(python.image, [100, 100])
python.rect = pygame.Rect(455, 40, 100, 100)

if __name__ == "__main__":
    while Gameloop:

        
        # Define objetos da janela
        menu_display.fill((68, 73, 80))
        drawGroup.draw(menu_display)

        Texto('Py',30,(30,144,255), 275, 40, menu_display)
        Texto('Million',30,(251, 236, 93), 205, 90, menu_display)

        for event in pygame.event.get():
            # Fecha a janela
            if event.type == pygame.QUIT:
                Gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Gameloop = False
                elif event.key == pygame.K_SPACE:
                    audios.certeza.play()

        pygame.display.update()