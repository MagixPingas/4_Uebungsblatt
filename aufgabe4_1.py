'''Schreiben Sie ein Python-Programm, welches das Heron-Verfahren zur näherungsweisen
Berechnung der Quadratwurzel √a einer positiven Zahl a implementiert.
Zur Erinnnerung: Das Heron-Verfahren startet mit einem Näherungswert x0 für die Qua-
dratwurzel √a, z.B. x0 = 1
2 (1 + a), und berechnet dann für n = 1, 2, 3, . . . iterativ die
Folge der Näherungswerte xn = 1
2 (xn−1 + a/xn−1). Das Verfahren soll enden, sobald der
Absolutbetrag der Dierenz zweier aufeinander folgenden Näherungswerte kleiner als eine
vorgegebene Fehlerschranke ε ist, d.h. sobald |xn − xn−1| < ε gilt.
Am Anfang des Programmes sollen die positive Zahl a und die positive Fehlerschranke ε
interaktiv am Bildschirm eingegeben werden und, nachdem gemäÿ dem Heron-Verfahren
ein Näherungswert für √a berechnet wurde, soll dieser am Bildschirm ausgegeben werden.'''




def heron(a, limit):
    temp = 1
    prev = 0
    while abs(temp-prev) > limit:
        prev = temp
        temp = 0.5*(prev + a/prev)

    return temp


def execute():
    a = eval(input("Zahl unter der Quadratwurzel: "))
    limit = eval(input("Fehlerschranke: "))
    result = heron(a, limit)
    print(f"Die Quadratwurzel von {a} beträgt: {result}\n")



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