import matplotlib.pyplot as plt
import numpy as np


class Robot1D:
    def __init__(self, pos):
        self.pos = pos
        self.move_dist = 1

    # Movement is perfectly accurate in this simulator,
    # even though we are assuming it isn't.
    def move(self):
        self.pos += self.move_dist


class Particle(Robot1D):
    def __init__(self, pos):
        Robot1D.__init__(self, pos)
        self.movement_sigma = 0.2

    def sample_motion(self):
        # Predict the robots movement and account for movement uncertainty.
        """your code here"""
        '''****************'''
        # around two lines of code here
        '''****************'''

particle = Particle(0)
# Move 10 times.
print("Particle Pos: " + str(particle.pos))
for i in range(10):
    particle.sample_motion()
    print(f"Particle {i+1} Pos: " + str(particle.pos))

# Uncomment quit() to see how distribution converges with more samples.
quit()

sample_count = 1
for i in range(8):
    x = np.random.normal(
        particle.move_dist,
        particle.movement_sigma,
        sample_count)

    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, facecolor='green', alpha=0.75)
    plt.grid(True)
    plt.xlim([0, 2])
    print(sample_count)
    plt.show(block=False)
    plt.pause(2)
    if i == 7:
        plt.pause(100)
        break
    plt.close()

    sample_count *= 10
