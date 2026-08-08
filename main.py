import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from shot import Shot
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,) 
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, drawable, updatable)
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return
            
        screen.fill("black")
        for object in drawable:
            object.draw(screen)

        for object in updatable:
            object.update(dt)

        for object in asteroids:
           if object.collides_with(player):
               log_event("player_hit")
               print("Game over!")
               sys.exit()
        for object in asteroids:
            for shot in shots:
                if object.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    object.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000
       


    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print(f"{dt}")


if __name__ == "__main__":
    main()
