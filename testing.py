import unittest

from Student import Student
from VirtualDiary import VirtualDiary

class TestStringMethods(unittest.TestCase):

	def testing_data(self):
		self._students1 = Student(1, "Janusz", "Tytanowy", "A", 3, [2, 3, 4])
		self._students2 = Student(2, "Adam", "Mleko", "A", 7, [4, 4, 4])
		self._students3 = Student(3, "Ania", "Podsiadlo", "B", 17, [2])]
	
	def add_students_test(self):
		self.assertEqual()
