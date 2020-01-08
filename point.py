class Point:

	x: int
	y: int

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y


if __name__ == "__main__":
	p = Point(1, 123)
	print(p.x, p.y)
	q = Point(1, 123)
	assert q == p
	assert not(p == Point(1, 1))
