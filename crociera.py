import operator
from cabina import Cabina
from cabinaDeluxe import CabinaDeluxe
from cabina_animali import CabinaAnimali
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        self._nome = nome
        self._cabine = []
        self._passeggeri = []
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome

    def carica_file_dati(self, file_path):
        try:
            infile = open(file_path, "r", encoding="utf-8")
        except FileNotFoundError:
            print("Il path inserito non è valido, riprovare")

        for line in infile:
            line = line.strip().split(",")
            if len(line) < 5:
                line.append("")

            if line[0].startswith("C"):
                codcabina = line[0]
                numero_letti = line[1]
                numero_ponte = line[2]
                prezzo_base = line[3]

                if line[4] == "":
                    c = Cabina(codcabina, numero_letti, numero_ponte, prezzo_base)
                if line[4].isdigit():
                    num_animali = line[4]
                    c = CabinaAnimali(codcabina, numero_letti, numero_ponte, prezzo_base, num_animali)
                if line[4] == "Moderna" or line[4] == "Classica" or line[4] == "Lussuosa":
                    tipo_stanza = line[4]
                    c = CabinaDeluxe(codcabina, numero_letti, numero_ponte, prezzo_base, tipo_stanza)

                self._cabine.append(c)

            elif line[0].startswith("P"):
                cod = line[0]
                nome = line[1]
                cognome = line[2]
                p = Passeggero(cod, nome, cognome)

                self._passeggeri.append(p)
            else:
                raise ValueError(f'Formato non trovato: {line}')

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        cabina = None
        passeggero = None

        #cerca la cabina
        for c in self._cabine:
            if c._codcabina == codice_cabina:
                cabina = c
                break
        # cerca il passeggero
        for p in self._passeggeri:
            if p._cod == codice_passeggero:
                passeggero = p
                break
        if cabina is None:
            raise Exception("Cabina non trovata.")
        if passeggero is None:
            raise Exception("Passeggero non trovato.")

        if passeggero._cabina is not None:
            raise Exception(
                f"Il passeggero {passeggero._nome} {passeggero._cognome} è già assegnato alla cabina {passeggero._cabina._codcabina}.")

        # se tutto ok, assegna il passeggero
        cabina.aggiungi_passeggero(passeggero)
        print(f"{passeggero._nome} {passeggero._cognome} assegnato alla cabina {cabina._codcabina}.")

    def cabine_ordinate_per_prezzo(self):
        #lista_ordinata =  sorted(self._cabine, key=lambda c: c.prezzo_base)
        lista_ordinata =  sorted(self._cabine, key=operator.attrgetter("_prezzo_base"))
        return lista_ordinata

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for passeggero in self._passeggeri:
            if passeggero._cabina is not None:
                print(f"{passeggero._nome} associato alla cabina {passeggero._cabina._codcabina}")
            else:
                print(f"{passeggero._nome} non associato")