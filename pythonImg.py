import pygame

class Python(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('src/img/PythonImg.png')
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(455, 40, 100, 100)