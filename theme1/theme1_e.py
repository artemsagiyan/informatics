class Mkad:
    def __init__(self, t, v, l=109):
        self.t = t
        self.v = v
        self.l = l

    def calculate_km(self):
        return (self.t * self.v) % self.l
