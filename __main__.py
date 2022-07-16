import os
import time
from unicodedata import name
from reader import feed

cruciverba = [
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
]
crucicorretto = [
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
]
maxline = 8
maxcells = 64

definizioniv = {"1)":   "ciao",
                "2)":   "ciao2",
                }

definizionio = {"4)":   "ciao4",
                "5)":   "ciao5",
                }

tentativi = 0
tic = time.perf_counter()

#----------------------------------------------------------------------#


def view():

    os.system('cls' if os.name == 'nt' else 'clear')

    for i in range(0, maxcells, maxline):
        print("|", end="")
        for j in range(maxline):
            print(cruciverba[i+j], end="")
            print("|", end="")
        print("\n")

    print("\n\n")

    print("VERTICALI")
    for ele in definizioniv:
        print(ele, end="\t")
        print(definizioniv[ele])

    print("\n\n")

    print("ORIZZONTALI")
    for ele in definizionio:
        print(ele, end="\t")
        print(definizionio[ele])

    print("\n\n")

#----------------------------------------------------------------------#


def askO(n):

    c = 0

    for i in range(n, maxcells+1):
        if cruciverba[i] == "*":
            c = i-n
        else:
            c = (((n//maxline)+1)*maxline)-n

    print(f"Lunghezza della parola {c}caratteri")

    p = input("inserisci la parola:\n")

    if len(p) < c:
        print("Parola troppo corta, reinserire")
        askO(n)
    elif len(p) > c:
        print("Parola troppo lunga :/")
        askO(n)
    else:
        for i in range(len(p)):
            cruciverba[n+i] = p[i]

 #----------------------------------------------------------------------#


def askV(n):

    if n % maxline == 0:
        c = -1
    else:
        c = 0
    for i in range(n, maxcells+1, maxline):
        if cruciverba[i] == "*":
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


def main():

    while True:

        view()
        n = -1

        while not 0 <= n <= 63:
            n = int(input("Inserisci la cella:\n"))

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
#----------------------------------------------------------------------#


if __name__ == "__main__":
    
    main()
