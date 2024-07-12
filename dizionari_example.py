# import json
import sys

studente = {
    "nome": "Luca Bianchi",
    "eta'": 17,
    "classe": "4B",
    "materie_preferite": ["matematica", "informatica", "fisica"]
}


def stampa(chiave):
    print(studente[chiave])

def main(argv):
    for chiavi in argv:
        stampa(chiavi)

# for chiave, valore in studente.items():
#    print(chiave, ": ", valore)

# json_string = json.dumps(studente)
# print(json_string)

if __name__ == "__main__":
    main(sys.argv)