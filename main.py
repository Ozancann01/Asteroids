import pygame
import sys
from constants import *

from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    updatable=pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
 



    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = asteroids, updatable, drawable
    AsteroidField.containers = (updatable,) 

    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")


        for dra in drawable:
            dra.draw(screen)

        #player.draw(screen)



        asteroids.update(dt)
        updatable.update(dt)
        shots.update(dt)
        

        for asteroid in asteroids:
            
            if asteroid.colliding(player):
                sys.exit("Game over!!")
            
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.colliding(shot) :
                    shot.kill()
                    asteroid.split()


        #player.update(dt)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000

if __name__ == "__main__":
    main()
 
