import random
from atribute_skill import Atribute_skill

class Atribute(object):
    _name           = str()
    _val            = int()
    _bonuse         = int()
    _mastered       = bool()
    _mastered_val   = int()
    _modificator    = int()
    _val_to_modificator = {1:-5, 2:-4, 3:-4, 4:-3, 5:-3, 6:-2, 7:-2, 8:-1, 9:-1, 10:0, 11:0, 12:1, 13:1, 14:2, 15:2, 16:3, 17:3, 18:4, 19:4, 20:5, 21:5, 22:6, 23:6, 24:7, 25:7, 26:8, 27:8, 28:9, 29:9, 30:10}
    _atribute_skills = dict()

    def __init__(self, name:str, val:int, bonuse:int, mastered:bool, mastered_val:int):   
        self._name = name
        self._val = val
        self._bonuse = bonuse
        self.set_modificator()
        self._modificator = self.get_modificator()
        self._mastered = mastered
        self._mastered_val = mastered_val

    def set_modificator(self):
        self._modificator = self._val_to_modificator[self._val + self._bonuse]

    def get_modificator(self):
        return self._modificator

    def get_rand_save_value(self):
        result = int(random.randint(0, 20)) + int(self.get_modificator())
        if self._mastered:
            result == result + self._mastered_val
        return result

    def set_atribute_skill(self, name:str, mastred_skill:bool):
        new_skill = Atribute_skill(name, self._modificator, mastred_skill, self._mastered_val)
        self._atribute_skills[name] = new_skill

    def get_skill(self, name:str):
        return self._atribute_skills[name]

    def test(self):
        """метод тест для вывода иерархии"""
        print("использован класс Atribute")

if __name__ == "__main__":
    test_atr = Atribute("str", 8, 8, True, 2)
    print("name = " + test_atr._name)
    print("val = " + str(test_atr._val))
    print("bonuse = " + str(test_atr._bonuse))
    print("modificator = " + str(test_atr.get_modificator()))
    print("mastered = " + str(test_atr._mastered))
    print("save_value = " + str(test_atr.get_rand_save_value()))
    print("создадим навык атрибута с имененм skil1 и с бонусом мастерства")
    test_atr.set_atribute_skill("skil1", True)
    print("Значение имя навыка = " + str(test_atr.get_skill("skil1").get_name()))
    print("Значение модификатора навыка = " + str(test_atr.get_skill("skil1").get_val()))
    print(test_atr.test())
