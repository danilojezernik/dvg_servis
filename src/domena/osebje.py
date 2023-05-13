"""
Osebje bo sestavljeno iz serviserjev in nadrejenih. Oznaka se lahko dodaja ali spreminja. Oznake so: Serviser, Vodja vzdrževanja
"""


class Oseba:
    def __init__(self, serviser: str, vodja_servisa: str):
        self.serviser: str = serviser
        self.vodja_servisa: str = vodja_servisa