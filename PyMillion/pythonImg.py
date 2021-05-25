import pygame
import os

class Python(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.image = pygame.image.load(os.path.join(main_dir,'src/img/PythonImg.png'))
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(455, 40, 100, 100)
