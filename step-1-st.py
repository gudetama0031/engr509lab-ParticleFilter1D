from plot import plot_simple
import random


class Robot1D:
    def __init__(self, pos):
        self.pos = pos   # robot position
        self.pole_detected = False   # sensor measurement: pole detected or not
        self.move_unit = 1    # move distance

    def move(self):
        self.pos += self.move_unit

    def detect_pole(self, poles):
        if self.pos + 1 in poles:
            self.pole_detected = True
        else:
            self.pole_detected = False


class Particle(Robot1D):   # Derived class
    def __init__(self, pos, color):
        Robot1D.__init__(self, pos)
        self.belief = 1   # The init posterior (or the prior)
        self.color = color

    def sample_move(self):
        # Move the particle the same distance as the robot moves.
        """your code here"""
        '''****************'''
        # one line of code here
        '''****************'''

    def measure_update(self, robot_pole_detected):
        # Update the posterior based on the sensor measurement:
        # Set the belief to 0 if the robot detection and the particle detection
        # don't match.
        """your code here"""
        '''****************'''
        # around two lines of code here
        '''****************'''


# Setup Robot Location
robot = Robot1D(pos=2)  # position is at the spot #2
poles = [5, 9, 13]

# Setup particles
num_of_locations = 40
particle_spacing = 1
print("Starting Number of Particles: " +
      str(int(num_of_locations / particle_spacing)))
particles = []
for i in range(0, num_of_locations, particle_spacing):
    color = (random.random(), random.random(), random.random(), 1)
    particles += [Particle(i, color)]  # i--the particle initial position

# Plot starting distribution, no beliefs
plot_simple(particles, poles)

# Begin Calculating
for j in range(12):
    # Move
    if j != 0:
        robot.move()  # the default move distance was set to be
        for particle in particles:
            particle.sample_move()

    # Measure and Correct
    robot.detect_pole(poles)  # change the self.pole_detected value--True or False
    for particle in particles:
        particle.detect_pole(poles)

        # Update Beliefs
        particle.measure_update(robot.pole_detected)

    plot_simple(particles, poles, robot.pos, j)
