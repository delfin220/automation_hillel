import unittest
import homeworks


# test_homeworks08.py
import unittest
from homeworks import totalsum, count_unique, h_letter, Student


class TestFilterStrings(unittest.TestCase):

   def test_totalsum(self):
       self.assertEqual(totalsum([2,4]), 6)
   def test_empty(self):
       self.assertEqual(totalsum([]), 0)
   def test_not_even(self):
        self.assertEqual(totalsum([1,5]), 0)

class TestCountUniqie(unittest.TestCase):
    def test_empty(self):
        self.assertFalse(count_unique(""))
    def test_unique_symbol(self):
        self.assertTrue(count_unique("abcdefghijk"))
    def test(self):
        self.assertFalse(count_unique("abc"))

class TestCountHLetter(unittest.TestCase):
    def test_empty(self):
        self.assertFalse(h_letter(""))
    def test_h_letter_include_lower_reg(self):
        self.assertTrue(h_letter("hello"))
    def test_h_letter_include_upper_reg_in_middle(self):
        self.assertTrue(h_letter("justHtest"))

class TestStudent(unittest.TestCase):
    def test_get_infp(self):
        student = Student("Andrii", "Terzeman", 30, 60)
        self.assertEqual(student.get_info(), "Student's name:, Andrii Terzeman, age: 30, average score: 60 ")

    def test_check_average_score(self):
        student = Student("Andrii", "Terzeman", 60, 30)
        student.set_average_score(70)
        self.assertEqual(student.average_score, 70)

    def test_info_returns_str(self):
        student = Student("Andrii", "Terzeman", 30, 60)
        self.assertIsInstance(student.get_info(), str)





if __name__ == "__main__":
    unittest.main()