import pygame
import os

class Texto():
    def __init__(self, text, size, color, x, y, display, font):
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        if font == "Pixel":
            self.font_name = os.path.join(main_dir,'src/fonts/PixelOperator.ttf')
        elif font == "8-Bit":
            self.font_name = os.path.join(main_dir,'src/fonts/8-BIT WONDER.ttf')
        self.font = pygame.font.Font(self.font_name, size)
        self.texto = self.font.render(text, True, color)
        self.texto_rect = self.texto.get_rect()
        self.texto_rect = (x, y)
        display.blit(self.texto, self.texto_rect)
