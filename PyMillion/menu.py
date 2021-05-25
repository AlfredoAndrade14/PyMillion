import pygame

from pygame.constants import KEYDOWN, K_t, MOUSEBUTTONDOWN

from .textos import Texto

from .pythonImg import Python

from .audios import Audios

objectGroup = pygame.sprite.Group()

python = Python(objectGroup)

class Menu():
    def main_menu():    
        Menuv = False
        while not Menuv:
             # Configura a janela
            SCREEN_SIZE = (600, 695)
            menu_display = pygame.display.set_mode(SCREEN_SIZE)
            pygame.display.set_caption('PyMillion')

            menu_display.fill((68, 73, 80))
            objectGroup.draw(menu_display)

            Texto('Py',30,(30,144,255), 270, 40, menu_display,"8-Bit")
            Texto('Million',30,(251, 236, 93), 200, 90, menu_display,"8-Bit")

            Texto("MAIN MENU", 30, (255, 255, 255), 160, 200, menu_display, "Pixel")

            mx, my = pygame.mouse.get_pos()

            # Botões
            start_game_btn = pygame.Rect(170, 295, 245, 40)
            pygame.draw.rect(menu_display, (68, 73, 80), start_game_btn)
            Texto("START GAME", 25, (30, 144, 255), 170, 300, menu_display, "Pixel")

            options_btn = pygame.Rect(200, 345, 185, 40)
            pygame.draw.rect(menu_display, (68, 73, 80), options_btn)
            Texto("OPTIONS", 25, (30, 144, 255), 208, 350, menu_display, "Pixel")

            credits_btn = pygame.Rect(200, 395, 185, 40)
            pygame.draw.rect(menu_display, (68, 73, 80), credits_btn)
            Texto("CREDITS", 25, (30, 144, 255), 208, 400, menu_display, "Pixel")

            quit_btn = pygame.Rect(240, 445, 105, 40)
            pygame.draw.rect(menu_display, (68, 73, 80), quit_btn)
            Texto("SAIR", 25, (30, 144, 255), 245, 450, menu_display, "Pixel")

            for event in pygame.event.get():
                # Sai do MENU
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                # Inicia o jogo
                if start_game_btn.collidepoint((mx, my)):
                    if event.type == MOUSEBUTTONDOWN:
                        Gameloop = True
                        Menuv = True
                        pygame.display.update()
                        return Gameloop
                elif options_btn.collidepoint((mx, my)):
                    if event.type == MOUSEBUTTONDOWN:
                        Menu.Options()
                elif credits_btn.collidepoint((mx, my)):
                    if event.type == MOUSEBUTTONDOWN:
                        Menu.Creditos()
                # Sai do jogo
                elif quit_btn.collidepoint((mx, my)):
                    if event.type == MOUSEBUTTONDOWN:
                        pygame.quit()
                        quit()

                if event.type == KEYDOWN:
                    if event.key == K_t:
                        objectGroup.empty()
                elif event.type == pygame.KEYUP:
                    if event.key == K_t:
                        objectGroup.add(python)
                    

            pygame.display.update()


    
    def game_over(premio, count):   
        # Configura a janela
        SCREEN_SIZE = (600, 695)
        menu_display = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('PyMillion')
        
        Playing = False
        while not Playing:
            menu_display.fill((68, 73, 80))
            objectGroup.draw(menu_display)

            Texto('Py',30,(30,144,255), 270, 40, menu_display,"8-Bit")
            Texto('Million',30,(251, 236, 93), 200, 90, menu_display,"8-Bit")

            Texto("VOCÊ ERROU", 16, (178, 34, 34, 10), 220, 200, menu_display, "Pixel")
            Texto("Você ganhou: " + str(premio) + " Reais", 16, (218, 165, 32), 150, 300, menu_display, "Pixel")
            Texto("Você acertou: " + str(count) + " Perguntas", 16, (218, 165, 32), 110, 350, menu_display, "Pixel")

            mx, my = pygame.mouse.get_pos()

            # Botões
            quit_btn = pygame.Rect(340, 455, 105, 40)
            pygame.draw.rect(menu_display, ((68, 73, 80)), quit_btn)
            Texto("SAIR", 25, (30, 144, 255), 345, 460, menu_display, "Pixel")

            menu_btn = pygame.Rect(140, 455, 105, 40)
            pygame.draw.rect(menu_display, ((68, 73, 80)), menu_btn)
            Texto("Menu", 25, (30, 144, 255), 145, 460, menu_display, "Pixel")

            for event in pygame.event.get():
                # Sai do MENU
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                # Volta para o menu inicial do jogo
                if menu_btn.collidepoint((mx, my)):
                    if event.type == MOUSEBUTTONDOWN:
                        Playing = True
                        Menu.main_menu()
                # Sai do jogo
                elif quit_btn.collidepoint((mx, my)):
                    if event.type == MOUSEBUTTONDOWN:
                        pygame.quit()
                        quit()
                
            pygame.display.update()


    def Options():
            # Configura a janela
            SCREEN_SIZE = (600, 695)
            menu_display = pygame.display.set_mode(SCREEN_SIZE)
            pygame.display.set_caption('PyMillion')
        
            Option = False
            Muted = False
            while not Option:
                menu_display.fill((68, 73, 80))
                objectGroup.draw(menu_display)

                Texto('Py',30,(30,144,255), 270, 40, menu_display,"8-Bit")
                Texto('Million',30,(251, 236, 93), 200, 90, menu_display,"8-Bit")

                Texto("OPÇÕES", 25, (255, 255, 255), 220, 200, menu_display, "Pixel")

                mx, my = pygame.mouse.get_pos()

                # Botões
                som_btn = pygame.Rect(145, 325, 245, 40)
                pygame.draw.rect(menu_display, ((68, 73, 80)), som_btn)
                Texto("Desativar som", 25, (30, 144, 255), 150, 330, menu_display, "Pixel")

                som_btn2 = pygame.Rect(175, 375, 245, 40)
                pygame.draw.rect(menu_display, ((68, 73, 80)), som_btn2)
                Texto("Ativar som", 25, (30, 144, 255), 180, 380, menu_display, "Pixel")

                menu_btn = pygame.Rect(235, 455, 105, 40)
                pygame.draw.rect(menu_display, ((68, 73, 80)), menu_btn)
                Texto("Menu", 25, (30, 144, 255), 240, 460, menu_display, "Pixel")

                for event in pygame.event.get():
                    # Sai das opções
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            quit()

                    if som_btn.collidepoint((mx, my)):
                        if event.type == MOUSEBUTTONDOWN and not Muted:
                            pygame.mixer.quit()
                            pygame.mixer.init()
                            Muted = True
                            
                    elif som_btn2.collidepoint((mx, my)):
                        if event.type == MOUSEBUTTONDOWN and Muted:
                            pygame.mixer.init()
                            Audios()
                            Muted = False
                            
                    # Sai do jogo
                    elif menu_btn.collidepoint((mx, my)):
                        if event.type == MOUSEBUTTONDOWN:
                            Option = True
                            return
                    
                pygame.display.update()
    
    def Creditos():
            # Configura a janela
            SCREEN_SIZE = (600, 695)
            menu_display = pygame.display.set_mode(SCREEN_SIZE)
            pygame.display.set_caption('PyMillion')    
            
            Playing = False
            while not Playing:
                menu_display.fill((68, 73, 80))
                
                Texto('Py',30,(30,144,255), 275, 10, menu_display, "8-Bit")
                Texto('Million',30,(251, 236, 93), 205, 60, menu_display, "8-Bit")

                Texto('Jogo Feito Por:',20,(30,144,255), 80, 210, menu_display, "Pixel")
                Texto('André Araújo Alves',15,(251, 236, 93), 190, 300, menu_display, "Pixel")
                Texto('e',15,(30,144,255), 290, 330, menu_display, "Pixel")
                Texto('Alfredo Vasconcelos de Andrade',15,(251, 236, 93), 100, 360, menu_display, "Pixel")

                mx, my = pygame.mouse.get_pos()

                # Botões
                quit_btn = pygame.Rect(340, 455, 105, 40)
                pygame.draw.rect(menu_display, ((68, 73, 80)), quit_btn)
                Texto("SAIR", 25, (30, 144, 255), 345, 460, menu_display, "Pixel")

                menu_btn = pygame.Rect(140, 455, 105, 40)
                pygame.draw.rect(menu_display, ((68, 73, 80)), menu_btn)
                Texto("Menu", 25, (30, 144, 255), 145, 460, menu_display, "Pixel")

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
                    elif menu_btn.collidepoint((mx, my)):
                        if event.type == MOUSEBUTTONDOWN:
                            return
                            

                pygame.display.update()

    def vitoria():   
        # Configura a janela
        SCREEN_SIZE = (600, 695)
        menu_display = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('PyMillion')
        
        Playing = False
        while not Playing:
            menu_display.fill((68, 73, 80))
            objectGroup.draw(menu_display)

            Texto('Py',30,(30,144,255), 270, 40, menu_display,"8-Bit")
            Texto('Million',30,(251, 236, 93), 200, 90, menu_display,"8-Bit")

            Texto("PARABÉNS VOCÊ GANHOU", 16, (255, 255, 255), 145, 200, menu_display, "Pixel")
            Texto("Você ganhou Um milhão de reais", 16, (218, 165, 32), 70, 300, menu_display, "Pixel")
            Texto("Você acertou todas as perguntas", 16, (60, 179, 113), 60, 350, menu_display, "Pixel")

            mx, my = pygame.mouse.get_pos()

            # Botões
            quit_btn = pygame.Rect(340, 455, 105, 40)
            pygame.draw.rect(menu_display, ((68, 73, 80)), quit_btn)
            Texto("SAIR", 25, (30, 144, 255), 345, 460, menu_display, "Pixel")

            menu_btn = pygame.Rect(140, 455, 105, 40)
            pygame.draw.rect(menu_display, ((68, 73, 80)), menu_btn)
            Texto("Menu", 25, (30, 144, 255), 145, 460, menu_display, "Pixel")

            for event in pygame.event.get():
                # Sai do MENU
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                # Volta para o menu inicial do jogo
                if menu_btn.collidepoint((mx, my)):
                    if event.type == MOUSEBUTTONDOWN:
                        Playing = True
                        Menu.main_menu()
                # Sai do jogo
                elif quit_btn.collidepoint((mx, my)):
                    if event.type == MOUSEBUTTONDOWN:
                        pygame.quit()
                        quit()
                
            pygame.display.update()
