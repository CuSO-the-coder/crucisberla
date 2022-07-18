import os
import time
from unicodedata import name
from reader import feed

cruciverba = [
    " ",    " ",    " ",    " ",    " ",    " ",    " ",    " ",    " ",    " ",    "#",  " ",
    " ",    " ",    " ",    "#",   " ",    " ",    " ",    " ",    "#",   " ",    " ",   " ",
    " ",    "#",   " ",    " ",    "#",   " ",    " ",    " ",    " ",    "#",   " ",   " ",
    " ",    " ",    " ",    " ",    " ",    " ",    "#",   "#",   " ",    " ",    " ",   " ",
    " ",    " ",    " ",    "#",   " ",    "#",   " ",    " ",    " ",    " ",    " ",   " ",
]
crucicorretto = [
    "C",    "R",    "U",   "C",    "I",    "V",    "E",     "R",    "B",    "A",     "#",    "U",
    "A",    "O",    "T",   "#",    "P",   "O",    "C",    "A",    "#",    "H",    "A",    "N",
    "S",    "#",    "I",    "N",    "#",   "M",   "O",   "M",   "A",    "#",     "R",     "I",
    "C",    "A",    "L",   "A",    "T",    "O",    "#",    "#",    "P",    "O",    "C",    "O",
    "O",    "R",    "E",   "#",   "O",    "#",    "P",    "Y",    "T",    "H",    "O",    "N"
]

maxline = 12
maxcells = 60

definizioniV = {
    "0)":   "Si mette in moto (ma non a Napoli)",
    "1)":   "Sigla di Rovigo",
    "2)":   "Qualcosa che serve",
    "4)":   "192.168.1.120",
    "5)":   "Isola delle Fiji",
    "6)":   "Rimbomba nelle grotte",
    "7)":   "Random Access Memory",
    "9)":   "Preposizione inglese",
    "11)":   "Unione in inglese",
    "22)":   "Può essere a tutto sesto",
    "27)":   "Sodio",
    "32)":   "Azienda  Provinciale Trasporti",
    "37)":   "Gas nobile del 3° periodo",
    "40)":   "Sigla di Torino",
    "45)":   "Esclamazione di stupore"
}

definizioniO = {
    "0)":   "Lo stai facendo ora",
    "12)":   "Attack On Titan",
    "16)":   "Il contrario di 'tanta'",
    "21)":   "Sin/Cos",
    "26)":   "Di, A, Da, {...}, Con, Su, Per, Tra, Fra",
    "29)":   "Museum of Modern Art",
    "34)":   "Rio senza 'o'",
    "36)":   "Il contrario di 'elevare'",
    "44)":   "Se non è tanto è {...}",
    "48)":   "Le segna l'orologio",
    "55)":   "Il 'serpentese' per i programmatori"
}

tentativi = 0

tic = time.perf_counter()

#----------------------------------------------------------------------#


def loading():
    for i in range(6):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n")
        print("Caricamento")
        print("° "*(i+1))
        time.sleep(0.5)
    
    time.sleep(1)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\n\n")
    print("  ______                             __          __                         __          \n /      \                           |  \        |  \                       |  \         \n|  ▓▓▓▓▓▓\ ______  __    __  _______ \▓▓ _______| ▓▓____   ______   ______ | ▓▓ ______  \n| ▓▓   \▓▓/      \|  \  |  \/       \  \/       \ ▓▓    \ /      \ /      \| ▓▓|      \ \n| ▓▓     |  ▓▓▓▓▓▓\ ▓▓  | ▓▓  ▓▓▓▓▓▓▓ ▓▓  ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓\  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓ \▓▓▓▓▓▓\ \n| ▓▓   __| ▓▓   \▓▓ ▓▓  | ▓▓ ▓▓     | ▓▓\▓▓    \| ▓▓  | ▓▓ ▓▓    ▓▓ ▓▓   \▓▓ ▓▓/      ▓▓\n| ▓▓__/  \ ▓▓     | ▓▓__/ ▓▓ ▓▓_____| ▓▓_\▓▓▓▓▓▓\ ▓▓__/ ▓▓ ▓▓▓▓▓▓▓▓ ▓▓     | ▓▓  ▓▓▓▓▓▓▓\n \▓▓    ▓▓ ▓▓      \▓▓    ▓▓\▓▓     \ ▓▓       ▓▓ ▓▓    ▓▓\▓▓     \ ▓▓     | ▓▓\▓▓    ▓▓\n  \▓▓▓▓▓▓ \▓▓       \▓▓▓▓▓▓  \▓▓▓▓▓▓▓\▓▓\▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓  \▓▓▓▓▓▓▓\▓▓      \▓▓ \▓▓▓▓▓▓▓", end="\n\n")
    print("-------------------")
    print("╔═══╗    ╔═══╗╔═══╗\n║╔═╗║    ║╔═╗║║╔═╗║\n║║ ╚╝╔╗╔╗║╚══╗║║ ║║\n║║ ╔╗║║║║╚══╗║║║ ║║\n║╚═╝║║╚╝║║╚═╝║║╚═╝║\n╚═══╝╚══╝╚═══╝╚═══╝")
    print("-------------------")
    time.sleep(2.4)

    os.system('cls' if os.name == 'nt' else 'clear')

#----------------------------------------------------------------------#


def askTuto():
    print("\n")
    print("*--------------------------------------------------------------------------------------------------------------------------*")
    print("|                                                                                                                          |")
    print("| Benvenuto su 'Crucisberla', un cruciverba giocabile tramite il terminale di Python, desideri avere un piccolo tutorial?  |")
    print("|                                                                                                                          |")
    print("*--------------------------------------------------------------------------------------------------------------------------*")
    
    y_n = ""

    while not (y_n == "si" or y_n == "no" or y_n == "sì"):
        y_n = input("Risposta [si/no]: \t")
        y_n = y_n.lower()

    if y_n == "sì" or y_n == "si":
        print("Iniziamo il tutorial!")

        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("Ti verrà mostrata una situazione di questo tipo: \n")
        
        for i in range(0, maxcells, maxline):
            print("|", end="")
            for j in range(maxline):
                print(cruciverba[i+j], end="")
                print("|", end="")
            print("\n")
        
        print("Le caselle vuote le dovrai riempire con delle parole in base alla definizione corrispondente, gli # sono caselle annerite, quindi non potrai modificarli.")
        time.sleep(4)
        
        print("Ti verrà chiesto il numero della casella/definizione e il verso in cui inserire la parola (veritcale o orizzontale).")
        time.sleep(2)

        print("E questo è quanto, divertiti!")
        time.sleep(2)
        
        game()

    else:
        print("Va bene, divertiti!")
        time.sleep(3)
        
        game()

#----------------------------------------------------------------------#


def view():

    os.system('cls' if os.name == 'nt' else 'clear')

    for i in range(0, maxcells, maxline):
        print("|", end="")
        for j in range(maxline):
            print(cruciverba[i+j], end="")
            print("|", end="")
        print("\n")

    print("\n")

    print("VERTICALI")
    for ele in definizioniV:
        print(ele, end="\t")
        print(definizioniV[ele])

    print("\n")

    print("ORIZZONTALI")
    for ele in definizioniO:
        print(ele, end="\t")
        print(definizioniO[ele])

    print("\n")

#----------------------------------------------------------------------#


def askO(n):

    c = 0

    for i in range(n, maxcells+1):
        if cruciverba[i] == "#":
            c = i-n
        else:
            c = (((n//maxline)+1)*maxline)-n

    print(f"Lunghezza della parola {c} caratteri")

    p = input("inserisci la parola:\n")

    if len(p) < c:
        print("Parola troppo corta, reinserire")
        askO(n)
    elif len(p) > c:
        print("Parola troppo lunga :/")
        askO(n)
    else:
        p = p.upper()
        for i in range(len(p)):
            cruciverba[n+i] = p[i]

#----------------------------------------------------------------------#


def askV(n):

    if n % maxline == 0:
        c = -1
    else:
        c = 0

    for i in range(n, maxcells+1, maxline):
        if cruciverba[i] == "#":
            break
        else:
            c += 1

    print(f"Lunghezza della parola {c}caratteri")

    p = input("Inserisci la parola:\n")

    if len(p) < c:
        print("Parola troppo corta, reinserire")
        askV(n)
    elif len(p) > c:
        print("Parola troppo lunga :/")
        askV(n)
    else:
        p = p.upper()
        for i in range(len(p)):
            cruciverba[n+i*maxline] = p[i]

#----------------------------------------------------------------------#


def viewfin():

    for i in range(0, maxcells, maxline):
        print("|", end="")
        for j in range(maxline):
            print(cruciverba[i+j], end="")
            print("|", end="")
        print("\n")

#----------------------------------------------------------------------#


def correggi():

    if cruciverba == crucicorretto:
        toc = time.perf_counter()
        print(
            f"Complimenti! \n Hai completato il cruciverba in maniera corretta in {tentativi} tentativi impiegando {tic-toc}  secondi")
        viewfin()
    else:
        print("Mi dispiace, hai commesso degli errori, riprova :( ")
        view()

#----------------------------------------------------------------------#


def game():

    while True:

        view()

        n = -1

        while not (0 <= n <= maxcells-1):
            n = int(input("Inserisci la cella:\n"))
            if cruciverba[n] == "#":
                print("Hey, non puoi cambiare le caselle annerite")
                n = -1

        t = ""
        while not(t == "o" or t == "v" or t == "orizzontale" or t == "verticale"):
            t = input("Verticale o orizzontale:\n")
            t = t.lower()

        if t == "orizzontale" or t == "o":
            askO(n)
        elif t == "verticale" or t == "v":
            askV(n)

        if cruciverba.count(" ") == 0:
            risp = input("Cruciverba completato, correggerlo? (sì/no) \n")
            risp = risp.lower()
            if risp == "sì":
                tentativi += 1
                correggi()

#----------------------------------------------------------------------#


def main():
    loading()
    askTuto()

#----------------------------------------------------------------------#
#----------------------------------------------------------------------#


if __name__ == "__main__":
    main()
