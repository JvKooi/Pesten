#!/usr/bin/python3
import sys
import random
suits={'schoppen':'♠','ruiten':'♦','harten':'♥','klaver':'♣','J':' '}

class kaart:
    def __init__(self,symbool,waarde):
        self.symbool = symbool
        self.waarde = waarde

  # bron: https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards 
    def __repr__(self,return_string=True):
        if self.symbool in suits:
            lines = [[] for i in range(9)]
            if self.waarde == '10':
                rank = self.waarde
                space = ''
            else:
                rank = self.waarde
                space = ' '

            a = suits[self.symbool]

            lines[0].append('┌─────────┐')
            lines[1].append('│{}{}       │'.format(rank, space))
            lines[2].append('│         │')
            lines[3].append('│         │')
            lines[4].append('│    {}    │'.format(a))
            lines[5].append('│         │')
            lines[6].append('│         │')
            lines[7].append('│       {}{}│'.format(space, rank))
            lines[8].append('└─────────┘')

            result = []
            for index, line in enumerate(lines):
                result.append(''.join(lines[index]))

            if return_string:
                return '\n'.join(result)
            else:
                return result
    
        else:
            lines = [[] for i in range(9)]

            lines[0].append('┌─────────┐')
            lines[1].append('│░░░░░░░░░│')
            lines[2].append('│░░░░░░░░░│')
            lines[3].append('│░░░░░░░░░│')
            lines[4].append('│░░░░░░░░░│')
            lines[5].append('│░░░░░░░░░│')
            lines[6].append('│░░░░░░░░░│')
            lines[7].append('│░░░░░░░░░│')
            lines[8].append('└─────────┘')

            result = []
            for index, line in enumerate(lines):
                result.append(''.join(lines[index]))
      
            if return_string:
                return '\n'.join(result)
            else:
                return result

class hand(list):

  # bron: https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards 
  def __repr__(self, index = 0):
    lines = [[] for i in range(9)]
    while index < len(self):
        if self[index].symbool in suits:
            if self[index].waarde == 10 or self[index].waarde == '10':
                rank = self[index].waarde
                space = ''
            else:
                rank = self[index].waarde
                space = ' '
            symbool_repr = suits[self[index].symbool]

            lines[0].append('┌─────────┐')
            lines[1].append('│{}{}       │'.format(rank, space))
            lines[2].append('│         │')
            lines[3].append('│         │')
            lines[4].append('│    {}    │'.format(symbool_repr))
            lines[5].append('│         │')
            lines[6].append('│         │')
            lines[7].append('│       {}{}│'.format(space, rank))
            lines[8].append('└─────────┘')

        else:
            lines[0].append('┌─────────┐')
            lines[1].append('│░░░░░░░░░│')
            lines[2].append('│░░░░░░░░░│')
            lines[3].append('│░░░░░░░░░│')
            lines[4].append('│░░░░░░░░░│')
            lines[5].append('│░░░░░░░░░│')
            lines[6].append('│░░░░░░░░░│')
            lines[7].append('│░░░░░░░░░│')
            lines[8].append('└─────────┘')
        index = index + 1
    result = [''.join(line) for line in lines]
    return '\n'.join([''.join(line) for line in lines])

# code voor het aanmaken van een deck
def deck_aanmaken():
    symbolen = ['schoppen','ruiten','harten','klaver']
    waarden = ['A','2','3','4','5','6','7','8','9','10','B','V','H']
    deck=[]
    for i in range(len(symbolen)):
        for j in range(len(waarden)):
            deck.append(kaart(symbolen[i],waarden[j]))
    if instelling_joker == 'ja':
        deck.append(kaart('J','J'))
        deck.append(kaart('J','J'))
    return deck

# code voor het uitdelen van de kaarten aan begin van het spel
def delen(deck,instelling_aantal_kaarten):
    speler_hand = hand([])
    i=0
    while i!=instelling_aantal_kaarten:
        a=random.choice(deck)
        speler_hand.append(a)
        deck.remove(a)
        i=i+1
    return speler_hand

def spel_spelen(speler_hand,tegenstander_hand,pot,deck,speler_input,volgorde,beurt):
  while len(speler_hand) != 0 or len(tegenstander_hand) != 0:
    ronde_spelen(speler_hand,tegenstander_hand,pot,deck,speler_input,volgorde,beurt)
  if len(speler_hand) == 0:
    print('Gefeliciteerd, je hebt gewonnen!')
  elif len(tegenstander_hand) == 0:
    print('Helaas, je hebt verloren!')

def ronde_spelen(speler_hand,tegenstander_hand,pot,deck,speler_input,volgorde,beurt):
  print_tegenstander(tegenstander_hand)
  print(pot)
  print(speler_hand)
  A=speler_input(speler_hand)
  speler_kaart =  speler_hand[A[1]-1]
  if A[0] == 'pakken':
    kaart_pakken(speler_hand,deck)
  elif A[0] == 'spelen':
    if not controleer_kaart(pot,speler_kaart):
      ronde_spelen(speler_hand,tegenstander_hand,pot,deck,speler_input,volgorde,beurt)
    elif controleer_kaart(pot,speler_kaart):
      gespeeld=[]
      gespeeld.append(speler_kaart)
      print(gespeeld)
      speler_hand.remove(speler_hand[A[1]-1])
      print(speler_hand)
      gespeelde_kaart(speler_kaart,gespeeld,speler_hand,tegenstander_hand,volgorde,beurt,pot,deck)
    beurt = beurt + 1

def print_tegenstander(tegenstander_hand):
  a=len(tegenstander_hand)
  if a<=8:
    computer_hand=hand([kaart('verborgen','verborgen')]*a)
    print(computer_hand)
  else:
    computer_hand=(hand([kaart('verborgen','verborgen')]), 'x', str(a))
    print(computer_hand)

def speler_input(speler_hand):
  print('Speel een kaart of pak een kaart:')
  kaart_input = input('Ik wil een kaart ')
  if kaart_input == 'pakken':
    kaart_keuze = 0
  if kaart_input == 'spelen':
    print('Welke kaart wilt u spelen?')
    kaart_keuze = int(input('Uw keuze is kaartnummer: '))
  return ([kaart_input,kaart_keuze])

def gespeelde_kaart(speler_kaart,gespeeld,speler_hand,tegenstander_hand,volgorde,beurt,pot,deck):
  if speler_kaart.waarde == '2':
    kaart_twee(pot,gespeeld,deck,speler_hand,gespeeld,tegenstander_hand)
  elif speler_kaart.waarde == '7':
    kaart_zeven(pot,gespeeld,deck,beurt)
  elif speler_kaart.waarde == '8':
    kaart_acht(pot,gespeeld,deck,beurt)
  elif speler_kaart.waarde == '10':
    kaart_tien(pot,gespeeld,deck,speler_hand,tegenstander_hand)
  elif speler_kaart.waarde == 'B':
    kaart_boer(pot,gespeeld,deck)
  elif speler_kaart.waarde == 'H':
    kaart_heer(pot,gespeeld,deck,beurt)
  elif speler_kaart.waarde == 'A':
    kaart_aas(pot,gespeeld,deck,volgorde)
  elif speler_kaart.waarde == 'J':
    kaart_joker(pot,gespeeld,deck,speler_hand,tegenstander_hand)
  stapels_bijwerken

def stapels_bijwerken(pot,gespeeld,deck):
    deck.append(pot[0])
    pot.clear()
    pot.append(gespeeld[-1])
    gespeeld.remove(gespeeld[-1])
    deck = deck + gespeeld
    gespeeld.clear()

#####################################
#code voor twee pakken nog niet helemaal af: misschien combineren met joker?
def kan_ik_opleggen(x):
  print('kun je een',str(x),'opleggen? ')
  result = input()
  return result == 'ja'

def kaart_twee(pot,gespeeld,deck,speler_hand,tegenstander_hand):
  if instelling_twee == 'ja':
    return
#####################################

def kaart_zeven(pot,gespeeld,deck,beurt):
  if instelling_zeven == 'ja':
    beurt = beurt - 1

def kaart_acht(pot,gespeeld,deck,beurt):
  if instelling_acht == 'ja':
    beurt = beurt + 1
  
def kaart_tien(pot,gespeeld,deck,speler_hand,tegenstander_hand):
  if instelling_tien == 'ja':
    a=len(speler_hand)
    for i in range(len(tegenstander_hand)):
      speler_hand.append(tegenstander_hand[i])
    tegenstander_hand.clear()
    for i in range(a):
      tegenstander_hand.append(speler_hand[i])
    for i in range(a):
      speler_hand.remove(speler_hand[0])
   
def kaart_boer(pot,gespeeld,deck):
  if instelling_boer == 'ja':
    print('Welk symbool wilt u spelen?')
    symbool_input = input('Uw keuze is: ')
    gespeeld.append(kaart('symbool_input','B'))

def kaart_heer(pot,gespeeld,deck,beurt):
  if instelling_heer == 'ja':
    beurt = beurt - 1

def kaart_aas(pot,gespeeld,deck,volgorde):
  if instelling_aas == 'ja':  
    nieuwevolgorde=[]
    while len(volgorde) !=0:
        nieuwevolgorde.append(volgorde.pop(-1))
    volgorde = nieuwevolgorde

def kaart_joker(deck,speler_hand):
  if instelling_joker == 'ja':
    for i in range(5):
      kaart_pakken(deck,speler_hand)

# kaart pakken uit het deck
def kaart_pakken(speler_hand,deck):
  speler_hand.append(deck.pop(random.choice(range(len(deck)))))

#code voor kaart acht
#def kaart_acht(volgorde,beurt):
    #if volgorde[-2]==beurt:
        #beurt=volgorde[0]
    #elif volgorde[-1]==beurt:
        #beurt=volgorde[1]
    #else:
        #for i in range(len(volgorde)):
            #if volgorde[i]==beurt:
                #beurt=volgorde[i+2]
                #return beurt
    
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

# moet restricties geven aan de invoer van de instellingen (nog niet in werking)
def instelling_input():
    instelling = input()
    if instelling == 'ja':
        return
    elif instelling == 'nee':
        return
    else:
        print('kies uit: ja/nee')
        
#moet controleren of de opgelegde kaart correct is
def controleer_kaart(pot,speler_kaart):
  if pot[-1].symbool =='J':
    return
  elif speler_kaart.symbool == 'J':
    return
  elif speler_kaart.waarde == pot[0].waarde or speler_kaart.symbool == pot[0].symbool:
    return
  else:
    print ('Foute kaart, probeer opnieuw')
    return False 

# code om een spel te spelen en dit weer te geven
def instellingen():
    instelling_aantal_spelers = int(input('Met hoeveel spelers wil je spelen? '))
    instelling_aantal_kaarten = int(input('met hoeveel kaarten wil je beginnen? '))
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

volgorde=speelvolgorde(instelling_aantal_spelers)
beurt=0
deck = deck_aanmaken()
speler_hand = delen(deck,instelling_aantal_kaarten)
tegenstander_hand = delen(deck,instelling_aantal_kaarten)
pot = hand([])
pot.append(random.choice(deck))

spel_spelen(speler_hand,tegenstander_hand,pot,deck,speler_input,volgorde,beurt)


