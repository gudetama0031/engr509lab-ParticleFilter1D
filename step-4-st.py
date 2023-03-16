import matplotlib.pyplot as plt
import numpy as np


class Robot1D:
    def __init__(self, pos):
        self.pos = pos
        self.dist_pole = 0


class Particle(Robot1D):
    def __init__(self, pos):
        Robot1D.__init__(self, pos)
        self.weight = 0
        self.measurement_sigma = 1.0

    def probability_density_function(self, mu, x):
        """Gaussian PDF with pre-defined standard deviation"""
        y = 1/(self.measurement_sigma * np.sqrt(2*np.pi)) * np.exp(-(mu-x)**2/(2*self.measurement_sigma**2))
        return y

    def weight_update(self, robot_measure):
        """your code here"""
        '''*****************************'''
        # around one line of code here
        '''*****************************'''


# Plot Weights for a list of robot measurements.
particle = Particle(0.0)

x = np.arange(-5, 5, 0.01)  # robot measurements
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = particle.probability_density_function(0, x[i])

plt.plot(x, y, '-r')
plt.grid(True)
plt.show()

# Integrate left side to calculate probablity.
sum_probability = 0
for i in range(int(len(y) / 2)):
    sum_probability += y[i]

print("If Probability is close to 0.5, then PDF works.")
print("Integrate left side of the PDF is: ", round(sum_probability * 0.01, 2))
print()

# Update Particle Weigth based on robot measurement.
robot_measure = 3.0
particle.dist_pole = 1.0
particle.weight_update(robot_measure)
print("Particle Weight: " + str(round(particle.weight, 2)))
plt.plot(x, y, '-r')
plt.plot([-5, 5], [particle.weight, particle.weight], '-b')
plt.grid(True)
plt.show()
