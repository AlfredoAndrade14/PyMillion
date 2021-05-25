import pygame
import os

class Audios():
    def __init__(self):
        #sons do jogo
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        pygame.mixer.music.load(os.path.join(main_dir,'src/sounds/musica.wav'))
        pygame.mixer.music.play(-1) 
        self.acertou = pygame.mixer.Sound(os.path.join(main_dir,'src/sounds/acertou.wav'))
        self.acertou2 = pygame.mixer.Sound(os.path.join(main_dir,'src/sounds/acertou2.wav'))
        self.errou = pygame.mixer.Sound(os.path.join(main_dir,'src/sounds/errou.wav'))
        self.certeza = pygame.mixer.Sound(os.path.join(main_dir,'src/sounds/certeza.wav'))
        self.pfinal = pygame.mixer.Sound(os.path.join(main_dir,'src/sounds/pfinal.wav'))
