class Atribute_skill(object):
    _name           = str()
    _val            = int()
    _atr_val        = int()
    _mastered       = bool()
    _mastered_val   = int()

    def  __init__(self, name: str, atr_mod_value: int, mastered: bool, mastered_val:int ):
        self._name = name
        self._mastered = mastered
        self._mastered_val = mastered_val
        self.set_mastered_val()
        self._atr_val = atr_mod_value
        self._val = self.get_val()

    def set_mastered_val(self):
        if self._mastered:
            self._mastered_val = self._mastered_val
        else:
            self._mastered_val = 0

    def get_val(self):
        res = self._atr_val + self._mastered_val
        return res

    def get_name(self):
        return self._name

    def get_mastered(self):
        return self._mastered

if __name__ == "__main__":
    skill = atribute_skill("atl", 4, True, 2)
    print("значение атрибута = " + str(skill._atr_val))
    print("добавить бонус мастерства? ответ:" + str(skill._mastered))
    print("бонус мастерства = " + str(skill._mastered_val))
    print("значение навыка = " + str(skill._val))