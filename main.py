import pygame

#importa uma classe para importar sons e tocar a musica
from audios import Audios

#importa uma classe para cirar textos na tela
from textos import Texto

pygame.init()
Gameloop = True
Playing = False

#inicializa os audios do jogo
audios = Audios()

#configura a janela
SCREEN_SIZE = (600, 695)
display = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('PyMillion')

#define sprites
drawGroup = pygame.sprite.Group()
python = pygame.sprite.Sprite(drawGroup)
python.image = pygame.image.load('src/img/PythonImg.png')
python.image = pygame.transform.scale(python.image, [100, 100])
python.rect = pygame.Rect(455, 40, 100, 100)


if __name__ == "__main__":
    while Gameloop:

        #define objetos da janela
        display.fill([68, 73, 80])
        drawGroup.draw(display)

        Texto('Py',30,(30,144,255), 275, 40, display)
        Texto('Million',30,(251, 236, 93), 205, 90, display)

        for event in pygame.event.get():
            #fecha a janela
            if event.type == pygame.QUIT:
                Gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Gameloop = False
                elif event.key == pygame.K_SPACE:
                    audios.certeza.play()


        #temporariamente move a logo do python
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            python.rect.x -= 1
        if keys[pygame.K_d]:
            python.rect.x += 1
        if keys[pygame.K_s]:
            python.rect.y += 1
        if keys[pygame.K_w]:
            python.rect.y -= 1

        pygame.display.update()