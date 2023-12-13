class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def main():
	import math
	inp = input("Insert the coordinates of the first point: ")
	first_point = Point(float(inp.split(",")[0]), float(inp.split(",")[1]))
	inp = input("Insert the coordinates of the first point: ")
	second_point = Point(float(inp.split(",")[0]), float(inp.split(",")[1]))
	print("Their distance is:", (math.sqrt((first_point.x - second_point.x)**2 + (first_point.y - second_point.y)**2)))

if __name__ == "__main__":
	main()
