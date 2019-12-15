import atribute_pack.standart_atributes as st
class Race(object):
    _race_name = str()
    _size = int()
    _speed = int()
    _worldview = str()
    _atribute_bonuse = dict()
    _atributes = dict()

    def create_standart_atributes(self):
        self._atributes["Сила"] = st.Strenth(14, 0, True, 2, True)



if __name__ == "__main__":
    rase = Race()
    rase.create_standart_atributes()
