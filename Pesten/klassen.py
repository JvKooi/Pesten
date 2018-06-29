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
    intervallen = [hand(),hand(),hand(),hand(),hand()]
    if len(speler_hand) > 8 and len(speler_hand) <= 16:
      for i in range(8):
        intervallen[0].append(speler_hand[i])
      for i in range(8,len(speler_hand)):
        intervallen[1].append(speler_hand[i])
    elif len(speler_hand) > 16 and len(speler_hand) <= 24:
      for i in range(8):
        intervallen[0].append(speler_hand[i])
      for i in range(8,16):
        intervallen[1].append(speler_hand[i])
      for i in range(16,len(speler_hand)):
        intervallen[2].append(speler_hand[i])
    elif len(speler_hand) > 24 and len(speler_hand) <= 32:
      for i in range(8):
        intervallen[0].append(speler_hand[i])
      for i in range(8,16):
        intervallen[1].append(speler_hand[i])
      for i in range(16,24):
        intervallen[2].append(speler_hand[i])
      for i in range(24,len(speler_hand)):
        intervallen[3].append(speler_hand[i])
    elif len(speler_hand) > 32 and len(speler_hand) <= 40:
      for i in range(8):
        intervallen[0].append(speler_hand[i])
      for i in range(8,16):
        intervallen[1].append(speler_hand[i])
      for i in range(16,24):
        intervallen[2].append(speler_hand[i])
      for i in range(24,32):
        intervallen[3].append(speler_hand[i])
      for i in range(32,len(speler_hand)):
        intervallen[4].append(speler_hand[i])
    print(intervallen[0])
    print(intervallen[1])
    if len(intervallen[2])>0:
      print(intervallen[2])  
    if len(intervallen[3])>0:
      print(intervallen[3]) 
    if len(intervallen[4])>0:
      print(intervallen[4])
