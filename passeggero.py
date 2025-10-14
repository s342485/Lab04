class Passeggero:
    def __init__(self, cod, nome, cognome):
        self._cod = cod
        self._nome = nome
        self._cognome = cognome
        self._cabina = None

    def __str__(self):
        return f"{self._cod} {self._nome} {self._cognome}"
    def __repr__(self):
        return f"codice={self._cod}, nome={self._nome}, cognome={self._cognome}"





