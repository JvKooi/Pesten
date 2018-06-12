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


#speler_hand = hand([kaart('schoppen',1),kaart('harten',2),kaart('J','J')])
#tegenstander_hand = hand([kaart('harten',1),kaart('verborgen',2),kaart('klaver',10)])
#print(speler_hand)
#print(tegenstander_hand)

#code voor het deck en het uitdelen aan het begin van het spel
symbolen=['schoppen','ruiten','harten','klaver']
a=['A','2','3','4','5','6','7','8','9','10','B','V','H']
deck=[]
for i in range(len(symbolen)-1):
  for j in range(len(a)-1):
    deck.append(kaart(symbolen[i],a[j]))
deck.append(kaart('J','J'))
deck.append(kaart('J','J'))

import random

speler_hand=hand([])
def delen(deck,speler_hand):
  i=0
  while i!=7:
    a=random.choice(deck)
    speler_hand.append(a)
    deck.remove(a)
    i=i+1
  return speler_hand

