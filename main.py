"""
main file, this should be the file that is run
"""

from random import randint
from time import sleep

from point import Point
from grid import Grid

def get_initial_grid(s: str):
	if s == "default":
		dim = 65
		alive_points = []
		rbound = randint(0, dim*dim)
		for x in range(0, rbound):
			r1 = randint(0, dim)
			r2 = randint(0, dim)
			if Point(r1, r2) not in alive_points:
				alive_points.append(Point(r1, r2))
		return Grid(dim, alive_points)

def main(s: str):
	grid = get_initial_grid(s)
	print(grid)
	while(True):
		sleep(.15)
		grid.tick()
		print(grid)

if __name__ == "__main__":
	main("default")
