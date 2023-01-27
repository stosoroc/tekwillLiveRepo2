class Comanda:

    def __init__(self, produse):
        self.produse = produse
        self._pret_override = None

    @property
    def pret(self):
        if self._pret_override:
            return self._pret_override
        return sum(produs.pret for produs in self.produse)

    @pret.setter
    def pret(self, value):
        self._pret_override = value


print(Comanda([]).pret)
comanda = Comanda([])
comanda.pret = 100
print(comanda.pret)
