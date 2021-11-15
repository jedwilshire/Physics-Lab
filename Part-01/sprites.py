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
        if abs(self.vel.y) < EFFECTIVE_ZERO:
            self.vel.y = 0
        if abs(self.vel.x) < EFFECTIVE_ZERO:
            self.vel.x = 0
            
        # set self.friction to self.vel * FRICTION * self.app.dt         
        
        # change velocity vector by friction by subtracting friction from it       
        
        # change velocity vector using v = v + a*t.  a is self.acc and t is self.app.dt        
        
        # change position using p = 1/2*a*t^2 + v * t + p p is self.pos        
        
        # call self.bounce()
        
        # set the center of the particles rect to self.pos        
        
    
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
        # and move the pos of the ball to be a radius away from wall.
        if self.touching_left_wall() and self.vel.x < 0:
            # change vel to reflect off left wall's normal times elasticity
            self.vel = self.vel.reflect(LEFT_WALL_NORMAL) * ELASTICITY
            # move self.pos.x to a radius away from left wall
            self.pos.x = self.radius
        elif self.touching_right_wall() and self.vel.x > 0:
            # similar to touching left wall portion
            
        elif self.touching_top_wall() and self.vel.y < 0:
            # reflect off top wall
            # set self.pos.y to be a radius length down from top
        elif self.touching_bottom_wall() and self.vel.y > 0:
            # simliar to top wall bounce
            # set self.pos.y to be a radius length up from bottom
            
            
            
            
            
        
        
        
