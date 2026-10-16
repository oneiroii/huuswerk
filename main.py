from datetime import datetime
import random

#-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --#

###### opdracht 1 les 1

#variables
ticket = 7.50
gok_tax = 2.50
werknemer_diensten = 3.50
vaste_kosten = ticket + gok_tax + werknemer_diensten
minimum_budget = ""
MIN_AGE = 18
CURRENT_YEAR = datetime.now().year

#intro inputs
voornaam = input("Vul voornaam in: ").capitalize()
achternaam = input("Vul achternaam in: ").capitalize()
geboortedatum = input("Geboorte datum (dd-mm-yyyy): ")

birth_day, birth_month, birth_year = geboortedatum.split("-")
age = CURRENT_YEAR - int(birth_year)
if age < MIN_AGE:
    exit(1)

geslacht = input("Geslacht: M (man), V (vrouw) of A (ander)").capitalize()
groet = ""

#gender groet
if geslacht == "M" or geslacht == "m":
     groet = "Meneer " + achternaam
elif geslacht == "V" or geslacht == "v":
    groet = "Mevrouw " + achternaam
else:
    groet = voornaam
#budget
budget = float(input("Wat is uw startbudget (in euro)?"))
saldo = budget - vaste_kosten

if saldo > 0:
    minimum_budget = "Je hebt nog genoeg budget voor toegang tot het casino :)"
else:
    minimum_budget = "Je hebt niet genoeg budget voor toegang tot het casino :("
    exit(2)

#print all out
print("Casino de Gouden Driehoek")
print("-------------------------")
print(f"Welkom {groet} \n")
print(f"Startbudget: {budget:.2f} \nVaste kosten: {vaste_kosten:.2f} \nSaldo: {saldo:.2f} ")
print(f"\n {minimum_budget}")

#-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --#

####### Opdracht 2 les 2

#variables
round_number = 1
spin = random.randrange(0, 37)

def even_oneven():
    if spin % 2 == 0:
        # even is 3, oneven is 4, komt uit choice menu
        odd_even = 3
        return odd_even
    else:
        odd_even = 4
        return odd_even

        # kleur bepalen
def get_color():
    #1 is rood, 2 is zwart, komt uit choice menu
    if spin <= 18 and even_oneven() == 3:
        color = 2
        return color
    elif spin <= 18 and even_oneven() == 4:
        color = 1
        return color
    elif spin >= 18 and even_oneven() == 3:
        color = 1
        return color
    else:
        color = 2
        return color

#kleuren
kleur_naam = {1: "Rood", 2: "Zwart"}


print("Welkom bij roulette:")

while True:
    choice = int(input("Kies één van de volgende opties: \n 1. Rood \n 2. Zwart \n 3. Even \n 4. Oneven \n 0. Stop"))
    if choice not in [1, 2, 3, 4, 0]:
        print("Keuze niet mogelijk")
        continue
    elif choice == 0:
        exit(0)
    inzet = float(input("Hoeveel zet je in?"))
    if inzet <= 0 or saldo < inzet:
        print("Inzet niet mogelijk")
        continue
    #pas budget aan na inzet
    saldo -= inzet

    #spin
    even_oneven()
    get_color()
    kleur = get_color()

    #waar valt de bal op:
    print(f"De bal valt op {kleur_naam[kleur]}({spin})")
    # heeft speler gewonnen
    if choice == get_color() or choice == even_oneven():
        winst = inzet * 2
        print (f"Je wint € {winst}")
        saldo += winst
        print (f"Nieuwe saldo: € {saldo}")
    elif choice != get_color() or choice != even_oneven():
        print("Helaas incorrect.")
        print(f"Nieuwe saldo: € {saldo}")

