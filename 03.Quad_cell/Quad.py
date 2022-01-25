from Point import Point
class Quad:
	points = []
	def __init__(self, points = []):
		self.points = points


	@property
	def p1(self) -> Point: return self.points[0]
	@property
	def p2(self) -> Point: return self.points[1]
	@property
	def p3(self) -> Point: return self.points[2]
	@property
	def p4(self) -> Point: return self.points[3]

	@p1.setter
	def p1(self, p): self.points[0] = p
	@p2.setter
	def p2(self, p): self.points[1] = p
	@p3.setter
	def p3(self, p): self.points[2] = p
	@p4.setter
	def p4(self, p): self.points[3] = p

