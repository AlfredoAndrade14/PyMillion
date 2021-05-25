import pygame
from pygame.constants import MOUSEBUTTONDOWN

# Importa uma classe para importar sons e tocar a musica
from .audios import Audios

# Importa uma classe para cirar textos na tela
from .textos import Texto

# Importa a classe que cria o menu principal
from .menu import Menu

from time import sleep

# Importa a função de sorteio
from .sorteiaperg import sorteiaPergunta
from .perguntas import perguntas1,perguntas2,perguntas3,perguntafinal

# importa as caixas de pergunta
from .caixa import *

def run():
    # Inicia o pygame
    pygame.init()

    # Inicializa os audios do jogo
    audios = Audios()

    # Configura a janela
    SCREEN_SIZE = (600, 695)
    menu_display = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('PyMillion')

    # Inica o menu
    Gameloop = Menu.main_menu()

    # Cores
    cor_A = (30,144,255, 10)
    cor_B = (178, 34, 34, 10)
    cor_C = (251, 236, 93, 10)
    cor_D = (60, 179, 113, 10)

    def valida_resposta(alternativa):
        audios.certeza.play()
        certeza = False
        sim = Caixinha(220, 525, 145, 35, menu_display, (222, 207, 0), "CONFIRMAR", "") 
        sim.desenha_certeza()
        sim_box = pygame.Rect(220, 525, 145, 35)
        pygame.display.update()
        while not certeza:
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == MOUSEBUTTONDOWN:
                    if sim_box.collidepoint((mx, my)):
                        return alternativa
                    else:
                        if alt_a.collidepoint((mx, my)):
                            audios.certeza.play()
                            alternativa = A.conteudo
                        elif alt_b.collidepoint((mx, my)):
                            audios.certeza.play()
                            alternativa = B.conteudo
                        elif alt_c.collidepoint((mx, my)):
                            audios.certeza.play()
                            alternativa = C.conteudo
                        elif alt_d.collidepoint((mx, my)):
                            audios.certeza.play()
                            alternativa = D.conteudo
                        
        
    count = 0
    premio = 0
    respondeu = False
    while Gameloop:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # Fecha a janela
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            if event.type == MOUSEBUTTONDOWN:
                if alt_a.collidepoint((mx, my)):
                    alternativa = A.conteudo
                elif alt_b.collidepoint((mx, my)):
                    alternativa = B.conteudo
                elif alt_c.collidepoint((mx, my)):
                    alternativa = C.conteudo
                elif alt_d.collidepoint((mx, my)):
                    alternativa = D.conteudo
                else:
                    alternativa = ""

                if alternativa != "":
                    resp = valida_resposta(alternativa)
                    if resp == res:
                        if count != 15:
                            audios.acertou.play()
                            count += 1
                            premio += valor
                            sleep(1)
                            respondeu = False
                        else:
                            audios.acertou2.play()
                            count = 0
                            premio = 0
                            sleep(1)
                            respondeu = False
                            Menu.vitoria()
                    else:
                        audios.errou.play()
                        if count == 15:
                            premio = 0
                        else:
                            premio = int(premio/2)
                        respondeu = False
                        Menu.game_over(premio, count)
                        count = 0
                        premio = 0
                else:
                    pygame.display.update()


        if not respondeu and Gameloop:
            # Define objetos da janela
            menu_display.fill((68, 73, 80))

            Texto('Py',30,(30,144,255), 275, 10, menu_display, "8-Bit")
            Texto('Million',30,(251, 236, 93), 205, 60, menu_display, "8-Bit")
            Texto('Premio: ' + str(premio),16,( 218, 165, 32), 20, 650, menu_display, "Pixel")

            if count < 5:
                valor = 1000
                if count == 0:
                    lista = perguntas1[:]
                perg, res, a, b, c, d, lista = sorteiaPergunta(lista)
            elif count < 10:
                if count == 5:
                    valor = 5000
                    lista = perguntas2[:]
                else:
                    valor = 10000
                perg, res, a, b, c, d, lista = sorteiaPergunta(lista)
            elif count < 15:
                if count == 10:
                    valor = 50000
                    lista = perguntas3[:]
                else:
                    valor = 100000
                perg, res, a, b, c, d, lista = sorteiaPergunta(lista)
            else:
                lista = perguntafinal[:]
                perg, res, a, b, c, d, lista = sorteiaPergunta(lista)
                audios.pfinal.play()


            Pergunta = Caixinha(0, 120, 600, 90, menu_display, (25, 25, 112, 10), count, perg)
            Pergunta.desenha_caixinha()
            Pergunta.escreve_pergunta(str(count + 1) + '. ' + perg, (255, 255, 255), 15, 160)

            

            # Alternativa A
            alt_a = pygame.Rect(45, 260, 525, 53)
            A = Caixinha(70, 270, 500, 35, menu_display, (cor_A), "A", a)
            A.desenha_caixinha()
            A.escreve_pergunta(a, (0,0,0), 100, 280)

            # Alternativa B
            alt_b = pygame.Rect(45, 325, 525, 53)
            B = Caixinha(70, 335, 500, 35, menu_display, cor_B, "B", b) 
            B.desenha_caixinha()
            B.escreve_pergunta(b, (0,0,0), 100, 345)
            pygame.display.update()

            # Alternativa c
            alt_c = pygame.Rect(45, 390, 525, 53)
            C = Caixinha(70, 400, 500, 35, menu_display, cor_C, "C", c)
            C.desenha_caixinha()
            C.escreve_pergunta(c, (0,0,0), 100, 410)
                
            # Alternativa D
            alt_d = pygame.Rect(45, 455, 525, 53)
            D = Caixinha(70, 465, 500, 35, menu_display, cor_D, "D", d)
            D.desenha_caixinha()
            D.escreve_pergunta(d, (0,0,0), 100, 475)

            respondeu = True
        
        pygame.display.update()