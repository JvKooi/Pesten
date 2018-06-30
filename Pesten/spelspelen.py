import random
import time
import klassen
import spelstarten
import computer
import pestkaarten

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
      klassen.print_tegenstander(handen[i])

def ronde_spelen(beurt,deck,gespeeld,pot,handen,volgorde):
  tegenstanders_printen(handen,volgorde)
  print(pot)
  klassen.print_speler(handen['speler'])
  if volgorde[beurt%len(volgorde)] != 'speler':
    print(volgorde[beurt%len(volgorde)], 'is aan de beurt!')
    A = computer.CPU_input(handen[volgorde[beurt]],pot)
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

def speler_input(speler_hand):
  print('Speel een kaart of pak een kaart:')
  kaart_input = input('Ik wil een kaart ')
  while kaart_input != 'pakken' and kaart_input != 'spelen':
    print('U moet kiezen uit pakken of spelen')
    kaart_input = input('Ik wil een kaart ')
  if kaart_input == 'pakken':
    kaart_keuze = 0
    return ([kaart_input,kaart_keuze])
  if kaart_input == 'spelen':
    print('Welke kaart wilt u spelen?')
    kaart_keuze = int(input('Uw keuze is kaartnummer: '))
    while kaart_keuze > len(speler_hand) or kaart_keuze <= 0:
      print('U heeft',int(len(speler_hand)), 'kaarten')
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
  
# kaart pakken uit het deck
def kaart_pakken(speler_hand,deck):
  speler_hand.append(deck.pop(random.choice(range(len(deck)))))

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
