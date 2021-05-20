import pygame

# Importa uma classe para cirar textos na tela
from textos import Texto

class Caixinha:
    def __init__(self, x, y, w, h, display, cor, alternativa):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.display = display
        self.cor = cor
        self.alternativa = alternativa
        caixa = pygame.Rect(x, y, w, h)
        pygame.draw.rect(display, cor, caixa, 0, 10)
        
    def desenha_caixinha(self):
        if self.x > 0:
            pygame.draw.circle(self.display, [255, 255, 255, 5], [self.x, self.y + 17], 25)
            Texto(self.alternativa, 16, (68, 73, 80), self.x-8, self.y+9, self.display, "Pixel")

    def escreve_pergunta(self, conteudo , x, y):
        return Texto(conteudo, 12, (0,0,0), x, y, self.display, "Pixel")
