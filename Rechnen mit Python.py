# Rechnen mit python

## Truthy

name = "" #Leerer Name

print(name or "no name provided") ## Truthy wenn Name leer ist wird hier FALSE



### IF
user_input= ""
def get_input():
     user_input = input("How much do you want?")
     return int(user_input)
def check_int(number_to_add):

    try:

        int(number_to_add)
        return int(number_to_add)
    except ValueError:

        print("this is not a number please try again:")
        number_to_add=get_input()

number_to_add = get_input()
number_to_add= check_int(number_to_add)
print(type(number_to_add))

number = 10 + number_to_add

if number > 11:
    message = str(number) + " > 11"
else:
    message = "HAAAA"

print(message)

## if-ausdruck

ifNumber = get_input()
message_ifAusdruck = "10 or more" if ifNumber > 10 else "smaller"
print(message_ifAusdruck)

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



