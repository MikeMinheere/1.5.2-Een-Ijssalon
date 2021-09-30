import time
i = True
x = True
print()
print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')
def stap3():
    print('hier is uw ' + hoorntjeOfBakje + ' met ' + str(AantalBolletjes) + ' Bolletjes')
def snapIkNiet():
    print('sorry, dat snap ik niet')
def smaken():
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
            
while x == True:
    AantalBolletjes = int(input('hoeveel bolletjes wil je? '))
    if AantalBolletjes <= 3:
        smaken()
        while i == True:
            time.sleep(1)
            hoorntjeOfBakje = str(input('wil je een bakje?(1) of een hoorntje?(2) '))
            if hoorntjeOfBakje == '1':
                i = False
                hoorntjeOfBakje = 'bakje'
                time.sleep(1)
                stap3()
            elif hoorntjeOfBakje == '2':
                i = False
                hoorntjeOfBakje = 'hoorntje'
                time.sleep(1)
                stap3()
            else:snapIkNiet()
    elif AantalBolletjes <=8:
        smaken()
        time.sleep(1)
        print('oke, je krijgt van mij een bakje met ' + str(AantalBolletjes) + ' bolletjes.')
        hoorntjeOfBakje = 'bakje'
        time.sleep(1)
        stap3()
    else:snapIkNiet()
    opnieuwBestellen = input('wil je opnieuw bestellen?(J/N)').upper()
    if opnieuwBestellen == 'J':
        x = True
    elif opnieuwBestellen == 'N':
        x = False
        print('Oke, bedankt voor jouw aankoop bij Papi Gelato!')
    else:snapIkNiet()