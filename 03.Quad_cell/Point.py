class Point:
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, p: 'P'):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p: 'P'):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, c: float):
        return Point(self.x * c, self.y * c)

    def to_array(self):
        return [self.x, self.y]