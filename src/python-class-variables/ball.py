

class Ball:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_volume(self):
        return 4/3 * self.radius ** 3 * Ball.pi
