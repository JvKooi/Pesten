#!/usr/bin/python3
import sys
import random
import time
suits={'schoppen':'♠','ruiten':'\033[1;31m♦\033[1;m','harten':'\033[1;31m♥\033[1;m','klaveren':'♣','J':' '}

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
    symbolen = ['schoppen','ruiten','harten','klaveren']
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

def handen_leeg(handen,volgorde):
  A = []
  for i in volgorde:
    if len(handen[i]) == 0:
      A.append(0)
    else:
      A.append(1)
  if 0 in A:
    return True
  else:
    return False

def spel_spelen(beurt,deck,gespeeld,pot,handen,volgorde):
  while handen_leeg(handen,volgorde) == False:
    resultaat = ronde_spelen(beurt,deck,gespeeld,pot,handen,volgorde)
    beurt = resultaat[0]
    deck = resultaat[1]
    gespeeld = resultaat[2]
    pot = resultaat[3]
    handen = resultaat[4]
    volgorde = resultaat[5]
  tegenstanders_printen(handen,volgorde)
  print(pot)
  print_speler(handen['speler'])
  if len(handen['speler']) == 0:
    print('Gefeliciteerd, je hebt gewonnen!')
  else:
    for i in volgorde:
      if len(handen[i]) == 0:
        print(i, 'heeft gewonnen!')

def tegenstanders_printen(handen,volgorde):
  for i in volgorde:
    if i != 'speler':
      print('De hand van', i,':')
      print_tegenstander(handen[i])

def ronde_spelen(beurt,deck,gespeeld,pot,handen,volgorde):
  tegenstanders_printen(handen,volgorde)
  print(pot)
  print_speler(handen['speler'])
  if volgorde[beurt] != 'speler':
    print(volgorde[beurt], 'is aan de beurt!')
    A = CPU_input(handen[volgorde[beurt]])
    time.sleep(3)
    if A[0] == 'pakken':
      print(volgorde[beurt], 'heeft een kaart gepakt!')
    else:
      print(volgorde[beurt], 'heeft een kaart gespeeld!')
    time.sleep(3)
  else:
    print('Jij bent aan de beurt!')
    A = speler_input(handen[volgorde[beurt]])
  speler_kaart =  handen[volgorde[beurt]][A[1]-1]
  if A[0] == 'pakken':
    kaart_pakken(handen[volgorde[beurt]],deck)
    beurt = (beurt + 1) % len(volgorde)
  elif A[0] == 'spelen':
    if not controleer_kaart(pot,speler_kaart):
      ronde_spelen(beurt,deck,gespeeld,pot,handen,volgorde)
      beurt = beurt + 1
    elif controleer_kaart(pot,speler_kaart):
      gespeeld.append(handen[volgorde[beurt]].pop(A[1]-1))
      resultaat = gespeelde_kaart(beurt,deck,gespeeld,pot,handen,volgorde,speler_kaart)
      volgorde = resultaat[5]
      beurt = (resultaat[0] + 1) % len(volgorde)
      deck = resultaat[1]
      gespeeld = resultaat[2]
      pot = resultaat[3]
      handen = resultaat[4]
  return ([beurt,deck,gespeeld,pot,handen,volgorde])

def CPU_input(speler_hand):
  if pot[-1].symbool == 'J':
    potentieel = speler_hand
  else:
    potentieel = hand()
    for i in range(len(speler_hand)):
      if speler_hand[i].symbool == 'J':
        potentieel.append(speler_hand[i])
      elif speler_hand[i].symbool == pot[-1].symbool:
        potentieel.append(speler_hand[i])
      elif speler_hand[i].waarde == pot[-1].waarde:
        potentieel.append(speler_hand[i])
  if len(potentieel) == 0:
    return ['pakken',0]
  else:
    L = [hand() for i in range(14)]
    for i in range(len(potentieel)):
      if potentieel[i].waarde == 'J':
        L[0].append(potentieel[i])
      elif potentieel[i].waarde == '7':
        L[1].append(potentieel[i])
      elif potentieel[i].waarde == 'H':
        L[2].append(potentieel[i])
      elif potentieel[i].waarde == '2':
        L[3].append(potentieel[i])
      elif potentieel[i].waarde == '8':
        L[4].append(potentieel[i])
      elif potentieel[i].waarde == '10':
        L[5].append(potentieel[i])
      elif potentieel[i].waarde == 'B':
        L[6].append(potentieel[i])
      elif potentieel[i].waarde == 'A':
        L[7].append(potentieel[i])
      elif potentieel[i].waarde == 'V':
        L[8].append(potentieel[i])
      elif potentieel[i].waarde == '9':
        L[9].append(potentieel[i])
      elif potentieel[i].waarde == '6':
        L[10].append(potentieel[i])
      elif potentieel[i].waarde == '5':
        L[11].append(potentieel[i])
      elif potentieel[i].waarde == '4':
        L[12].append(potentieel[i])
      elif potentieel[i].waarde == '3':
        L[13].append(potentieel[i])
    i = 0
    while len(L[i]) == 0:
      i = i + 1
    keuze = random.choice(L[i])
    for i in range(len(speler_hand)):
      if speler_hand[i] == keuze:
        return ['spelen',int(i+1)]

def print_tegenstander(tegenstander_hand):
  if len(tegenstander_hand) <= 8:
    computer_hand=hand([kaart('verborgen','verborgen')]*len(tegenstander_hand))
    print(computer_hand)
  else:
    computer_hand=[hand([kaart('verborgen','verborgen')]), 'x', str(len(tegenstander_hand))]
    print(*computer_hand, sep=' ')

def print_speler(speler_hand):
  if len(speler_hand)<=8:
    print(speler_hand)
  else:
    A = [hand(),hand(),hand(),hand(),hand()]
    if len(speler_hand) > 8 and len(speler_hand) <= 16:
      for i in range(8):
        A[0].append(speler_hand[i])
      for i in range(8,len(speler_hand)):
        A[1].append(speler_hand[i])
    elif len(speler_hand) > 16 and len(speler_hand) <= 24:
      for i in range(8):
        A[0].append(speler_hand[i])
      for i in range(8,16):
        A[1].append(speler_hand[i])
      for i in range(16,len(speler_hand)):
        A[2].append(speler_hand[i])
    elif len(speler_hand) > 24 and len(speler_hand) <= 32:
      for i in range(8):
        A[0].append(speler_hand[i])
      for i in range(8,16):
        A[1].append(speler_hand[i])
      for i in range(16,24):
        A[2].append(speler_hand[i])
      for i in range(24,len(speler_hand)):
        A[3].append(speler_hand[i])
    elif len(speler_hand) > 32 and len(speler_hand) <= 40:
      for i in range(8):
        A[0].append(speler_hand[i])
      for i in range(8,16):
        A[1].append(speler_hand[i])
      for i in range(16,24):
        A[2].append(speler_hand[i])
      for i in range(24,32):
        A[3].append(speler_hand[i])
      for i in range(32,len(speler_hand)):
        A[4].append(speler_hand[i])
    print(A[0])
    print(A[1])
    if len(A[2])>0:
      print(A[2])  
    if len(A[3])>0:
      print(A[3]) 
    if len(A[4])>0:
      print(A[4])

def speler_input(speler_hand):
  print('Speel een kaart of pak een kaart:')
  kaart_input = input('Ik wil een kaart ')
  if kaart_input == 'pakken':
    kaart_keuze = 0
  if kaart_input == 'spelen':
    print('Welke kaart wilt u spelen?')
    kaart_keuze = int(input('Uw keuze is kaartnummer: '))
  return ([kaart_input,kaart_keuze])

def gespeelde_kaart(beurt,deck,gespeeld,pot,handen,volgorde,speler_kaart):
  if speler_kaart.waarde == '2':
    resultaat = kaart_twee(gespeeld,deck,handen,volgorde,beurt)
    gespeeld = resultaat[0]
    deck = resultaat[1]
    handen = resultaat[2]
    beurt = resultaat[3]
  elif speler_kaart.waarde == '7':
    beurt = kaart_zeven(beurt)
  elif speler_kaart.waarde == '8':
    beurt = kaart_acht(beurt)
  elif speler_kaart.waarde == '10':
    handen = kaart_tien(handen,volgorde,beurt)
  elif speler_kaart.waarde == 'B':
    gespeeld = kaart_boer(gespeeld,volgorde,beurt)
  elif speler_kaart.waarde == 'H':
    beurt = kaart_heer(beurt)
  elif speler_kaart.waarde == 'A':
    resultaat = kaart_aas(beurt,volgorde)
    beurt = resultaat[0]
    volgorde = resultaat [1]
  elif speler_kaart.waarde == 'J':
    resultaat = kaart_joker(handen,deck,volgorde,beurt)
    handen = resultaat[0]
    deck = resultaat[1]
  stapels_bijwerken(deck,pot,gespeeld)
  return ([beurt,deck,gespeeld,pot,handen,volgorde])

def stapels_bijwerken(deck,pot,gespeeld):
  deck.append(pot[0])
  pot.clear()
  pot.append(gespeeld[-1])
  gespeeld.remove(gespeeld[-1])
  deck = deck + gespeeld
  gespeeld.clear()
  
def kaart_teller(speler_hand):
  L=[hand(), hand(), hand(), hand(), hand(), hand()]
  i = len(speler_hand)-1
  while i >= 0:
      if speler_hand[i].symbool == 'schoppen':
        L[0].append(speler_hand[i])
        i=i-1
      elif speler_hand[i].symbool == 'ruiten':
        L[1].append(speler_hand[i])
        i=i-1
      elif speler_hand[i].symbool == 'harten':
        L[2].append(speler_hand[i])
        i=i-1
      elif speler_hand[i].symbool == 'klaveren':
        L[3].append(speler_hand[i])
        i=i-1
      elif speler_hand[i].waarde == 'J':
        L[4].append(speler_hand[i])
        i=i-1
      if speler_hand[i].waarde == '2':
        L[5].append(speler_hand[i])
  return ([len(L[0]),len(L[1]), len(L[2]), len(L[3]), len(L[4]), len(L[5])])

def kaart_twee(gespeeld,deck,handen,volgorde,beurt):
  if instelling_twee == 'ja':
    A = kaart_teller(handen[volgorde[(beurt+1)%len(volgorde)]])
    print(volgorde[beurt], 'heeft een twee gespeeld!')
    time.sleep(3)
    if A[-1] == 0:
      print(volgorde[beurt+1], 'moet twee kaarten pakken')
      time.sleep(3)
      kaart_pakken(handen[volgorde[(beurt+1)%len(volgorde)]],deck)
      kaart_pakken(handen[volgorde[(beurt+1)%len(volgorde)]],deck)
      beurt = beurt + 1
    else:
      j = 1
      i = A[-1]
      B = []
      while i != 0:
        B.append(i)
        i = kaart_teller(handen[volgorde[(beurt+j)%len(volgorde)]])[-1]
        if i != 0:
          print(volgorde[(beurt+j)%len(volgorde)], 'heeft ook een twee!')
          time.sleep(3)
          n = len(handen[volgorde[(beurt+j)%len(volgorde)]])-1
          while handen[volgorde[(beurt+j)%len(volgorde)]][n].waarde != '2':
            n = n-1
          gespeeld.append(handen[volgorde[(beurt+j)%len(volgorde)]].pop(n))
        j = j+1
      a = len(B)*2            
      print(volgorde[beurt+j-1], 'moet',a,'kaarten pakken')
      time.sleep(3)
      k = 0
      while k != a:
        kaart_pakken(handen[volgorde[(beurt+j-1)%len(volgorde)]],deck)
        k = k+1 
      beurt = beurt + j - 1
  return ([gespeeld,deck,handen,beurt])  
  
  B = []
  for i in volgorde:
    B.append(kaart_teller(handen[i])[-1])
  if instelling_twee == 'ja':
    if B[(beurt+1)%len(volgorde)] == 0:
      kaart_pakken(handen[volgorde[(beurt+1)%len(volgorde)]],deck)
      kaart_pakken(handen[volgorde[(beurt+1)%len(volgorde)]],deck)
    elif B[(beurt+1)%len(volgorde)] > 0:
      i = len(handen[volgorde[(beurt+1)%len(volgorde)]])-1
      while i > 0:
        if handen[volgorde[(beurt+1)%len(volgorde)]][i].waarde != '2':
          i=i-1
      gespeeld.append(handen[volgorde[(beurt+1)%len(volgorde)]].pop(i))
      for i in range(4):
        kaart_pakken(handen[volgorde[(beurt+2)%len(volgorde)]],deck)
    return ([gespeeld,deck,handen])
    
def kaart_zeven(beurt):
  if instelling_zeven == 'ja':
    beurt = beurt - 1
    return beurt

def kaart_acht(beurt):
  if instelling_acht == 'ja':
    beurt = beurt + 1
    return beurt
  
def kaart_tien(handen,volgorde,beurt):
  if instelling_tien == 'ja':
    a=len(handen[volgorde[beurt]])
    for i in range(len(handen[volgorde[(beurt+1)%len(volgorde)]])):
      handen[volgorde[beurt]].append(handen[volgorde[(beurt+1)%len(volgorde)]][i])
    handen[volgorde[(beurt+1)%len(volgorde)]].clear()
    for i in range(a):
      handen[volgorde[(beurt+1)%len(volgorde)]].append(handen[volgorde[beurt]][i])
    for i in range(a):
      handen[volgorde[beurt]].remove(handen[volgorde[beurt]][0])
    print(volgorde[beurt],'heeft handen gewisseld met',volgorde[(beurt+1)%len(volgorde)],'!')
    time.sleep(3)
    return handen
   
def kaart_boer(gespeeld,volgorde,beurt):
  if instelling_boer == 'ja':
    if volgorde[beurt] == 'speler':       
        print('Welk symbool wilt u spelen?')
        symbool_input = input('Uw keuze is: ')
        gespeeld.append(kaart(str(symbool_input),'B'))
    else:
        aantal_symbolen = kaart_teller(handen[volgorde[beurt]])
        aantal_symbolen.remove(aantal_symbolen[-1])
        aantal_symbolen.remove(aantal_symbolen[-1])
        max_symbool = max(aantal_symbolen)
        i = 0
        while aantal_symbolen[i] != max_symbool:
            i = i + 1
        symbolen = ['schoppen','ruiten','harten','klaveren']
        print(volgorde[beurt], 'heeft de pot veranderd in', symbolen[i],'!')
        time.sleep(3)
        gespeeld.append(kaart(symbolen[i],'B'))
    return gespeeld

def kaart_heer(beurt):
  if instelling_heer == 'ja':
    beurt = beurt - 1
    return beurt

def kaart_aas(beurt,volgorde):
  if instelling_aas == 'ja':  
    nieuwevolgorde=[]
    i = beurt
    while i >= 0:
      nieuwevolgorde.append(volgorde[i])
      i = i - 1
    for i in range(1,len(volgorde)-beurt):
      nieuwevolgorde.append(volgorde[-i])
    beurt = 0
    print(nieuwevolgorde[beurt],'heeft de volgorde omgedraaid!')
    time.sleep(3)
    return ([beurt,nieuwevolgorde])

def kaart_joker(handen,deck,volgorde,beurt):
  if instelling_joker == 'ja':
    for i in range(5):
      kaart_pakken(handen[volgorde[(beurt+1)%len(volgorde)]],deck)
    return ([handen,deck])

# kaart pakken uit het deck
def kaart_pakken(speler_hand,deck):
  speler_hand.append(deck.pop(random.choice(range(len(deck)))))

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
        
#moet controleren of de opgelegde kaart correct is
def controleer_kaart(pot,speler_kaart):
  if pot[-1].symbool =='J':
    return True
  elif speler_kaart.symbool == 'J':
    return True
  elif speler_kaart.waarde == pot[0].waarde or speler_kaart.symbool == pot[0].symbool:
    return True
  else:
    print('\033[1;46m!!!!!!\033[1;m')
    print ('\033[1;36mFoute kaart, probeer opnieuw!\033[1;m')
    print('\033[1;46m!!!!!!\033[1;m')
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
gespeeld = []
deck = deck_aanmaken()
handen=handen_aanmaken(volgorde,deck,instelling_aantal_kaarten)
pot = hand([])
kaart_pakken(pot,deck)
spel_spelen(beurt,deck,gespeeld,pot,handen,volgorde)



