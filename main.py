import random

class Domanda:
    def __init__(self, testo, difficolta, corretta, errata):
        self.testo = testo
        self.difficolta = difficolta
        self.corretta = corretta
        self.opzioni = [corretta] + errata

    def visualizzazione_domanda (self):
        random.shuffle(self.opzioni)
        print(f"\nLivello {self.difficolta}) {self.testo}")
        for i in range(len(self.opzioni)):
            print(f" {i+1}. {self.opzioni[i]}")

    def controlla(self, scelta):
        # trasformiamo la risposta in indice
        indice = int(scelta)-1
        risposta_data = self.opzioni[indice]
        return risposta_data == self.corretta

def carica(nome_file):
    lista_oggetti_domanda = []
    file = open(nome_file, "r", encoding="utf-8")
    righe = file.readlines()
    file.close()
    #range(inizio, fine, salto)
    for i in range (0, len(righe), 7):
        testo= righe[i].strip()
        difficolta = int(righe[i+1].strip())
        corretta = righe[i+2].strip()
        errata = [righe[i+3].strip(), righe[i+4].strip(), righe[i+5].strip()]

        nuova_d = Domanda(testo, difficolta, corretta, errata)
        lista_oggetti_domanda.append(nuova_d)
    return lista_oggetti_domanda

tutte_domande = carica("domande")
punteggio = 0
livello_attuale = 0
gioco_attivo = True

while gioco_attivo == True:
    domande_filtrate = []
    for d in tutte_domande:
        if d.difficolta == livello_attuale:
            domande_filtrate.append(d)

    if not domande_filtrate:
        print("Hai VINTOO!!")
        break

    domanda_scelta = random.choice(domande_filtrate)
    domanda_scelta.visualizzazione_domanda()

    utente = input("Inserisci il numero della risposta: ")

    if domanda_scelta.controlla(utente):
        print("Esatto!\n")
        punteggio+=1
        livello_attuale+=1
    else:
        print(f"Sbagliato! Era: {domanda_scelta.corretta}")
        gioco_attivo = False
        print(f"Partita finita! Punteggio: {punteggio}")

nome = input("Inserisci il tuo Nickname: ")

classifica = []
try:
    f = open("4", "r")
    for riga in f:
        parti = riga.strip().split() # Divide "Paolo 4" in ["Paolo", "4"]
        if len(parti) >= 2:
            nickname_vecchio = parti[0]
            punti_vecchi = int(parti[1]) # Trasformiamo in numero!
            classifica.append((nickname_vecchio, punti_vecchi))
    f.close()
except FileNotFoundError:
    pass # Se il file non esiste ancora, non fa nulla

classifica.append((nome, punteggio))

def prendi_punteggio(elemento):
    return elemento[1]

classifica.sort(key=prendi_punteggio, reverse=True)

f = open("punti.txt", "w")
for giocatore in classifica:
    # giocatore[0] è il nome, giocatore[1] è il punteggio
    f.write(f"{giocatore[0]} {giocatore[1]}\n")
f.close()

print("Classifica salvata con successo!")













