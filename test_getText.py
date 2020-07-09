from getText import *
import unittest

class TestText(unittest.TestCase):

    def test_output(self):
        self.assertEqual(processInput("123456.78"),"Rs. One Lakh Twenty Three Thousand Four Hundred And Fifty Six 78/100 ONLY")
        self.assertEqual(processInput("3456"),"Rs. Three Thousand Four Hundred And Fifty Six ONLY")
        self.assertEqual(processInput("80098.64"),"Rs. Eighty Thousand Ninety Eight 64/100 ONLY")
        self.assertEqual(processInput("768.3"),"Rs. Seven Hundred And Sixty Eight 3/10 ONLY")
        self.assertEqual(processInput("46.1"),"Rs. Forty Six 1/10 ONLY")
        self.assertEqual(processInput("1.2"),"Rs. One 2/10 ONLY")
        self.assertEqual(processInput("10.91"),"Rs. Ten 91/100 ONLY")
        self.assertEqual(processInput("55.3"),"Rs. Fifty Five 3/10 ONLY")
        self.assertEqual(processInput("777"),"Rs. Seven Hundred And Seventy Seven ONLY")
        self.assertEqual(processInput("10000"),"Rs. Ten Thousand ONLY")
        self.assertEqual(processInput("16899.87"),"Rs. Sixteen Thousand Eight Hundred And Ninety Nine 87/100 ONLY")
        self.assertEqual(processInput("400"),"Rs. Four Hundred ONLY")
        self.assertEqual(processInput("18.55"),"Rs. Eighteen 55/100 ONLY")
    
    def test_input(self):
        self.assertRaises(TypeError)