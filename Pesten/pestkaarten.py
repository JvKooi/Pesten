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

#functie voor het tellen van kaarten op symbool
def kaart_teller(speler_hand):
  L=[klassen.hand(), klassen.hand(), klassen.hand(), klassen.hand(), klassen.hand(), klassen.hand()]
  i = len(speler_hand)-1
  #check alle kaarten in hand, sorteer op symbool
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
      # kijk of er 2'en aanwezig zijn.
      if speler_hand[i].waarde == '2':
        L[5].append(speler_hand[i])
  #return telling van sortering
  return ([len(L[0]),len(L[1]), len(L[2]), len(L[3]), len(L[4]), len(L[5])])

#functie voor het uitvoeren van de pestkaart twee
def kaart_twee(gespeeld,deck,handen,volgorde,beurt):
  #check instelling
  if instelling_twee == 'ja':
    #tel 2'en in hand volgende speler
    A = kaart_teller(handen[volgorde[(beurt+1)%len(volgorde)]])
    print(volgorde[beurt], 'heeft een twee gespeeld!')
    time.sleep(3)
    if A[-1] == 0:
      #Als geen 2'en in hand, pak twee kaarten
      print(volgorde[(beurt+1)%len(volgorde)], 'moet twee kaarten pakken')
      time.sleep(3)
      spelspelen.kaart_pakken(handen[volgorde[(beurt+1)%len(volgorde)]],deck)
      spelspelen.kaart_pakken(handen[volgorde[(beurt+1)%len(volgorde)]],deck)
      beurt = beurt + 1
    else:
      #Als wel 2'en in hand
      speler_verschil = 1
      aantal_twee = A[-1]
      while aantal_twee != 0:
        #Check handen volgende spelers totdat er een speler is zonder 2'en.
        aantal_twee = kaart_teller(handen[volgorde[(beurt+speler_verschil)%len(volgorde)]])[-1]
        if aantal_twee != 0:
          print(volgorde[(beurt+speler_verschil)%len(volgorde)], 'heeft ook een twee!')
          time.sleep(3)
          index = len(handen[volgorde[(beurt+speler_verschil)%len(volgorde)]])-1
          #kijk waar twee in hand zit
          while handen[volgorde[(beurt+speler_verschil)%len(volgorde)]][index].waarde != '2':
            index = index-1
          gespeeld.append(handen[volgorde[(beurt+speler_verschil)%len(volgorde)]].pop(index))
        speler_verschil = speler_verschil+1
      #stel vast het aantal te pakken kaarten  
      aantal = len(gespeeld)*2            
      print(volgorde[(beurt+speler_verschil-1)%len(volgorde)], 'moet',aantal,'kaarten pakken')
      time.sleep(3)
      k = 0
      #pak alle kaarten
      while k != aantal:
        spelspelen.kaart_pakken(handen[volgorde[(beurt+speler_verschil-1)%len(volgorde)]],deck)
        k = k+1 
      beurt = beurt + speler_verschil - 1
  return ([gespeeld,deck,handen,beurt])  

#functie voor de pestkaart zeven    
def kaart_zeven(beurt):
  #checkt instelling
  if instelling_zeven == 'ja':
    #beurt 1 plaats terug (wordt later met 1 verhoogt)
    beurt = beurt - 1
  return beurt

#functie voor de pestkaart acht
def kaart_acht(beurt):
  #checkt instelling
  if instelling_acht == 'ja':
    #voegt 1 toe bij de beurt zodat de volgende speler wordt overgeslagen
    beurt = beurt + 1
  return beurt

#functie voor de pestkaart tien  
def kaart_tien(handen,volgorde,beurt):
  #checkt instelling
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

#functie voor de pestkaart boer   
def kaart_boer(gespeeld,volgorde,beurt,handen):
  #checkt instelling
  if instelling_boer == 'ja':
    #als de speler aan de beurt is: vraag om het nieuwe symbool
    if volgorde[beurt] == 'speler':       
        print('Welk symbool wilt u spelen?')
        symbool_input = input('Uw keuze is: ')
        #zolang input niet voldoet aan 1 cvan de symbolen, vraag opnieuw
        while symbool_input != 'schoppen' and symbool_input != 'harten' and symbool_input != 'klaveren' and symbool_input != 'ruiten':
          print('U kunt kiezen uit: schoppen, klaveren, ruiten of harten')
          symbool_input = input('Uw keuze is: ')
        #voeg vervolgens de gekozen boer toe aan de pot
        gespeeld.append(klassen.kaart(str(symbool_input),'B'))
    else:
        #tegenstander checkt van welk symbool hij de meeste heeft
        aantal_symbolen = kaart_teller(handen[volgorde[beurt]])
        #verwijdert de telling van de joker en 2'en
        aantal_symbolen.remove(aantal_symbolen[-1])
        aantal_symbolen.remove(aantal_symbolen[-1])
        #selecteer het symbool waarvan de meeste zijn
        max_symbool = max(aantal_symbolen)
        i = 0
        #zoekt door gebruik van de index weer naar de naam van het symbool waarvan de meeste zijn.
        while aantal_symbolen[i] != max_symbool:
            i = i + 1
        symbolen = ['schoppen','ruiten','harten','klaveren']
        print(volgorde[beurt], 'heeft de pot veranderd in', symbolen[i],'!')
        time.sleep(3)
        #voegt vervolgens de gekozen boer toe aan de pot voor de goede weergave van de zet
        gespeeld.append(klassen.kaart(symbolen[i],'B'))
  #geeft gespeeld terug met daarin de boer
  return gespeeld

#functie voor de pestkaart heer
def kaart_heer(beurt):
  #checkt instelling
  if instelling_heer == 'ja':
    #beurt 1 plaats terug (wordt later met 1 verhoogd)
    beurt = beurt - 1
  return beurt

#functie voor de pestkaart aas
def kaart_aas(beurt,volgorde):
  #checkt instelling
  if instelling_aas == 'ja':
    #maak nieuwe volgorde aan en bepaal index
    nieuwevolgorde=[]
    i = beurt
    #Ga alle spelers in volgorde langs en voeg zij toe aan nieuwe volgorde door steeds de persoon voor beurt te kiezen.
    while i >= 0:
      nieuwevolgorde.append(volgorde[i])
      i = i - 1
    for i in range(1,len(volgorde)-beurt):
      nieuwevolgorde.append(volgorde[-i])
    #stel beurt weer in om bij het begin van volgorde te beginnen
    beurt = 0
    print(nieuwevolgorde[beurt],'heeft de volgorde omgedraaid!')
    time.sleep(3)
    #return de beurt en de nieuwe volgorde
    return ([beurt,nieuwevolgorde])
  #als instelling nee, return meteen beurt en volgorde
  else:
    return ([beurt,volgorde])

#functie voor de pestkaart joker
def kaart_joker(handen,deck,volgorde,beurt):
  #check instelling 
  if instelling_joker == 'ja':
    # voer de functie kaartpakken 5 keer uit voor de volgende speler
    for i in range(5):
      spelspelen.kaart_pakken(handen[volgorde[(beurt+1)%len(volgorde)]],deck)
  # return alle handen en het deck
  return ([handen,deck])
