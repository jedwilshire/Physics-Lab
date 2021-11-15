import pygame
from settings import *

class Particle(pygame.sprite.Sprite):
    def __init__(self, application, x, y, speed, angle, radius, color):
        # call super constructor from Sprite class
        super().__init__()
        # create self.pos - a vector for position
        self.pos = pygame.math.Vector2(x, y)
        # create self.vel - a vector for velocity with magnitude speed and direction angle
        self.vel = pygame.math.Vector2(speed, 0).rotate(angle)
        # create self.acc - a vector for acceleration set to (0, GRAVITY)
        self.acc = pygame.math.Vector2(0, GRAVITY)
        # create self.radius to store the radius property
        self.radius = radius
        # create self.image a surface with width and height equal to the diameter
        self.image = pygame.Surface( (radius * 2, radius * 2) )
        # draw a circle with color parameter onto the self.image surface centered in center of surface
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        # make BLACK color transparent
        self.image.set_colorkey(BLACK)
        # create self.rect using the image
        self.rect = self.image.get_rect()
        # position center of particle's rect using self.po
        self.rect.center = self.pos
        # create self.app a reference back to application
        self.app = application
        # add self to self.app.particles_group
        self.app.particles_group.add(self)

        
    def update(self):
        if abs(self.vel.y) < EFFECTIVE_ZERO:
            self.vel.y = 0
        if abs(self.vel.x) < EFFECTIVE_ZERO:
            self.vel.x = 0
            
        # set self.friction to self.vel * FRICTION * self.app.dt
        self.friction = self.vel * FRICTION * self.app.dt
        
        # change velocity vector by friction by subtracting friciton from it
        self.vel -= self.friction
        
        # change velocity vector using v = v + a*t.  a is self.acc and t is self.app.dt
        self.vel += self.acc * self.app.dt
        
        # change position using p = 1/2*a*t^2 + v * t + p p is self.pos
        self.pos +=  1 / 2 * self.acc * self.app.dt ** 2 + self.vel * self.app.dt
                     
        # set the center of the particles rect to self.pos
        self.bounce()
        self.rect.center = self.pos
    
    def touching_left_wall(self):
        # if x pos is within radius of left wall
        return self.pos.x <= self.radius
    
    def touching_right_wall(self):
        return self.pos.x >= WIDTH - self.radius - 1
    
    def touching_top_wall(self):
        return self.pos.y <= self.radius
    
    def touching_bottom_wall(self):
        # moving down and touching bottom
        return self.pos.y >= HEIGHT - self.radius - 1
    
    def bounce(self):
        # if ball is touching left, right, top, or bottom wall AND moving towards it
        # then set self.vel to self.vel.reflect(normal) * ELASTICITY
        if self.touching_left_wall() and self.vel.x < 0:
            self.vel = self.vel.reflect(LEFT_WALL_NORMAL) * ELASTICITY
            self.pos.x = self.radius
        elif self.touching_right_wall() and self.vel.x > 0:
            self.vel = self.vel.reflect(RIGHT_WALL_NORMAL) * ELASTICITY
            self.pos.x = WIDTH - self.radius
        elif self.touching_top_wall() and self.vel.y < 0:
            self.vel = self.vel.reflect(TOP_WALL_NORMAL) * ELASTICITY
            self.pos.y = self.radius
        elif self.touching_bottom_wall() and self.vel.y > 0:
            self.vel = self.vel.reflect(BOTTOM_WALL_NORMAL) * ELASTICITY
            self.pos.y = HEIGHT - self.radius
            
            
            
            
            
        
        
        