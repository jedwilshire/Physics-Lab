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
        self.vel.rotate_ip(angle)
        self.app = app
        self.app.particles.add(self)
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius, self.thickness)
    
    def update(self):
        self.move()
        self.bounce()
    
    def move(self):
        self.vel = self.vel + GRAVITY * self.app.dt
        self.pos += 1/2 * GRAVITY * self.app.dt + self.vel * self.app.dt
        
    def bounce(self):
        if self.pos.x > WIDTH - self.radius and self.vel.x > 0:
            self.vel.reflect_ip(pygame.math.Vector2(-1, 0))
        elif self.pos.x < self.radius and self.vel.x < 0:
            self.vel.reflect_ip(pygame.math.Vector2(1, 0))
        if self.pos.y > HEIGHT - self.radius and self.vel.y > 0:
            self.vel.reflect_ip(pygame.math.Vector2(0, -1))
        elif self.pos.y < self.radius and self.vel.y < 0:
            self.vel.reflect_ip(pygame.math.Vector2(0, 1))
        
            
            