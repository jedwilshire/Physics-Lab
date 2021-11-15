# Physics-Lab
A Python labratory for coding physics with pygame and pygame vectors.  Creates balls that bounce around screen.
This is a learning - coding lab. 
Each part of the lab has comments in the code to finish.
Solutions for each part can be found in the solutions folder.
Part-01 has the students create a bouncing balls simulations.
The balls can travel through each other - no ball collisions.
The position, velocity, and acceleration of the ball is 
set using pygame.math.Vector2 objects.
Motion is set using the following formulas:
friction = v * FRICTION * dt
where FRICTION is a coeficent of friction for air and walls
dv = a*dt - friction
dp = 1/2 * a * dt^2 + v * dt

collisions with walls result in the velocity vector
equaling the reflection of the vector over the vector normal
to the wall colliding * ELASTICITY
a constant for the efficency of the bounce.
