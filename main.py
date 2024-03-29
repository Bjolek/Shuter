import json
import pygame
import Rocket
import asteroid
import random

def start_game():
    def read_data():
        global settings
        with open("Settings.json", "r", encoding="utf-8") as file:
            settings = json.load(file)

    def write_data():
        global settings
        with open("Settings.json", "w", encoding="utf-8") as file:
            json.dump(settings, file)

    read_data()
    window = pygame.display.set_mode((800, 500))
    fps = pygame.time.Clock()

    fon = pygame.image.load("galaxy.jpg")
    fon = pygame.transform.scale(fon, (800, 500))


    Ship = Rocket.Spaceship(350, 350, 100, 150, 10, settings["skin"])

    stones = []

    stones.append(asteroid.Asteroid(random.randint(50, 750), -500, 70, 70, random.randint(1, 5), "asteroid.png") )
    stones.append(asteroid.Asteroid(random.randint(50, 750), -500, 70, 70, random.randint(1, 5), "asteroid.png") )
    stones.append(asteroid.Asteroid(random.randint(50, 750), -500, 70, 70, random.randint(1, 5), "asteroid.png") )
    stones.append(asteroid.Asteroid(random.randint(50, 750), -500, 70, 70, random.randint(1, 5), "asteroid.png") )
    stones.append(asteroid.Asteroid(random.randint(50, 750), -500, 70, 70, random.randint(1, 5), "asteroid.png") )
    stones.append(asteroid.Asteroid(random.randint(50, 750), -500, 70, 70, random.randint(1, 5), "asteroid.png") )
    game = True


    game = True
    while game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()

        window.blit(fon, [0 , 0])
        Ship.render(window)
        Ship.move()
        for elem in stones:
            elem.move()
            if elem.hit_box.y > 800:
                elem.hit_box.y = -10
                elem.hit_box.x = (random.randint(1, 5))
        for a in stones:
            if a.hit_box.colliderect(Ship.hit_box):
                game = False
                write_data()
                pygame.quit()
                return
        for a in stones:
            a.render(window)

        for A in stones:
            for B in Ship.bulles:
                if A.hit_box.colliderect(B.hit_box):
                    A.hit_box.y = -500
                    settings["money"] += 1

        pygame.display.flip()
        fps.tick(60)