import pygame
import constants
from circleshape import CircleShape


#main class wow
class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.PLAYER_RADIUS = 20
        self.x = constants.SCREEN_WIDTH / 2
        self.y = constants.SCREEN_HEIGHT / 2

    #tbs this gives us a form and collision factor
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    #space-ship model creator
    def draw(self,screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    #calculating rotation speed
    def rotate(self,dt):
        self.rotation += dt * constants.PLAYER_TURN_SPEED

    #moving method
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    #updating the position of our ship
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)