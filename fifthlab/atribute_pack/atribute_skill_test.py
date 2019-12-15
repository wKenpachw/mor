import unittest
from atribute_skill import Atribute_skill

class atribute_skill_test(unittest.TestCase):

    def test1(self):
        skill1 = Atribute_skill("Атлетика", 4, True, 2)
        self.assertEqual(skill1.get_name(), "Атлетика")
    
    def test2(self):
        skill2 = Atribute_skill("Атлетика", 4, True, 2)
        self.assertEqual(skill2.get_val(), 6)
   
   
if __name__ == "__main__":
    unittest.main()
