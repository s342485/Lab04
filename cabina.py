class Cabina:
    def __init__(self, codcabina, numero_letti, numero_ponte, prezzo_base):
        self._codcabina = codcabina
        self._numero_letti = int(numero_letti)
        self._numero_ponte = numero_ponte
        self._prezzo_base = float(prezzo_base)
        self._passeggeri = []

    def aggiungi_passeggero(self, passeggero):
        if len(self._passeggeri) < self._numero_letti:
            self._passeggeri.append(passeggero)
            #“Il passeggero X ora è assegnato a questa cabina.
            passeggero._cabina = self
        else:
            print("Cabina piena!")

    @property
    def _disponibilità(self):
        return self._disponibilità

    @_disponibilità.setter
    def _disponibilità (self, value):
        self._disponibilità = value

    def sovrapprezzo(self, prezzo_base):
        pass

    def __str__(self):
        return f"Cabina {self._codcabina} | Letti: {self._numero_letti} | Ponte: {self._numero_ponte} | Prezzo: {self._prezzo_base:.2f}€"

