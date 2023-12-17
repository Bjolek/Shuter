import pygame
import Rocket

window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()

Ship = Rocket.Spaceship(250, 350,50,50,10,"rocket.png")


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    window.fill((123, 123, 123))
    Ship.render(window)
    Ship.move()
    pygame.display.flip()
    fps.tick(60)