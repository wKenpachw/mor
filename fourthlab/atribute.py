import random
import math
from atribute_pack.atribute_skill import Atribute_skill

class Atribute(object):
    _name           = str()
    _val            = int()
    _bonuse         = int()
    _mastered       = bool()
    _mastered_val   = int()
    _modificator    = int()
    _atribute_skills = dict()

    def __init__(self, name:str, val:int, bonuse:int, mastered:bool, mastered_val:int):   
        self._name = name
        self._val = val
        self._bonuse = bonuse
        self.set_modificator()
        self._modificator = self.get_modificator()
        self._mastered = mastered
        self._mastered_val = mastered_val
        #val_to_modificator = lambda x, y: ceil(((x + y) - 1)/2) - 5

    def set_modificator(self):
        val_to_modificator = lambda x, y: math.ceil(((x + y) - 1)/2) - 5
        self._modificator = val_to_modificator(self._val,self._bonuse)

    def get_modificator(self):
        return self._modificator

    def get_rand_save_value(self):
        result = int(random.randint(1, 20)) + int(self.get_modificator())
        if self._mastered:
            result == result + self._mastered_val
        return result

    def set_atribute_skill(self, name:str, mastred_skill:bool):
        new_skill = Atribute_skill(name, self._modificator, mastred_skill, self._mastered_val)
        self._atribute_skills[name] = new_skill

    def get_skill(self, name:str):
        return self._atribute_skills[name]

    def get_name(self):
        return self._name

    def get_val(self):
        return self._val

    def get_bonuse(self):
        return self._bonuse

    def check_skill(self, name:str):
        return self._atribute_skills[name].check_skill()

    def get_skill_modify(self, name:str):
        return self._atribute_skills[name].get_val()

    def test(self):
        """метод тест для вывода иерархии"""
        print("использован класс Atribute")

if __name__ == "__main__":
    test_atr = Atribute("str", 18, 0, True, 2)
    print("name = " + test_atr.get_name())
    print("val = " + str(test_atr.get_val()))
    print("bonuse = " + str(test_atr.get_bonuse()))
    print("modificator = " + str(test_atr.get_modificator()))
    print("mastered = " + str(test_atr._mastered))
    print("save_value = " + str(test_atr.get_rand_save_value()))
    print("создадим навык атрибута с имененм skil1 и с бонусом мастерства")
    test_atr.set_atribute_skill("skil1", True)
    print("Значение имя навыка = " + str(test_atr.get_skill("skil1").get_name()))
    print("Значение модификатора навыка = " + str(test_atr.get_skill_modify("skil1")))
    print("Значение спасброска навыка = " + str(test_atr.check_skill("skil1")))
    print(test_atr.test())
    
