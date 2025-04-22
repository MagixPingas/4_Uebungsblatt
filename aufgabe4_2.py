'''Die sog. Collatz-Funktion C sei für alle natürlichen Zahlen n deniert durch C(n) = n/2
falls n gerade ist bzw. C(n) = 3n + 1 falls n ungerade ist. Für jede natürliche Zahl n0
als Startwert kann man dann die zu diesem Startwert gehörige rekursiv denierte sog.
Collatz-Folge n0, n1, n2, n3, n4, . . . mit nk = C(nk−1) für alle k = 1, 2, 3, 4, . . . betrachten.
Von Lothar Collatz stammt die sog. Collatz-Vermutung: Bei jeder natürlichen Zahl n0
als Startwert kommt in der zugehörigen Collatz-Folge vermutlich immer die Zahl 1 vor.
Z.B. für n0 = 43 erhält man die zugehörige Collatz-Folge 43, 130, 65, 196, 98, 49, 148, 74,
37, 112, 56, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2, 1, . . .
a) Schreiben Sie ein Programm, bei dem man interaktiv am Bildschirm einen Startwert
n0 eingeben kann und welches dann solange die zugehörige Collatz-Folge ausgibt,
bis diese zum ersten Mal die Zahl 1 erreicht und dann abbricht.
b) Ergänzen Sei ihr in a) geschriebenes Programm so, dass bei der Collatz-Folge die
Anzahl der Schritte bis zum Erreichen der Zahl 1 mitgezählt und ausgegeben wird.
c) Ergänzen Sei ihr in b) geschriebenes Programm auch noch so, dass auch noch der
Maximalwert in der Collatz-Folge ermittelt und ausgegeben wird.
d) Ergänzen Sie ihr in c) geschriebenes Programm noch um eine interaktive Abfrage,
ob das Programm wiederholt werden soll, und implementieren Sie die Wiederholung
mittels einer while-Schleife.'''


def collatz(number, counter = 1, max_val = 0):

    if number > max_val:
        max_val = number

    if 1 == number:
        return counter, max_val
    else:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1

        print(number)
        return collatz(number, counter + 1, max_val)



def execute():
    a = eval(input("Startwert: "))
    steps, max_val = collatz(a)

    print(f"Anzahl der Schritte: {steps}")
    print(f"Maximalwert der Folge: {max_val}")




execute()


while True:
    answer = input("Programm nochmal ausführen? (Y/n): ")

    if answer in ('Y', 'y', ''):
        execute()
    elif answer in ('N', 'n'):
        print("Tschüss!")
        break
    else:
        print("Ungültige Eingabe!.")