import pygame

class Audios():
    def __init__(self):
        #sons do jogo
        self.acertou = pygame.mixer.Sound('src/sounds/acertou.wav')
        self.acertou2 = pygame.mixer.Sound('src/sounds/acertou2.wav')
        self.errou = pygame.mixer.Sound('src/sounds/errou.wav')
        self.certeza = pygame.mixer.Sound('src/sounds/certeza.wav')
        self.pfinal = pygame.mixer.Sound('src/sounds/pfinal.wav')
