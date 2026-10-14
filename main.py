# This is a sample Python script.
#variables
ticket = 7.50
gok_tax = 2.50
werknemer_diensten = 3.50
vaste_kosten = ticket + gok_tax + werknemer_diensten
minimum_budget = ""

#intro inputs
voornaam = input("Vul voornaam in: ").capitalize()
achternaam = input("Vul achternaam in: ").capitalize()
geboortedatum = input("Geboorte datum (dd-mm-yyyy): ")

birth_day, birth_month, birth_year = geboortedatum.split("-")
age = CURRENT_YEAR - birth_year
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

print ("test")
