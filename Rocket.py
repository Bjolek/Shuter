import pygame
import Bullet

class Spaceship:
    def __init__(self, x, y, w, h, speed, texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture,(w, h ))
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y


    def render(self, window):
        window.blit(self.texture, (self.hit_box.x, self.hit_box.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.hit_box.x += self.speed
        if keys[pygame.K_a]:
            self.hit_box.x -= self.speed

        for d in self.bulles:
            d.move()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.bulles.append(Bullet.Bullet(self.hit_box.x, self.hit_box.y, 10, 5, 6, "bullet.png"))

