import pygame

from pygame.constants import MOUSEBUTTONDOWN

from textos import Texto

from pythonImg import Python

objectGroup = pygame.sprite.Group()

python = Python(objectGroup)

class Menu():
    def main_menu():   
        # Configura a janela
        SCREEN_SIZE = (600, 695)
        menu_display = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('PyMillion')

        # CORES
        BACKGROUND_COLOR = (68, 73, 80)
        PYTHON_BLUE = (30, 144, 255)
        WHITE_PY = (255, 255, 255)
        
        
        Playing = False
        while not Playing:
            menu_display.fill(BACKGROUND_COLOR)
            
            objectGroup.draw(menu_display)

            Texto('Py',30,(30,144,255), 275, 40, menu_display,"8-Bit")
            Texto('Million',30,(251, 236, 93), 205, 90, menu_display,"8-Bit")

            Texto("MAIN MENU", 30, (WHITE_PY), 160, 200, menu_display, "Pixel")

            mx, my = pygame.mouse.get_pos()

            # Botões
            start_game_btn = pygame.Rect(160, 295, 270, 40)
            pygame.draw.rect(menu_display, (BACKGROUND_COLOR), start_game_btn)
            Texto("START GAME", 25, (PYTHON_BLUE), 170, 300, menu_display, "Pixel")

            options_btn = pygame.Rect(160, 345, 270, 40)
            pygame.draw.rect(menu_display, (BACKGROUND_COLOR), options_btn)
            Texto("OPTIONS", 25, (PYTHON_BLUE), 215, 350, menu_display, "Pixel")

            credits_btn = pygame.Rect(160, 395, 270, 40)
            pygame.draw.rect(menu_display, (BACKGROUND_COLOR), credits_btn)
            Texto("CREDITS", 25, (PYTHON_BLUE), 215, 400, menu_display, "Pixel")

            for event in pygame.event.get():
                # Sai do MENU
                if event.type == pygame.QUIT:
                    Gameloop = False
                    return Gameloop
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Gameloop = False
                        return Gameloop

                if start_game_btn.collidepoint((mx, my)):
                    if event.type == MOUSEBUTTONDOWN:
                        Gameloop = True
                        return Gameloop

            pygame.display.update()
