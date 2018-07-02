import random
import klassen
import spelspelen

#functie voor de keuze van de CPU, geprogrameerd voor gekozen strategie
#bekijk eerst potentiele kaarten, stel daarna prioriteit
def CPU_input(speler_hand,pot):
  #bepaal eerst een lijst van potentiele kaarten die gespeeld gaan worden
  #check of de pot een joker is, dan zijn alle kaarten potentieel
  if pot[-1].symbool == 'J':
    potentieel = speler_hand
  #als pot geen joker
  else:
    #maak een subhand potentieel aan
    potentieel = klassen.hand()
    #voor alle kaarten in hand
    for i in range(len(speler_hand)):
      #als hand een joker bezit, voeg toe aan potentieel
      if speler_hand[i].symbool == 'J':
        potentieel.append(speler_hand[i])
      #als hand een kaart met dezelfde symbool als pot bezit, voeg toe aan potentieel  
      elif speler_hand[i].symbool == pot[-1].symbool:
        potentieel.append(speler_hand[i])
      #als hand een kaart met dezelfde waarde als pot bezit, voeg toe aan potentieel  
      elif speler_hand[i].waarde == pot[-1].waarde:
        potentieel.append(speler_hand[i])
  #als er geen potentiele kaarten zijn om te spelen, pak dan een kaart
  if len(potentieel) == 0:
    #return hetzelfde als wat de speler zou returnen als de input 'pakken' is
    return ['pakken',0]
  #als er wel een poteniele kaart(en) is/zijn
  else:
    #maak een lijst met 14 handen (1 voor elke waarde plus joker)
    L = [klassen.hand() for i in range(14)]
    for i in range(len(potentieel)):
      #check van elke kaart de waarde, volgens deze prioriteitenlijst
      #L[0] 
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
        return ['spelen',int(i)]
