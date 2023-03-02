
class Robot1D:
    def __init__(self, pos):
        self.pos = pos
        self.dist_pole = -1000  # measurement: distance to the pole
        self.max_range = 3

    # Measurement is perfectly accurate in this simulator
    # even though particles assuming it isn't.
    def measure(self, poles):
        # Set self.pole_dist to the distance to the closest pole.
        """your code here"""
        '''*****************************'''
        # around 9-10 lines of code here
        '''*****************************'''

class Particle(Robot1D):
    def __init__(self, pos):
        Robot1D.__init__(self, pos)



poles = [1, 10]
particle = Particle(0.1)
particle.measure(poles)
print("Measurement Should Be 0.9")
print("You Measured: " + str(round(particle.dist_pole, 1)))
print()

particle.pos = 11
particle.measure(poles)
print("Measurement Should Be -1000")
print("You Measured: " + str(round(particle.dist_pole, 1)))
print()

particle.pos = 6.9
particle.measure(poles)
print("Measurement Should Be -1000")
print("You Measured: " + str(round(particle.dist_pole, 1)))
print()

particle.pos = 7.1
particle.measure(poles)
print("Measurement Should Be 2.9")
print("You Measured: " + str(round(particle.dist_pole, 1)))
print()

particle.pos = 9.5
particle.measure(poles)
print("Measurement Should Be 0.5")
print("You Measured: " + str(round(particle.dist_pole, 1)))
print()
