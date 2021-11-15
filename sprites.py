import pygame
from settings import *

class Particle(pygame.sprite.Sprite):
    def __init__(self, application, x, y, speed, angle, radius, color):
        # create self.pos - a vector for position
        self.pos = pygame.math.Vector2(x, y)
        # create self.vel - a vector for velocity with magnitude speed and direction angle
        self.vel = pygame.math.Vector2(speed, 0).rotate(angle)
        # create self.acc - a vector for acceleration set to new Vector2(GRAVITY)
        self.acc = pygame.math.Vector2(GRAVITY)
        # create self.radius to store the radius property
        self.radius = radius
        # create self.image a surface with width and height equal to the diameter
        self.image = pygame.Surface( (radius * 2, radius * 2) )
        # draw a circle with color parameter onto the self.image surface centered in center of surface
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        # make WHITE color transparent
        self.image.set_colorkey(WHITE)
        # create self.rect using the image
        self.rect = self.image.get_rect()
        # create self.app a reference back to application
        self.app = application
        
    def update(self):
        # call the bounce method
        
        # change velocity vector using v = v + a*t.  a is self.acc and t is self.app.dt
        self.vel += self.acc * self.app.dt
        # change position using p = 1/2*a*t + v * t + p p is self.pos
        self.pos += 1 / 2 * self.acc * self.app.dt + self.vel * self.app.dt
    
    def bounce(self):
        # if ball is within self.radius of left, right, top, or bottom AND moving in that direction
        # then reflect_ip self.vel by the normal vector for its side
        if self.pos <= self.radius and self.vel.x < 0:
            self.vel.reflect_ip(
            
        
        
        