from cabina import Cabina

class CabinaAnimali(Cabina):
    def __init__(self, codcabina, numero_letti, numero_ponte, prezzo_base, num_animali):
        super().__init__(codcabina, numero_letti,numero_ponte, prezzo_base)
        self._num_animali = float(num_animali)
        self.sovrapprezzo()

    def sovrapprezzo(self):
        prezzo_finale = self._prezzo_base *(1 + (0.10 * self._num_animali))
        self._prezzo_base = prezzo_finale

    def __str__(self):
        return f"Cabina {self._codcabina} | Letti: {self._numero_letti} | Ponte: {self._numero_ponte} | Max Animali: {int(self._num_animali)} | Prezzo: {self._prezzo_base:.2f}€"
