import pygame
from settings import *

class Particle(pygame.sprite.Sprite):
    def __init__(self, application, x, y, speed, angle, radius, color):
        # call super constructor from Sprite class
        super().__init__()
        # create self.pos - a vector for position
        
        # create self.vel - a vector for velocity with magnitude speed and direction angle
        
        # create self.acc - a vector for acceleration set to (0, GRAVITY)
        
        # create self.radius to store the radius property
        
        # create self.image a surface with width and height equal to the diameter
        
        # draw a circle with color parameter onto the self.image surface centered in center of surface
        
        # make BLACK color transparent
        
        # create self.rect using the image
        
        # position center of particle's rect using self.po
        
        # create self.app a reference back to application
        
        # add self to self.app.particles_group
        

        
    def update(self):
        # call bounce method
        
        # IF the particle is not touching the bottom wall,
        # set self.acc.y = GRAVITY ELSE set self.acc.y to 0
        
        # set self.friction to self.vel * FRICTION * self.app.dt
        
        # change velocity vector using v = v + a*t.  a is self.acc and t is self.app.dt
        
        # change velocity vector by friction by subtracting friciton from it
        
        # change position using p = 1/2*a*t + v * t + p p is self.pos
        
        # set the center of the particles rect to self.pos
        
    
    def touching_left_wall(self):
        # if x pos is within radius of left wall return True
        
    
    def touching_right_wall(self):
        # return True if within radius of right wall
    
    def touching_top_wall(self):
        # similiar to others
    
    def touching_bottom_wall(self):
        # similiar to others
        
    
    def bounce(self):
        # if ball is touching left, right, top, or bottom wall AND moving towards it
        # then set self.vel to self.vel.reflect(normal) and set position's
        # proper component (Either x or y) at a radius distance away from wall
        # where normal is the Normal Vector from the settings for the side being bounced off
        if self.touching_left_wall() and self.vel.x < 0:
            
            
        elif self.touching_right_wall() and self.vel.x > 0:
            
            
        elif self.touching_top_wall() and self.vel.y < 0:
            
            
        elif self.touching_bottom_wall() and self.vel.y > 0:
            
            
            
            
            
            
        
        
        