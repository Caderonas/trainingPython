class student:
	def __init__(self, name = "", grade = "lovelace"):
		self._name = name
		self._grade = grade

	def get_name(self):
		return self._name
	def get_grade(self):
		return self._grade
	def set_name(self, name):
		self._name = name
	def set_grade(self, grade):
		self._grade = grade

