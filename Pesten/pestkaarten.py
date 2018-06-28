import time
import klassen
import spelspelen
import spelstarten
instelling_twee = spelstarten.instelling_twee
instelling_zeven = spelstarten.instelling_zeven
instelling_acht = spelstarten.instelling_acht
instelling_tien = spelstarten.instelling_tien
instelling_boer = spelstarten.instelling_boer
instelling_heer = spelstarten.instelling_heer
instelling_joker = spelstarten.instelling_joker
instelling_aas = spelstarten.instelling_aas

def kaart_teller(speler_hand):
  L=[klassen.hand(), klassen.hand(), klassen.hand(), klassen.hand(), klassen.hand(), klassen.hand()]
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
      elif speler_hand[i].waarde == '2':
        L[5].append(speler_hand[i])
  return ([len(L[0]),len(L[1]), len(L[2]), len(L[3]), len(L[4]), len(L[5])])

def kaart_twee(gespeeld,deck,handen,volgorde,beurt):
  B = []
  for i in volgorde:
    B.append(kaart_teller(handen[i])[-1])
  if instelling_twee == 'ja':
    if B[(beurt+1)%len(volgorde)] == 0:
      spelspelen.kaart_pakken(handen[volgorde[(beurt+1)%len(volgorde)]],deck)
      spelspelen.kaart_pakken(handen[volgorde[(beurt+1)%len(volgorde)]],deck)
    elif B[(beurt+1)%len(volgorde)] > 0:
      i = len(handen[volgorde[(beurt+1)%len(volgorde)]])-1
      while i > 0:
        if handen[volgorde[(beurt+1)%len(volgorde)]][i].waarde != '2':
          i=i-1
      gespeeld.append(handen[volgorde[(beurt+1)%len(volgorde)]].pop(i))
      for i in range(4):
        spelspelen.kaart_pakken(handen[volgorde[(beurt+2)%len(volgorde)]],deck)
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
   
def kaart_boer(gespeeld,volgorde,beurt,handen):
  if instelling_boer == 'ja':
    if volgorde[beurt] == 'speler':       
        print('Welk symbool wilt u spelen?')
        symbool_input = input('Uw keuze is: ')
        while symbool_input != 'schoppen' and symbool_input != 'harten' and symbool_input != 'klaveren' and symbool_input != 'ruiten':
          print('U kunt kiezen uit: schoppen, klaveren, ruiten of harten')
          symbool_input = input('Uw keuze is: ')
        gespeeld.append(klassen.kaart(str(symbool_input),'B'))
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
        gespeeld.append(klassen.kaart(symbolen[i],'B'))
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
      spelspelen.kaart_pakken(handen[volgorde[(beurt+1)%len(volgorde)]],deck)
    return ([handen,deck])
