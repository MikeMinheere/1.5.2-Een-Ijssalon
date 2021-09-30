import time
print()
print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.”')
def stap3():
    print('hier is uw ' + hoorntjeOfBakje + ' met ' + str(AantalBolletjes) + ' Bolletjes')
def snapIkNiet():
    print('sorry, dat snap ik niet')
i = True
x = True
while x == True:
    AantalBolletjes = int(input('hoeveel bolletjes wil je? '))
    if AantalBolletjes <= 3:
        while i == True:
            hoorntjeOfBakje = str(input('wil je een bakje?(1) of een hoorntje?(2) '))
            if hoorntjeOfBakje == '1':
                i = False
                hoorntjeOfBakje = 'bakje'
                stap3()
            elif hoorntjeOfBakje == '2':
                i = False
                hoorntjeOfBakje = 'hoorntje'
                stap3()
            else:snapIkNiet()
    elif AantalBolletjes <=8:
        hoorntjeOfBakje = 'bakje'
        stap3()
    else:snapIkNiet
    opnieuwBestellen = input('wil je opnieuw bestellen?(J/N)').upper()
    if opnieuwBestellen == 'J':
        x = True
    elif opnieuwBestellen == 'N':
        x = False
        print('oke, bedankt voor jouw aankoop bij Papi Gelato!')
    else:snapIkNiet()