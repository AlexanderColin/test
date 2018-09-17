
naam = input ("Voer naam in: ")
adres = input ("Voer stad, land, postcode in: ")
telefoon = input ("Voer telefoonnummer in: ")
studie = input ("Voer je studie in: ")
info = print("Hier zijn je gegevens:", naam, adres,\n, telefoon, studie)

//

verkoop = float (input('Voer totaal verkoop in: '))
print ("Totale winst is", verkoop * 0.23)

//

item1 = float (input ("Prijs product 1? "))
item2 = float (input ("Prijs product 2? "))
item3 = float (input ("Prijs product 3? "))
item4 = float (input ("Prijs product 4? "))
item5 = float (input ("Prijs product 5? "))

subtotal = item1 + item2 + item3 + item4 + item5
salestotal = subtotal * 0.07
total = subtotal + salestotal

print ('subtotal:', subtotal)
print ('salestotal:', salestotal)
print ('total:', total)

//

distance = float (input ("""Voer afstand in km:"""))
print ("In 6uur rijden wordt", distance * 6, "km afgelegd")
print ("In 10uur rijden wordt", distance * 10, "km afgelegd")
print ("In 15uur rijden wordt", distance * 15, "km afgelegd")

//

distance = float (input ("Voer in afstand(km): "))
liter = float (input ("Voer in verbruikte benzine(L): "))
print ("Totaal benzine verbruik per km:", distance / liter)

//

print ("Voor 48 koekjes heb je:\n", \
       "1.5 koppen suiker\n", \
       "1 kop boter en\n", \
       "2.75 koppen bloem nodig\n")
koekjes = int (input ("Hoeveel koekjes wil je maken? "))
suiker  = koekjes * 1.5 / 48
boter   = koekjes * 1 / 48 
bloem   = koekjes * 2.75 / 48
print ("\nVoor", koekjes, "koekjes heb je:")
print (" ", suiker, "koppen suiker,")
print (" ", boter, "koppen boter en")
print (" ", bloem,"koppen bloem nodig")

