import random
import klassen

# code voor het aanmaken van een deck
def deck_aanmaken():
    symbolen = ['schoppen','ruiten','harten','klaveren']
    waarden = ['A','2','3','4','5','6','7','8','9','10','B','V','H']
    deck=[]
    for i in range(len(symbolen)):
        for j in range(len(waarden)):
            deck.append(klassen.kaart(symbolen[i],waarden[j]))
    deck.append(klassen.kaart('J','J'))
    deck.append(klassen.kaart('J','J'))
    return deck

# code voor het uitdelen van de kaarten aan begin van het spel
def delen(deck,instelling_aantal_kaarten):
    speler_hand = klassen.hand([])
    i=0
    while i!=instelling_aantal_kaarten:
        a=random.choice(deck)
        speler_hand.append(a)
        deck.remove(a)
        i=i+1
    return speler_hand

def speelvolgorde(instelling_aantal_spelers):
    B=[]
    A=[]
    A.append('speler')
    for i in range(1,instelling_aantal_spelers):
        a=''.join(['CPU',str(i)])
        A.append(a)
    for i in range(instelling_aantal_spelers):
        b=random.choice(A)
        B.append(b)
        A.remove(b)
    return B

def handen_aanmaken(volgorde,deck,instelling_aantal_kaarten):
  handen = {}
  for i in volgorde:
    handen.update({str(i):delen(deck,instelling_aantal_kaarten)})
  return handen

def instellingen():
    instelling_aantal_spelers = int(input('Met hoeveel spelers wil je spelen? '))
    instelling_aantal_kaarten = int(input('Met hoeveel kaarten wil je beginnen? '))
    instelling_speelinstelling = input('Wil je met standaardinstellingen spelen? ')
    if instelling_speelinstelling == 'ja':
        instelling_twee = 'ja'
        instelling_zeven = 'ja'
        instelling_acht = 'ja'
        instelling_tien = 'ja'
        instelling_boer = 'ja'
        instelling_heer = 'ja'
        instelling_joker = 'ja'
        instelling_aas = 'ja'
    else:
        print('Selecteer ja/nee voor het gebruik van een pestkaart')
        instelling_twee = input('Bij twee: twee pakken ')
        instelling_zeven = input('Bij zeven: nog een keer spelen ')
        instelling_acht = input('Bij acht: volgende speler overslaan ')
        instelling_tien = input('Bij tien: opnieuw delen ')
        instelling_boer = input('Bij boer: symbool kiezen ')
        instelling_heer = input('Bij heer: nog een keer spelen ')
        instelling_joker = input('Bij joker: vijf kaarten pakken ')
        instelling_aas = input('Bij aas: volgorde omdraaien ')
    return [instelling_aantal_spelers,instelling_aantal_kaarten,instelling_twee,instelling_zeven,instelling_acht,instelling_tien,instelling_boer,instelling_heer,instelling_joker,instelling_aas]

instel = instellingen()
instelling_aantal_spelers=instel[0]
instelling_aantal_kaarten=instel[1]
instelling_twee = instel[2]
instelling_zeven = instel[3]
instelling_acht = instel[4]
instelling_tien = instel[5]
instelling_boer = instel[6]
instelling_heer = instel[7]
instelling_joker = instel[8]
instelling_aas = instel[9]

