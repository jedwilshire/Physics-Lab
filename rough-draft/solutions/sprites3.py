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
        # an acceleration vector
        self.acc = pygame.math.Vector2(GRAVITY)
        self.friction = -self.vel
        self.app = app
        self.app.particles.add(self)
        self.stopped_on_ground = False
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius, self.thickness)
    
    def update(self):
        if not self.stopped_on_ground:
            self.move()
            self.bounce()
            #print(self.vel)
    
    def move(self):
        self.friction = -self.vel * FRICTION
        if self.pos.y >= HEIGHT - self.radius:
            self.vel += self.friction
        self.vel = self.vel + self.acc * self.app.dt
        self.pos += 1/2 * self.acc * self.app.dt + self.vel * self.app.dt
        if self.pos.y <= HEIGHT - self.radius:
            self.acc = GRAVITY
        
    def bounce(self):
        if self.pos.x > WIDTH - self.radius and self.vel.x > 0:
            self.vel.reflect_ip(pygame.math.Vector2(-1, 0))
        elif self.pos.x < self.radius and self.vel.x < 0:
            self.vel.reflect_ip(pygame.math.Vector2(1, 0))
        if self.pos.y > HEIGHT - self.radius:
            self.vel.reflect_ip(pygame.math.Vector2(0, -1))
            if self.vel.magnitude_squared() > EFFECTIVE_ZERO:
                self.acc = -GRAVITY
            else:
                self.stopped_on_ground = True
        elif self.pos.y < self.radius and self.vel.y < 0:
            self.vel.reflect_ip(pygame.math.Vector2(0, 1))
        
            
            