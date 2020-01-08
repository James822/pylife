from typing import List

from point import Point
from cell import Cell


def grid_create(dim: int, points: List[Point]) -> List[List[Cell]]:
	ans = []
	for y in range(0, dim):
		lst = []
		for x in range(0, dim):
			if Point(x,y) in points:
				lst.append( Cell(True, Point(x,y)) )
			else:
				lst.append( Cell(False, Point(x, y)) )
		ans.append(lst)
	return ans



class Grid:

	dim: int
	grid: List[List[Cell]]

	def __init__(self, dim: int, alive_cells: List[Point]):
		self.dim = dim
		self.grid = grid_create(self.dim, alive_cells)

	def tick(self):
		# actual method where the rules of conway's game of life
		# are implemented
		for row in self.grid:
			for cell in row:
				cell.set_next(self.dim, self.grid)
		for row in self.grid:
			for cell in row:
				cell.update()

	def __str__(self):
		ans = ""
		for row in self.grid:
			for cell in row:
				if cell.state:
					ans += "#"
				else:
					ans += " "
			ans += '\n'

		return ans


if __name__ == "__main__":
	g = Grid(10, [Point(1,0), Point(1, 1), Point(1, 2)] )
	print(g)
	g.tick()
	print(g)
	g.tick()
	print(g)
	g.tick()
	print(g)
