from settings import *
from random import randint, choice
from sprites import Particle
import pygame


class Application:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.particles_group = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.running = True
        self.make_particles()
    
    def make_particles(self):
        # create colors a list of all colors except WHITE or BLACK from settings
        colors = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE]
        """ use a for to create as many particles as NUM_PARTICLES setting
            * Ech particle will need a random integer for x and y that is  
            anywhere on the screen at least MAX_RADIUS distance away from an edge  
            * Each particle needs a random integer for speed and radius between the
            min and max values set in the sttings
            * Each particle needs a random integer angle measure between 0 and 359
            * Each particle needs a random color choosen from the colors list
            * Note that randint(a, b) and choice(list) have been imported from the random module"""
            
        for i in range(NUM_PARTICLES):
            x = randint(MAX_RADIUS, WIDTH - MAX_RADIUS)
            y = randint(MAX_RADIUS, HEIGHT - MAX_RADIUS)
            speed = randint(MIN_SPEED, MAX_SPEED)
            radius = randint(MIN_RADIUS, MAX_RADIUS)           
            angle = randint(180, 360)
            Particle(self, x, y, speed, angle, radius, choice(colors))
            
    
    def application_loop(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.update_events()
            
            # update particle logic and positions
            self.particles_group.update()
            
            # update the screen
            self.update_screen()    
    
    def update_screen(self):
        self.screen.fill(WHITE)
        self.particles_group.draw(self.screen)
        pygame.display.flip()
    
    def update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
                    
                    
def main():
    pygame.init()
    app = Application()
    app.application_loop()
    pygame.quit()

if __name__ == '__main__':
    main()