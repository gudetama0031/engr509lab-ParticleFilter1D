import numpy as np
import random
from plot import plot, print_particle_error

AUTORUN = True
robot_start = 7
num_particles = 20
map_length = 40
poles = [10, 15, 17, 19, 30, 39]


class Robot1D:
    def __init__(self, pos):
        self.pos = pos
        self.dist_pole = -100
        self.max_range = 3
        self.move_dist = 1

    # Movement is perfectly accurate in this simulator,
    # even though we are assuming it isn't.
    def move(self):
        self.pos += self.move_dist

    # Measurement is perfectly accurate in this simulator
    # even though we are assuming it isn't.
    def measure(self, poles):
        # Set self.pole_dist to the distance to the closest pole.
        """your code here"""
        '''*****************************'''

        '''*****************************'''



class Particle(Robot1D):
    def __init__(self, pos):
        Robot1D.__init__(self, pos)
        self.weight = 0
        self.movement_sigma = 0.2
        self.measurement_sigma = 1.0

    def sample_motion(self):
        self.pos += np.random.normal(self.move_dist, self.movement_sigma)

    def probability_density_function(self, mu, x):
        """Gaussian PDF with pre-defined standard deviation"""
        y = 1/(self.measurement_sigma * np.sqrt(2*np.pi)) * np.exp(-(mu-x)**2/(2*self.measurement_sigma**2))
        return y

    def weight_update(self, robot_measure):
        """your code here"""
        '''*****************************'''
        '''*****************************'''


def resample_particles(particles):
    # Returns a new set of particles obtained by performing
    # stochastic universal sampling, according to the particle weights.
    """your code start here"""
    '''**************************'''

    '''**************************'''
    return resampled_particles



def initialize_particles(particles):
    pos_even = map_length / num_particles
    for i in range(num_particles):
        particles += [Particle(i*pos_even)]
    return particles



robot = Robot1D(robot_start)

# Setup particles.
particles = []
initialize_particles(particles)

# Plot starting distribution, no beliefs
plot(particles, poles, robot.pos)

# Begin computating
for j in range(39 - robot.pos):
    # Move
    if j != 0:
        robot.move()
        for particle in particles:
            particle.sample_motion()

    # Measure
    robot.measure(poles)
    for particle in particles:
        particle.measure(poles)

        # Update Beliefs
        particle.weight_update(robot.dist_pole)

    print_particle_error(robot, particles)

    # Resample
    resampled_particles = resample_particles(particles)
    plot(particles, poles, robot.pos, resampled_particles, j, AUTORUN)
    particles = resampled_particles

plot(particles, poles, robot.pos, resampled_particles)
