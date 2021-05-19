import pygame

class AlternativaB(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('src/img/B.png')
        self.image = pygame.transform.scale(self.image, [250, 250])
        self.rect = pygame.Rect(-20, 170, 100, 100)