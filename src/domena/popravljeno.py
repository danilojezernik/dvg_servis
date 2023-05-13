"""
Delovanje: V primeru, da bo dvigalo zaustavljeno bo vrednost False, v primeru delovanja bo vrednost True
Popravilo: Opis popravil
"""


class Popravljeno:
    def __init__(self, popravilo: str, delovanje: bool):
        self.popravilo: str = popravilo
        self.delovanje: bool = delovanje
