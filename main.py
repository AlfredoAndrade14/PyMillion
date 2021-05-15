import pygame

pygame.init()
Gameloop = True


#configura a janela
display = pygame.display.set_mode([600,730])
pygame.display.set_caption('PyMillion')

drawGroup = pygame.sprite.Group()

python = pygame.sprite.Sprite(drawGroup)
python.image = pygame.image.load('img/PythonImg.png')
python.image = pygame.transform.scale(python.image, [150, 150])
python.rect = pygame.Rect(400, 50, 100, 100)


if __name__ == "__main__":
    while Gameloop:

        #define a cor do fundo da janela
        display.fill([68, 73, 80])
        drawGroup.draw(display)

        #fecha a janela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Gameloop = False

        #pega a tecla pressionada
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