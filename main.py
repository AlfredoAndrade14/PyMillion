import pygame
from pygame.constants import MOUSEBUTTONDOWN
from pygame.time import Clock

# Importa uma classe para importar sons e tocar a musica
from audios import Audios

# Importa uma classe para cirar textos na tela
from textos import Texto

# Importa a classe que cria o menu principal
from menu import Menu

# Importa a função de sorteio
from sorteiaperg import sorteiaPergunta
from perguntas import perguntas1

# Inicia o pygame
pygame.init()

from caixa import *

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

# CORES
BACKGROUND_COLOR = (68, 73, 80)


if __name__ == "__main__":
    count = 1
    premio = 0
    respondeu = False
    while Gameloop:

        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # Fecha a janela
            if event.type == pygame.QUIT:
                Gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Gameloop = False
            
            if event.type == MOUSEBUTTONDOWN:
                if alt_a.collidepoint((mx, my)):
                    audios.certeza.play()
                    if alt_a.collidepoint((mx, my)):
                        if a == res:
                            audios.acertou.play()
                            count += 1
                            premio += 5000
                        else:
                            audios.errou.play()
                            premio = 0
                            print('perdeu')
                    respondeu = False
                elif alt_b.collidepoint((mx, my)):
                    audios.certeza.play()
                    if alt_b.collidepoint((mx, my)):
                        if b == res:
                            audios.acertou.play()
                            count += 1
                            premio += 5000
                        else:
                            audios.errou.play()
                            premio = 0
                            print('perdeu')
                    respondeu = False
                elif alt_c.collidepoint((mx, my)):
                    audios.certeza.play()
                    if alt_c.collidepoint((mx, my)):
                        if c == res:
                            audios.acertou.play()
                            count += 1
                            premio += 5000
                        else:
                            audios.errou.play()
                            premio = 0
                            print('perdeu')
                    respondeu = False
                elif alt_d.collidepoint((mx, my)):
                    audios.certeza.play()
                    if alt_d.collidepoint((mx, my)):
                        if d == res:
                            audios.acertou.play()
                            count += 1
                            premio += 5000
                        else:
                            audios.errou.play()
                            premio = 0
                            print('perdeu')
                    respondeu = False

        if not respondeu and Gameloop:
            # Define objetos da janela
            menu_display.fill((68, 73, 80))

            Texto('Py',30,(30,144,255), 275, 10, menu_display, "8-Bit")
            Texto('Million',30,(251, 236, 93), 205, 60, menu_display, "8-Bit")
            Texto('Premio: ' + str(premio),16,( 218, 165, 32), 20, 650, menu_display, "Pixel")

            if count < 6:
                lista = perguntas1
                perg, res, a, b, c, d, lista = sorteiaPergunta(lista)
            elif count < 11:
                print('level 2')
                break
            elif count < 16:
                print('level 3')
                break
            else:
                print('pergubta final')
                break

            Pergunta = Caixinha(0, 120, 600, 90, menu_display, (25, 25, 112, 10), count)
            Pergunta.desenha_caixinha()
            Pergunta.escreve_pergunta(perg, (255, 255, 255), 15, 160)

            # Alternativa A
            alt_a = pygame.Rect(45, 260, 525, 53)
            A = Caixinha(70, 270, 500, 35, menu_display, ((30,144,255, 10)), "A")
            A.desenha_caixinha()
            A.escreve_pergunta(a, (0,0,0), 100, 280)

            # Alternativa B
            alt_b = pygame.Rect(45, 325, 525, 53)
            B = Caixinha(70, 335, 500, 35, menu_display, [178, 34, 34, 10], "B") 
            B.desenha_caixinha()
            B.escreve_pergunta(b, (0,0,0), 100, 345)

            # Alternativa c
            alt_c = pygame.Rect(45, 390, 525, 53)
            C = Caixinha(70, 400, 500, 35, menu_display, [251, 236, 93, 10], "C")
            C.desenha_caixinha()
            C.escreve_pergunta(c, (0,0,0), 100, 410)
            
            # Alternativa D
            alt_d = pygame.Rect(45, 455, 525, 53)
            D = Caixinha(70, 465, 500, 35, menu_display, [60, 179, 113, 10], "D")
            D.desenha_caixinha()
            D.escreve_pergunta(d, (0,0,0), 100, 475)

            respondeu = True
        
        pygame.display.update()