import pygame

class AlternativaC(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('src/img/C.png')
        self.image = pygame.transform.scale(self.image, [250, 250])
        self.rect = pygame.Rect(-20, 270, 100, 100)