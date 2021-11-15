import pygame, random
from sprites3 import Particle
from settings import *

class Application:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        pygame.display.set_caption('Particle Simulation')
        
        # a group of all sprites in this game
        self.particles = pygame.sprite.Group()
        
        self.clock = pygame.time.Clock()
        self.make_particles()
    
    def make_particles(self):
        for i in range(NUMBER_PARTICLES):
            radius = random.randint(MIN_SIZE, MAX_SIZE)
            x = random.randint(radius, WIDTH - radius)
            y = random.randint(radius, HEIGHT - radius)
            speed = random.randint(MIN_SPEED, MAX_SPEED)
            angle = random.randint(0, 360)
            p = Particle(self, x, y, radius, angle, speed)

    

    
    def gameloop(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000 # get time in milliseconds since last frame
            self.event_update()
            self.game_update()
            self.game_draw()
                    
    def game_draw(self):   
        self.screen.fill(WHITE)
        # draw all sprites to screen
        for particle in self.particles:
            particle.draw(self.screen)
        
        pygame.display.flip()
    
    def game_update(self):
        self.particles.update()

        
    def event_update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
    
def main():
    app = Application()
    app.gameloop()
    pygame.quit()

if __name__ == '__main__':
    main()
                
                
                
  
  
  
  
  
                
