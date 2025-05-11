# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
# Constants for the game
from constants import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock= pygame.time.Clock()

    updatable= pygame.sprite.Group()
    drawable= pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()

    Shot.containers=(updatable,drawable,shots)
    Asteroid.containers=(updatable,drawable,asteroids)
    AsteroidField.containers =(updatable)
    asteroid_field =AsteroidField()
    
    Player.containers=(updatable,drawable)
    # Create a player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)

    dt=0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        screen.fill("black")
        dt=clock.tick(60)/1000
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        for obj in drawable:
            obj.draw(screen)



if __name__ == "__main__":
    main()
