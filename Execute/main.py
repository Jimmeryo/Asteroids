import sys
from Objects.asteroidfield import AsteroidField
from Objects.player import Player
from Objects.asteroid import Asteroid
from Constants import constants
from Objects.shot import *



#main function
def main():
    print(f"Starting Asteroids! \nScreen width: 1280 \nScreen height: 720")
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsans", 20)

    #fps counter in the top-left side of the game window
    def fps_counter():
        fps = str(int(clock.get_fps()))
        fps_t = font.render(fps, 1, pygame.Color("White"))
        screen.blit(fps_t, (10, 10))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()


    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (shot, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (drawable, updatable)

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    dt=0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shots in shot:
                if asteroid.collides_with(shots):
                    shots.kill()
                    asteroid.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        fps_counter()
        pygame.display.flip()
        dt = clock.tick(60)/1000.0


if __name__ == "__main__":
    main()