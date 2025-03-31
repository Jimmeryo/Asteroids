import pygame
import constants

def main():
    print(f"Starting Asteroids! \nScreen width: 1280 \nScreen height: 720")
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.update()

if __name__ == "__main__":
    main()