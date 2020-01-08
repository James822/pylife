from point import Point


class Cell:

	state: bool
	pos: Point
	next_state: bool

	def __init__(self, state: bool, pos: Point):
		self.state = state
		self.pos = pos
		self.next_state = None

	def set_next(self, dim: int, grid):
		alive_neighbours = 0
		for x in [-1, 0, 1]:
			for y in [-1, 0, 1]:
				i = self.pos.x + x
				j = self.pos.y + y
				if ( (i >= 0) and (j >= 0) and (i < dim) and (j < dim) and not(x==0 and y==0) ):
					if grid[j][i].state:
						alive_neighbours += 1
		if (self.state and (alive_neighbours == 2 or alive_neighbours == 3)):
			self.next_state = True
		elif not(self.state) and alive_neighbours == 3:
			self.next_state = True
		else:
			self.next_state = False


	def update(self):
		self.state = self.next_state


if __name__ == "__main__":
	cell = Cell(True, Point(2,2))
	print(cell.pos.x, cell.pos.y)

