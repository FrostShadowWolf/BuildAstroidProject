import random
import pygame
import constants
import sys
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event, log_state
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants. SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)

    Shot.containers = (shots, drawable, updatable)

    player = Player(x = constants.SCREEN_WIDTH / 2, y = constants.SCREEN_HEIGHT / 2)
    
    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    
            
        screen.fill("black")

        for drawing in drawable:
           drawing.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

       


if __name__ == "__main__":
    main()
