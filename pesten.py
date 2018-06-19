#!/usr/bin/python3
import sys
import copy

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
  for i in range(len(symbolen)-1):
    for j in range(len(waarden)-1):
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

# code om 1 ronde te spelen, hierbij hebben de speler en de tegenstander beide 1 zet.
def ronde_spelen(speler_hand,tegenstander_hand,computer_hand,pot,volgorde,beurt):
  if len(speler_hand) > 0 and len(tegenstander_hand)>0:
    speler_input(speler_hand,tegenstander_hand,computer_hand,pot,volgorde,beurt)
    computer_hand = hand([kaart('verborgen',1)]*len(tegenstander_hand))
    ronde_spelen(speler_hand,tegenstander_hand,computer_hand,pot,volgorde,beurt)
  else:
    print('afgelopen')

# kaart pakken uit het deck
def kaart_pakken(deck,speler_hand):
  speler_hand.append(deck.pop(random.choice(range(len(deck)))))
  return speler_hand

#code voor kaart aas
def kaart_aas(volgorde):
  nieuwevolgorde=[]
  while len(volgorde) !=0:
    nieuwevolgorde.append(volgorde.pop(-1))
  return nieuwevolgorde

#code voor kaart acht
def kaart_acht(volgorde,beurt):
  if volgorde[-2]==beurt:
    beurt=volgorde[0]
  elif volgorde[-1]==beurt:
    beurt=volgorde[1]
  else:
    for i in range(len(volgorde)):
      if volgorde[i]==beurt:
        beurt=volgorde[i+2]
        return beurt

# code voor pest kaart 2
def kaart_twee(deck,hand_kaarten):
  if instelling_twee == 'ja':
    kaart_pakken(deck,hand_kaarten)
    kaart_pakken(deck,hand_kaarten)
  return hand_kaarten

# de joker kaart laat de persoon in kwestie (speler_hand) 5 kaarten pakken
def kaart_joker(deck,speler_hand):
  if instelling_joker == 'ja':
    for i in range(5):
      kaart_pakken(deck,speler_hand)
  return speler_hand

# elke kaart met waarde 10 laat de kaarten van de tegenstander voor 1 ronde zien
def kaart_tien(speler_hand,tegenstander_hand):
  a=len(speler_hand)
  for i in range(len(tegenstander_hand)):
    speler_hand.append(tegenstander_hand[i])
  tegenstander_hand.clear()
  for i in range(a):
    tegenstander_hand.append(speler_hand[i])
  for i in range(a):
    speler_hand.remove(speler_hand[0])
  return (speler_hand,tegenstander_hand)

# moet restricties geven aan de invoer van de instellingen (nog niet in werking)
def instelling_input():
  instelling = input()
  if instelling == 'ja':
    return
  elif instelling == 'nee':
    return
  else:
    print('kies uit: ja/nee')

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

# code om de speler's opties na te gaan. Hierbij werken sommige kaarten al wel(2,10,J)
# en de rest doet het nog niet.
def speler_input(speler_deck,tegenstander_hand,computer_hand,pot,volgorde,beurt):
  if len(computer_hand) <= 8:
    print(computer_hand)
  else:
    print(kaart('verborgen','J'), 'x', len(computer_hand))
  print(pot[-1])
  print(speler_hand)
  print('optie 1: kaart spelen \noptie 2: kaart pakken')
  kaart_input = input('Uw keuze is optie: ')
  if kaart_input == '2':
    kaart_pakken(deck,speler_deck)
  elif kaart_input == '1':
    print('Welke kaart wilt u spelen?')
    kaart_keuze = int(input('Uw keuze is kaartnummer: '))
    if speler_deck[kaart_keuze-1].waarde == '2':
      pot.append(speler_deck.pop(kaart_keuze-1))
      if instelling_twee == 'ja':
        tegenstander_hand = kaart_twee(deck,tegenstander_hand)
    elif speler_deck[kaart_keuze-1].waarde == 'B':
      pot.append(speler_deck.pop(kaart_keuze-1))
    elif speler_deck[kaart_keuze-1].waarde == '7':
      pot.append(speler_deck.pop(kaart_keuze-1))
      if instelling_zeven == 'ja':
        speler_input(speler_deck,tegenstander_hand,computer_hand,pot)
    elif speler_deck[kaart_keuze-1].waarde == '8':
      pot.append(speler_deck.pop(kaart_keuze-1))
      kaart_acht(volgorde,beurt)
      speler_input(speler_deck,tegenstander_hand,computer_hand,pot,volgorde,beurt)
    elif speler_deck[kaart_keuze-1].waarde == '10':
      pot.append(speler_deck.pop(kaart_keuze-1))
      if instelling_tien == 'ja':
        kaart_tien(speler_hand,tegenstander_hand)
    elif speler_deck[kaart_keuze-1].waarde == 'J':
      pot.append(speler_deck.pop(kaart_keuze-1))
      if instelling_joker == 'ja':
        kaart_joker(deck,tegenstander_hand)
    elif speler_deck[kaart_keuze-1].waarde == 'A':
      pot.append(speler_deck.pop(kaart_keuze-1))
      if instelling_aas == 'ja':
        volgorde=kaart_aas(volgorde)
    elif int(kaart_input) > len(speler_deck):
      return
    else:
      pot.append(speler_deck.pop(kaart_keuze-1))
  return 

# code voor de instellingen van het spel
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
beurt='speler'
deck = deck_aanmaken()
speler_hand = delen(deck,instelling_aantal_kaarten)
tegenstander_hand = delen(deck,instelling_aantal_kaarten)
handen=[speler_hand,tegenstander_hand]
computer_hand = hand([kaart('verborgen',1)]*len(tegenstander_hand))
pot = hand([])
pot.append(random.choice(deck))

ronde_spelen(speler_hand,tegenstander_hand,computer_hand,pot,volgorde,beurt)
