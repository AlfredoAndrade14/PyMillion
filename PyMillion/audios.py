import pygame

class Audios():
    def __init__(self):
        #sons do jogo
        self.acertou = pygame.mixer.Sound('PyMillion/src/sounds/acertou.wav')
        self.acertou2 = pygame.mixer.Sound('PyMillion/src/sounds/acertou2.wav')
        self.errou = pygame.mixer.Sound('PyMillion/src/sounds/errou.wav')
        self.certeza = pygame.mixer.Sound('PyMillion/src/sounds/certeza.wav')
        self.pfinal = pygame.mixer.Sound('PyMillion/src/sounds/pfinal.wav')
