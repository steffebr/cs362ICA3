import unittest
import calc

class TestSum(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calc.add(2,2), 4)

	def test_AddNegativeOne(self):
		self.assertEqual(calc.add(4,-1), 3)

	def test_AddNegativeBoth(self):
		self.assertEqual(calc.add(-2,-3), -5)


	def test_SubPositive(self):
		self.assertEqual(calc.sub(5,3), 2)

	def test_SubPositiveBackwards(self):
		self.assertEqual(calc.sub(3,5), -2)

	def test_SubNegativeOne(self):
		self.assertEqual(calc.sub(5,-3), 8)

	def test_SubNegativeBoth(self):
		self.assertEqual(calc.sub(-5,-3), -2)


	def test_MulPositive(self):
		self.assertEqual(calc.mul(4, 3), 12)

	def test_MulNegativeOne(self):
		self.assertEqual(calc.mul(4, -3), -12)

	def test_MulNegativeBoth(self):
		self.assertEqual(calc.mul(-4, -3), 12)

	def test_MulZero(self):
		self.assertEqual(calc.mul(0, 3), 0)

	def test_MulOne(self):
		self.assertEqual(calc.mul(1, 7), 7)


	def test_DivPositiveEvenly(self):
		self.assertEqual(calc.div(21, 7), 3)

	def test_DivPositiveNotEvenly(self):
		self.assertEqual(calc.div(25, 10), 2.5)

	def test_DivNegativeOne(self):
		self.assertEqual(calc.div(21, -7), -3)

	def test_DivNegativeBoth(self):
		self.assertEqual(calc.div(-21, -7), 3)

if __name__ == "__main__":
	unittest.main()