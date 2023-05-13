from src.domena.pomembno import Pomembno
from src.domena.popravljeno import Popravljeno


class Dvigalo:
    def __init__(self, id_dvigala: int, proizvajalec: str, naslov: str, leto_izdelave: int, leto_prenove: int,
                 zacetek_servisa: str, garancija: int, nosilnost: int, krmilje: str, vrsta_pogona: str):
        self.id_dvigala: int = id_dvigala
        self.proizvajalec: str = proizvajalec
        self.naslov: str = naslov
        self.leto_izdelave: int = leto_izdelave
        self.leto_prenove: int = leto_prenove
        self.zacetek_servisa: str = zacetek_servisa
        self.garancija: int = garancija
        self.nosilnost: int = nosilnost
        self.krmilje: str = krmilje
        self.vrsta_pogona: str = vrsta_pogona

        self.pomembno: list[Pomembno] = []
        self.popravilo: list[Popravljeno] = []
