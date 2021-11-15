from settings import *
from random import randint, choice
from sprites import Particle
import pygame


class Applicaiton:
    def __init__(self):
        self.screen = pygame.set_mode(WIDTH, HEIGHT)
        self.particles_group = pygame.sprite.Group()
        self.clock = pygame.Clock()
        self.running = True
        self.make_particles()
    
    def make_particles(self):
        colors = [RED, GREEN, BLUE, YELLOW, PURPLE, BLACK, ORANGE]
        for i in range NUM_PARTICLES:
            x = randint(MAX_RADIUS, WIDTH - MAX_RADIUS)
            y = randint(MAX_RADIUS, HEIGHT - MAX_RADIUS)
            speed = randint(MIN_SPEED, MAX_SPEED)
            radius = randint(MIN_RADIUS, MAX_RADIUS)
            angle = randint(0, 359)
            Particle(self, x, y, speed, angle, radius, choice(colors))
            
    
    def application_loop(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.update_events()
            
            # update particle logic and positions
            self.particles.update()
            
            # update the screen
            self.update_screen()    
    
    def update_screen(self):
        self.screen.fill(WHITE)
        self.particles.draw()
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