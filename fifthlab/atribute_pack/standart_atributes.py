from atribute_pack.atribute import Atribute
class Strenth(Atribute):
    def __init__(self, val:int, bonuse:int, mastered:bool, mastered_val:int, mastered_atletic: bool):   
        self._name = "Сила"
        self.set_atribute_skill("Атлетика", mastered_atletic)
    def get_atletic_value(self):
            self.get_skill("Атлетика").get_val()

class Agility(Atribute):
    def __init__(self, val:int, bonuse:int, mastered:bool, mastered_val:int, mastered_acrobatic: bool, mastered_hands: bool, mastered_stealth: bool):   
        self._name = "Ловкость"
        self.set_atribute_skill("Акробатика", mastered_acrobatic)
        self.set_atribute_skill("Ловкость_рук", mastered_hands)
        self.set_atribute_skill("Скрытность", mastered_stealth)

class Body(Atribute):
    def __init__(self, val:int, bonuse:int, mastered:bool, mastered_val:int):  
        super().__init__("Телосложение", val, bonuse, mastered, mastered_val)
    def test(setlf):
        print("Использован класс Body")
        super().test()

class Intelligence(Atribute):
    def __init__(self, val:int, bonuse:int, mastered:bool, mastered_val:int, mastered_analysis: bool, mastered_story: bool, mastered_magic: bool, mastered_nature: bool, mastered_religion: bool):   
        self._name = "Интелект"
        self.set_atribute_skill("Анилиз", mastered_analysis)
        self.set_atribute_skill("История", mastered_story)
        self.set_atribute_skill("Магия", mastered_magic)
        self.set_atribute_skill("Природа", mastered_nature)
        self.set_atribute_skill("Религия", mastered_religion)


class Wisdom(Atribute):
    def __init__(self, val:int, bonuse:int, mastered:bool, mastered_val:int, mastered_attentiveness:bool, mastered_survival:bool, mastered_medicine:bool, mastered_insight:bool, mastered_animal_care:bool):   
        self.set_atribute_skill("Внимательность", mastered_attentiveness)
        self.set_atribute_skill("Выживание", mastered_survival)
        self.set_atribute_skill("Медицина", mastered_medicine)
        self.set_atribute_skill("Проницательность", mastered_insight)
        self.set_atribute_skill("Уход за животными", mastered_animal_care)

class Charisma(Atribute):
    def __init__(self, val:int, bonuse:int, mastered:bool, mastered_val:int, mastered_performance:bool, mastered_intimidation:bool, mastered_cheating:bool, mastered_conviction:bool):   
        self._name = "Харизма"
        self.set_atribute_skill("Выступление", mastered_performance)
        self.set_atribute_skill("Запугивание", mastered_intimidation)
        self.set_atribute_skill("Обман", mastered_cheating)
        self.set_atribute_skill("Убеждение", mastered_conviction)
                             
if __name__ == "__main__":
    str = Strenth(14, 0, True, 2, True)
    agl = Agility(13, 0, True, 2, False, False, False)
    bod = Body(13, 0, True, 2)
    print(str.check_skill("Атлетика"))
    bod.test()