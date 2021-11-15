import pygame
from settings import *
class Particle(pygame.sprite.Sprite):
    def __init__(self, app, x, y, radius, angle, speed):
        super().__init__()
        self.pos = pygame.math.Vector2(x, y)
        self.radius = radius
        self.color = BLUE
        self.thickness = 1
        self.vel = pygame.math.Vector2(1, 0) * speed
        self.angle = angle
        self.vel.rotate_ip(self.angle)
        self.app = app
        self.app.particles.add(self)
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius, self.thickness)
    
    def update(self):
        self.move()
        self.bounce()
    
    def move(self):
        self.vel = self.vel + GRAVITY * self.app.dt
        #self.vel *= DRAG
        self.pos += 1/2 * GRAVITY * self.app.dt + self.vel * self.app.dt
        self.angle = round(pygame.math.Vector2(1, 0).angle_to(self.vel))
    def bounce(self):
        if self.pos.x > WIDTH and self.vel.x > 0:
            #self.pos.x = 2 * (WIDTH - self.radius) - self.pos.x
            self.angle = 180 - self.angle
            self.vel.x *= ELASTICITY
        elif self.pos.x < self.radius and self.vel.x < 0:
            #self.pos.x = 2 * self.radius - self.pos.x
            self.angle = 180 - self.angle
            self.vel.x *= ELASTICITY
        if self.pos.y > HEIGHT - self.radius and self.vel.y > 0:
            #self.pos.y = 2 *(HEIGHT - self.radius) - self.pos.y
            self.angle = -self.angle
            self.vel.y *= ELASTICITY
        elif self.pos.y < self.radius and self.vel.y < 0:
            #self.pos.y = 2 * self.radius - self.pos.y
            self.angle = -self.angle
            self.vel.y *= ELASTICITY
        self.angle %= 360
        current_angle = round(pygame.math.Vector2(1, 0).angle_to(self.vel))
        rotation = self.angle - current_angle
        self.vel.rotate_ip(rotation)
            
            