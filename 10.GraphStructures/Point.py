import numpy as np


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def to_array(self):
        return [self.x,self.y]

    def move(self, n_x_y):
            self.x = self.x + n_x_y[0]
            self.y = self.y + n_x_y[1]

            if(self.x < 0.0): self.x = 0.0
            if(self.x > 255.0): self.x = 255.0

            if(self.y < 0.0): self.y = 0.0
            if(self.y > 255.0): self.y = 255.0


    def rounded(self):
        x_t, y_t = np.int16(np.around((self.x, self.y)))
        return y_t, x_t

