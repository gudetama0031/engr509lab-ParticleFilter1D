import random
import numpy as np


class Robot1D:
    def __init__(self, pos):
        self.pos = pos
        self.move_dist = 1


class Particle(Robot1D):
    def __init__(self, pos):
        Robot1D.__init__(self, pos)
        self.weight = 0
        self.movement_sigma = 1
        self.move_dist = 1  # Overwrite move distance for this example
        self.color = (0, 0, 1, 1) # just for display, you can ignore this line

    def sample_motion(self):
        # Predict the robots movement and account for movement uncertainty.
        """your code here"""
        '''****************'''
        # around 1-2 lines of code here
        '''****************'''


def resample_particles(particles):
    # Returns a new set of particles obtained by performing
    # stochastic universal sampling, according to the particle weights.
    """your code here"""
    '''*************************************************'''
    # around 20 lines of code here
    '''************************************************'''
    return new_particles


num_particles = 10
map_length = 40
particles = []

# Set first few particles to different weight and color.
for i in range(num_particles):
    particles += [Particle(random.uniform(0, map_length))]
    if i < 3:
        particles[-1].weight = 1
        particles[-1].color = (1, 0, 0, 1)  # just for display, you can ignore this line
    else:
        particles[-1].weight = 0.1

# Resample Particles
resampled_particles = resample_particles(particles)
