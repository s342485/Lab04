from cabina import Cabina

class CabinaDeluxe(Cabina):
    def __init__(self, codcabina, numero_letti, numero_ponte, prezzo_base, tipo_stanza):
        super().__init__(codcabina, numero_letti, numero_ponte, prezzo_base)
        self._tipo_stanza = tipo_stanza
        self.sovrapprezzo() #aggiorna subito il prezzo

    def sovrapprezzo(self):
        prezzo_finale = float(self._prezzo_base) * 1.20
        self._prezzo_base = prezzo_finale
    def __str__(self):
        return f"Cabina {self._codcabina} | Letti: {self._numero_letti} | Ponte: {self._numero_ponte} | Deluxe: {self._tipo_stanza} | Prezzo: {self._prezzo_base:.2f}€"


