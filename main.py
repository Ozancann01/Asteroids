import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable=pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")


        for dra in drawable:
            dra.draw(screen)

        #player.draw(screen)

        updatable.update(dt)

        #player.update(dt)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000

if __name__ == "__main__":
    main()
 
