class Robot :
	""" Direction is use by his index in list : """
	direction = ["north", "east", "south", "west"]

	""" Getter and Setter for X, Y and direction (index)"""
	def __init__(self, x = 0, y = 0, direction = "north"):
		self._x = x
		self._y = y
		self._direction = direction
	def get_x(self):
		return self._x
	def get_y(self):
		return self._y
	def get_direction(self):
		return self.direction[self._direction]
	def set_x(self, x):
		self._x = x
	def set_y(self, y):
		self._y = y
	def set_direction(self, current):
		self._direction = self.direction.index(current)

	""" Functions of simulation """
	def turn_right(self):
		if self._direction == 4:
			self._direction = 0
		else:
			self._direction += 1
	def turn_left(self):
		if self._direction == 0:
			self._direction = 4
		else:
			self._direction -= 1
	def advance(self):
		if self._direction == 0:
			self._y -= 1
		if self._direction == 2:
			self._y += 1
		if self._direction == 3:
			self._x += 1
		if self._direction == 1:
			self._x -= 1

	""" Main simulation """
	def robotSimulator(self, string):
		for i in string:
			if i == 'R':
				self.turn_right()
			if i == 'L':
				self.turn_left()
			if i == 'A':
				self.advance()
			print ("Direction, x and y : "+i)
			print (self._direction)
			print ([self._x, self._y])
		return [self._x, self._y]

""" Tests zone """
robot = Robot()
robot.set_x(7)
robot.set_y(3)
robot.set_direction("north")
robot.robotSimulator("RAALAL")
print (robot.get_x())
print (robot.get_y())



