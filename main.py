import pygame
from time import sleep

from pygame.constants import MOUSEBUTTONDOWN

# Importa uma classe para importar sons e tocar a musica
from audios import Audios

# Importa uma classe para cirar textos na tela
from textos import Texto

def main_menu():   
    menu_loop = True
    clicked = False
    while menu_loop:
        menu_display.fill(BACKGROUND_COLOR)
        drawGroup.draw(menu_display)

        Texto("MAIN MENU", 30, (WHITE_PY), 160, 200, menu_display)

        mx, my = pygame.mouse.get_pos()

        # Botões
        start_game_btn = pygame.Rect(160, 295, 270, 40)
        pygame.draw.rect(menu_display, (BACKGROUND_COLOR), start_game_btn)
        Texto("START GAME", 25, (PYTHON_BLUE), 170, 300, menu_display)

        options_btn = pygame.Rect(160, 345, 270, 40)
        pygame.draw.rect(menu_display, (BACKGROUND_COLOR), options_btn)
        Texto("OPTIONS", 25, (PYTHON_BLUE), 215, 350, menu_display)

        credits_btn = pygame.Rect(160, 395, 270, 40)
        pygame.draw.rect(menu_display, (BACKGROUND_COLOR), credits_btn)
        Texto("CREDITS", 25, (PYTHON_BLUE), 215, 400, menu_display)

        if start_game_btn.collidepoint((mx, my)):
            if clicked:
                break



        for event in pygame.event.get():
            # Sai do MENU
            if event.type == pygame.QUIT:
                menu_loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu_loop = False
                elif event.key == pygame.K_SPACE:
                    audios.certeza.play()

            if start_game_btn.collidepoint((mx, my)):
                if event.type == MOUSEBUTTONDOWN:
                    print("chegou aqui")
                    menu_loop = False

        pygame.display.update()

pygame.init()
Gameloop = True
Playing = False

# CORES
BACKGROUND_COLOR = (68, 73, 80)
PYTHON_BLUE = (30, 144, 255)
WHITE_PY = (255, 255, 255)

# Inicializa os audios do jogo
audios = Audios()

# Configura a janela
SCREEN_SIZE = (600, 695)
display = pygame.display.set_mode(SCREEN_SIZE)
menu_display = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('PyMillion')

# Define sprites
drawGroup = pygame.sprite.Group()
python = pygame.sprite.Sprite(drawGroup)
python.image = pygame.image.load('src/img/PythonImg.png')
python.image = pygame.transform.scale(python.image, [100, 100])
python.rect = pygame.Rect(455, 40, 100, 100)

main_menu()

if __name__ == "__main__":
    while Gameloop:

        
        # Define objetos da janela
        display.fill(BACKGROUND_COLOR)
        drawGroup.draw(display)

        Texto('Py',30,(30,144,255), 275, 40, display)
        Texto('Million',30,(251, 236, 93), 205, 90, display)

        for event in pygame.event.get():
            # Fecha a janela
            if event.type == pygame.QUIT:
                Gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Gameloop = False
                elif event.key == pygame.K_SPACE:
                    audios.certeza.play()


        # Temporariamente move a logo do python
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            python.rect.x -= 1
        if keys[pygame.K_d]:
            python.rect.x += 1
        if keys[pygame.K_s]:
            python.rect.y += 1
        if keys[pygame.K_w]:
            python.rect.y -= 1

        pygame.display.update()