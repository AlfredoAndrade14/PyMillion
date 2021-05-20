import pygame

# Importa uma classe para cirar textos na tela
from textos import Texto

def Caixa(x, y, w, h, display, cor, alternativa):
    caixa = pygame.Rect(x, y, w, h)
    pygame.draw.rect(display, cor, caixa, 0, 10)
    if x > 0:
        pygame.draw.circle(display, [255, 255, 255, 5], [x, y + 17], 25)
        Texto(alternativa, 16, (68, 73, 80), x-8, y+9, display, "Pixel")