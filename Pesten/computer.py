import random
import klassen
import spelspelen

def CPU_input(speler_hand,pot):
  if pot[-1].symbool == 'J':
    potentieel = speler_hand
  else:
    potentieel = klassen.hand()
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
    L = [klassen.hand() for i in range(14)]
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
