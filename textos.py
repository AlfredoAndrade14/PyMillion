import pygame


class Texto():
    def __init__(self, text, size, color, x, y, display, font):
        if font == "Pixel":
            self.font_name = 'src/fonts/PixelOperator.ttf'
        elif font == "8-Bit":
            self.font_name = 'src/fonts/8-BIT WONDER.TTF'
        self.font = pygame.font.Font(self.font_name, size)
        self.texto = self.font.render(text, True, color)
        self.texto_rect = self.texto.get_rect()
        self.texto_rect = (x, y)
        display.blit(self.texto, self.texto_rect)
