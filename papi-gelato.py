import time

prijsBakje = 0.75
prijsHoorntje = 1.25
prijsBolletjes = 1.10
aantalLiter =0
def stap3(hoorntjeOfBakje, AantalBolletjes):
    print('hier is uw ' + hoorntjeOfBakje + ' met ' + str(AantalBolletjes) + ' Bolletjes')
def snapIkNiet():
    print('sorry, dat snap ik niet')
def smaken(AantalBolletjes, aantalLiter):
    e = True
    A = 1
    i = 0
    while e == True:
        i +=1
        smaak = input('welke smaak wilt u voor bolletje ' + str(A) + ', wil je? A) Aardbei, C) Chocola, V) Vanille of M) Munt? ').upper()
        A +=1
        if i == AantalBolletjes:
            e = False
        if smaak != 'A' and smaak != 'C' and smaak != 'V' and smaak != 'M':
            i -= 1
            A -= 1
            snapIkNiet()
def toppings(PrijsToppings, hoorntjeOfBakje, AantalBolletjes):
    n = True
    while n == True:
        topping = input('wat voor topping wil je: A) Geen, B) Slagroom, C) Sprinkels of D) karamelsaus ').upper()
        if topping == 'A':
            print('je hebt voor geen topping gekozen.')
            n = False
        elif topping == 'B':
            PrijsToppings += 0.50 
            n = False
        elif topping == 'C':
            PrijsToppings += (0.30*AantalBolletjes)
            n = False
        elif topping == 'D':
            if hoorntjeOfBakje == 'bakje':
                PrijsToppings += 0.90
            elif hoorntjeOfBakje == 'hoorntje':
                PrijsToppings += 0.60
            n = False
        elif topping != 'A' or topping != 'B' or topping != 'C' or topping != 'D':
            snapIkNiet()
            n = True
    return PrijsToppings
def bonnetje(PrijsToppings, totaalAantalBolletjes, totaalAantalHoorntjes, totaalAantalBakjes):
    b = totaalAantalBolletjes*prijsBolletjes
    h = totaalAantalHoorntjes*prijsHoorntje
    B = totaalAantalBakjes*prijsBakje

    print() 
    print('[----------{Papi Gelato}----------]')
    print()
    print(' bolletjes:   ' + str(totaalAantalBolletjes) + ' x ' + str(prijsBolletjes) + '       = €' + str(round(b, 3)))
    if totaalAantalHoorntjes > 0:
        print(' hoorntjes:   ' + str(totaalAantalHoorntjes) + ' x ' + str(prijsHoorntje) + '      = €' + str(round(h, 3)))
    if totaalAantalBakjes > 0:
        print(' bakjes:      ' + str(totaalAantalBakjes) + ' x ' + str(prijsBakje) + '      = €' + str(round(B, 3)))
    print(' toppings:                  = €' + str(round(PrijsToppings, 3)))
    print('                            ------- +')
    print(' totaal:                    = €' + str(round(b+B+h+PrijsToppings, 3)))
    print()
    print('[---------------------------------]')
    print('bedankt voor jouw aankoop bij Papi Gelato!')
def bolletjesBestellen():
    x = True
    totaalAantalHoorntjes = 0
    totaalAantalBakjes = 0
    totaalAantalBolletjes = 0  
    prijsToppings = 0
    while x == True:
        AantalBolletjes = int(input('hoeveel bolletjes wil je? '))
        totaalAantalBolletjes += AantalBolletjes
        if AantalBolletjes <= 0:
            snapIkNiet()
        elif AantalBolletjes <= 3:
            smaken(AantalBolletjes)
            y = True
            while y == True:
                time.sleep(1)
                hoorntjeOfBakje = str(input('wil je een bakje?(1) of een hoorntje?(2) '))
                if hoorntjeOfBakje == '1':
                    y = False
                    totaalAantalBakjes += 1
                    hoorntjeOfBakje = 'bakje'
                    time.sleep(1)
                    prijsToppings += toppings(prijsToppings, hoorntjeOfBakje, AantalBolletjes)
                    stap3(hoorntjeOfBakje, AantalBolletjes)
                elif hoorntjeOfBakje == '2':
                    y = False
                    totaalAantalHoorntjes +=1
                    hoorntjeOfBakje = 'hoorntje'
                    time.sleep(1)
                    prijsToppings += toppings(prijsToppings, hoorntjeOfBakje, AantalBolletjes)
                    stap3(hoorntjeOfBakje, AantalBolletjes)
        elif AantalBolletjes <=8:
            smaken(AantalBolletjes)
            time.sleep(1)
            print('oke, je krijgt van mij een bakje met ' + str(AantalBolletjes) + ' bolletjes.')
            hoorntjeOfBakje = 'bakje'
            totaalAantalBakjes += 1
            time.sleep(1)
            prijsToppings += toppings(prijsToppings, hoorntjeOfBakje, AantalBolletjes)
            stap3()
        else:snapIkNiet()
        o = True
        while o == True:
            opnieuwBestellen = input('wil je opnieuw bestellen?(J/N)').upper()
            if opnieuwBestellen == 'J':
                x = True
                o = False
            elif opnieuwBestellen == 'N':
                x = False
                o = False
                bonnetje(prijsToppings, totaalAantalBolletjes, totaalAantalHoorntjes, totaalAantalBakjes)
            else:snapIkNiet()
def literBestellen():
    aantalLiter = int(input('hoeveel liter ijs wilt u bestellen? '))
    if aantalLiter >= 0:
        smaken()
    return


print()
print('Welkom bij Papi Gelato!')
z = True
while z == True:
    particulierOfZakelijk = input('Bent u 1) particulier of 2) zakelijk?')
    if particulierOfZakelijk == '1':
        z = False
        bolletjesBestellen()
    elif particulierOfZakelijk == '2':
        z = False
        literBestellen()
    elif particulierOfZakelijk != '1' or particulierOfZakelijk != '2':
        snapIkNiet()
	