import pygame

from pygame.constants import MOUSEBUTTONDOWN

from textos import Texto

from pythonImg import Python

class Creditos():
    def creditos(display):   
        # Configura a janela
        menu_display = display

        # CORES
        BACKGROUND_COLOR = (68, 73, 80)
        PYTHON_BLUE = (30, 144, 255)    
        
        Playing = False
        while not Playing:
            menu_display.fill(BACKGROUND_COLOR)
            
            Texto('Py',30,(30,144,255), 275, 10, menu_display, "8-Bit")
            Texto('Million',30,(251, 236, 93), 205, 60, menu_display, "8-Bit")

            Texto('Jogo Feito Por:',20,(30,144,255), 80, 210, menu_display, "Pixel")
            Texto('André Araújo Alves',15,(251, 236, 93), 190, 300, menu_display, "Pixel")
            Texto('e',15,(30,144,255), 290, 330, menu_display, "Pixel")
            Texto('Alfredo Vasconcelos de Andrade',15,(251, 236, 93), 100, 360, menu_display, "Pixel")

            mx, my = pygame.mouse.get_pos()

            # Botões
            quit_btn = pygame.Rect(240, 445, 105, 40)
            pygame.draw.rect(menu_display, (BACKGROUND_COLOR), quit_btn)
            Texto("SAIR", 25, (PYTHON_BLUE), 245, 450, menu_display, "Pixel")

            for event in pygame.event.get():
                # Sai do MENU
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                # Sai do jogo
                if quit_btn.collidepoint((mx, my)):
                    if event.type == MOUSEBUTTONDOWN:
                        pygame.quit()
                        quit()

            pygame.display.update()