import unittest
from atribute import Atribute

class atribute_test(unittest.TestCase):
 
    def test1(self):
        skill1 = Atribute("str", 18, 0, True, 2)
        self.assertEqual(skill1.get_name(), "str")
    
    def test2(self):
        skill2 = Atribute("str", 18, 0, True, 2)
        self.assertEqual(skill2.get_val(), 18)
    
    def test3(self):
        skill3 = Atribute("str", 18, 0, True, 2)
        self.assertEqual(skill3.get_bonuse(), 0)
       
if __name__ == "__main__":
      unittest.main()




