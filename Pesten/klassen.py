suits={'schoppen':'♠','ruiten':'\033[1;31m♦\033[1;m','harten':'\033[1;31m♥\033[1;m','klaveren':'♣','J':' '}

class kaart:
    def __init__(self,symbool,waarde):
        self.symbool = symbool
        self.waarde = waarde

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
    A = []
    B = []
    for i in range(len(speler_hand)//8+1):
      A.append(hand())
      B.append((i+1)*8)
    j = 0
    n = 0
    while n != len(A):
      while j != B[n] and j < len(speler_hand):
        A[n].append(speler_hand[j])
        j = j + 1
      n = n + 1
    for k in range(len(A)):
      print(A[k])
