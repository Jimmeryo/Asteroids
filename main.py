import pygame
from pygame.time import Clock
from player import Player
import constants

#main function
def main():
    print(f"Starting Asteroids! \nScreen width: 1280 \nScreen height: 720")
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    dt=0
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsans", 20)

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    #fps counter in the top-left side of the game window
    def fps_counter():
        fps = str(int(clock.get_fps()))
        fps_t = font.render(fps, 1, pygame.Color("White"))
        screen.blit(fps_t, (10, 10))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)

        fps_counter()
        pygame.display.update()
        dt = clock.tick(60)/1000.0


if __name__ == "__main__":
    main()