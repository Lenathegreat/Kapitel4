# Rechnen mit python

def result(operator):
    print(operator)


operator = 3+4
operator = 3 /4
operator = 0.1 + 0.2    # Fließkommerzahlen: 0.30000000000000004 ungenauigkeit von pyhton

operator = 1_000_000    # in pyhton können zahlen mit unterstrich geschrieben werden und pyhton erkennt es als zahl = besser zur übersicht

operator = int(4.8)     # wird einfach abgerundet auf 4

operator = 7 % 3        # Modulo : Zeigt den rest an also 4
operator = 7 // 3       # Führt die Division durch und schreib das ergbnis ohne rest zurück
operator = 7 ** 3       # Potenz 7 hoch 3

operator = 2 + (3 * ( 4 ** 2)) #innerste Klammer wird zuerst ausgeführt

result(operator)
