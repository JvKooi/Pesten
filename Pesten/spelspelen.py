import random
import time
import klassen
import spelstarten
import computer
import pestkaarten

def handen_leeg(handen,volgorde):
  aantal_kaarten = []
  #bekijk of een speler een lege hand heeft
  for i in volgorde:
    if len(handen[i]) == 0:
      aantal_kaarten.append(0)
    else:
      aantal_kaarten.append(1)
  if 0 in aantal_kaarten:
    return True
  else:
    return False

def spel_spelen(beurt,deck,gespeeld,pot,handen,volgorde):
  #ga net zo lang door totdat een speler een lege hand heeft
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
  klassen.print_speler(handen['speler'])
  #zoek de speler die een lege hand heeft
  if len(handen['speler']) == 0:
    print('Gefeliciteerd, je hebt gewonnen!')
  else:
    for i in volgorde:
      if len(handen[i]) == 0:
        print(i, 'heeft gewonnen!')

def tegenstanders_printen(handen,volgorde):
  for i in volgorde:
    #print de hand van elke speler die niet 'speler' heet
    if i != 'speler':
      print('De hand van', i,':')
      klassen.print_tegenstander(handen[i])

def ronde_spelen(beurt,deck,gespeeld,pot,handen,volgorde):
  tegenstanders_printen(handen,volgorde)
  print(pot)
  klassen.print_speler(handen['speler'])
  #bekijk of de speler of de computer de beurt heeft
  if volgorde[beurt%len(volgorde)] != 'speler':
    print(volgorde[beurt%len(volgorde)], 'is aan de beurt!')
    # vraag de computergestuurde speler wat hij wil doen
    keuze = computer.CPU_input(handen[volgorde[beurt%len(volgorde)]],pot)
    time.sleep(3)
    #laat de menselijke speler weten wat er gebeurt
    if keuze[0] == 'pakken':
      print(volgorde[beurt], 'heeft een kaart gepakt!')
    elif keuze[0] == 'spelen':
      print(volgorde[beurt], 'heeft een kaart gespeeld!')
    time.sleep(3)
  else:
    print('Jij bent aan de beurt!')
    #vraag de speler wat hij wil spelen
    keuze = speler_input(handen[volgorde[beurt]])
  speler_kaart =  handen[volgorde[beurt]][keuze[1]]
  if keuze[0] == 'pakken':
    kaart_pakken(handen[volgorde[beurt]],deck)
    beurt = (beurt + 1) % len(volgorde)
  elif keuze[0] == 'spelen':
    #controleer of de kaart opgelegd kan worden
    while controleer_kaart(pot,speler_kaart) == False:
      ronde_spelen(beurt,deck,gespeeld,pot,handen,volgorde)
    elif controleer_kaart(pot,speler_kaart):
      gespeeld.append(handen[volgorde[beurt]].pop(keuze[1]))
      #roep de functie aan die de gevolgen van de gespeelde kaart nabootst
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
  #controleer of de invoer juist is
  while kaart_input != 'pakken' and kaart_input != 'spelen':
    print('U moet kiezen uit pakken of spelen')
    kaart_input = input('Ik wil een kaart ')
  #geef de juiste actie weer
  if kaart_input == 'pakken':
    kaart_keuze = 0
    return ([kaart_input,kaart_keuze])
  if kaart_input == 'spelen':
    print('Welke kaart wilt u spelen?')
    kaart_keuze = int(input('Uw keuze is kaartnummer: '))
    #controleer of de invoer wel klopt met de hand
    while kaart_keuze > len(speler_hand) or kaart_keuze <= 0:
      print('U heeft',int(len(speler_hand)), 'kaarten')
      kaart_keuze = int(input('Uw keuze is kaartnummer: '))
  return ([kaart_input,kaart_keuze-1])

def gespeelde_kaart(beurt,deck,gespeeld,pot,handen,volgorde,speler_kaart):
  #bekijk welke waarde de gespeelde kaart heeft en roep de juiste functie aan
  if speler_kaart.waarde == '2':
    resultaat = pestkaarten.kaart_twee(gespeeld,deck,handen,volgorde,beurt)
    gespeeld = resultaat[0]
    deck = resultaat[1]
    handen = resultaat[2]
    beurt = resultaat[3]
  elif speler_kaart.waarde == '7':
    beurt = pestkaarten.kaart_zeven(beurt)
  elif speler_kaart.waarde == '8':
    beurt = pestkaarten.kaart_acht(beurt)
  elif speler_kaart.waarde == '10':
    handen = pestkaarten.kaart_tien(handen,volgorde,beurt)
  elif speler_kaart.waarde == 'B':
    gespeeld = pestkaarten.kaart_boer(gespeeld,volgorde,beurt,handen)
  elif speler_kaart.waarde == 'H':
    beurt = pestkaarten.kaart_heer(beurt)
  elif speler_kaart.waarde == 'A':
    resultaat = pestkaarten.kaart_aas(beurt,volgorde)
    beurt = resultaat[0]
    volgorde = resultaat [1]
  elif speler_kaart.waarde == 'J':
    resultaat = pestkaarten.kaart_joker(handen,deck,volgorde,beurt)
    handen = resultaat[0]
    deck = resultaat[1]
  #werk de gevolgen van de gespeelde kaart bij
  stapels_bijwerken(deck,pot,gespeeld)
  return ([beurt,deck,gespeeld,pot,handen,volgorde])

def stapels_bijwerken(deck,pot,gespeeld):
  #bekijk of de pot een boer bevat
  if pot[-1].waarde == 'B':
    pot.clear()
  else:
    deck.append(pot[0])
    pot.clear()
  #werk de stapels bij
  pot.append(gespeeld[-1])
  gespeeld.remove(gespeeld[-1])
  deck = deck + gespeeld
  gespeeld.clear()
  
def kaart_pakken(speler_hand,deck):
  #controleer of er wel een kaart te geven is
  if len(deck) == 0:
    print('Sorry, de kaarten zijn op!')
    print('Het spel stopt!')
    exit()
  else:
    speler_hand.append(deck.pop(random.choice(range(len(deck)))))

def controleer_kaart(pot,speler_kaart):
  #controleer of de pot een joker is
  if pot[-1].symbool =='J':
    return True
  #controleer of de gespeelde kaart een joker is
  elif speler_kaart.symbool == 'J':
    return True
  #controleer of symbool of waarde van pot en gespeelde kaart overeenkomen
  elif speler_kaart.waarde == pot[0].waarde or speler_kaart.symbool == pot[0].symbool:
    return True
  else:
    print('\033[1;46m!!!!!!\033[1;m')
    print ('\033[1;36mFoute kaart, probeer opnieuw!\033[1;m')
    print('\033[1;46m!!!!!!\033[1;m')
    return False 
