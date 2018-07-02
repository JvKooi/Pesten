suits={'schoppen':'♠','ruiten':'\033[1;31m♦\033[1;m','harten':'\033[1;31m♥\033[1;m','klaveren':'♣','J':' '}

# defineer klasse kaart
class kaart:
    def __init__(self,symbool,waarde):
        self.symbool = symbool
        self.waarde = waarde

class hand(list):

  # bron: https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards 
  def __repr__(self, index = 0):
    # maak een lege lijst van lijsten
    lines = [[] for i in range(9)]
    # Ga alle kaarten langs
    while index < len(self):
        if self[index].symbool in suits:
            # ga na wat het symbool en de waarde van de kaart is
            if self[index].waarde == 10 or self[index].waarde == '10':
                rank = self[index].waarde
                space = ''
            else:
                rank = self[index].waarde
                space = ' '
            # selecteer juiste symbool uit suits    
            symbool_repr = suits[self[index].symbool]

            # Vul symbool en waarde in bij kaart, en voeg elke regel toe aan lines
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
            # voegt elke regel van een gedekte kaart toe in lines, voor het printen van de tegenstander
            lines[0].append('┌─────────┐')
            lines[1].append('│░░░░░░░░░│')
            lines[2].append('│░░░░░░░░░│')
            lines[3].append('│░░░░░░░░░│')
            lines[4].append('│░░░░░░░░░│')
            lines[5].append('│░░░░░░░░░│')
            lines[6].append('│░░░░░░░░░│')
            lines[7].append('│░░░░░░░░░│')
            lines[8].append('└─────────┘')
        # pak nu de volgende kaart
        index = index + 1
    #voeg alle lijnen met dezelfde index samen tot 1 regel    
    result = [''.join(line) for line in lines]
    #voeg alle lijnen samen uit result met \n zodat de hand in 1 keer wordt geprint 
    return '\n'.join([''.join(line) for line in lines])

def print_tegenstander(tegenstander_hand):
  #check of hand meer dan 8 kaarten heeft  
  if len(tegenstander_hand) <= 8:
    computer_hand=hand([kaart('verborgen','verborgen')]*len(tegenstander_hand))
    print(computer_hand)
  else:
  # Als meer dan 8 kaarten, print dan 1 kaart met getal rechtsonder.  
    computer_hand=[hand([kaart('verborgen','verborgen')]), 'x', str(len(tegenstander_hand))]
    print(*computer_hand, sep=' ')

def print_speler(speler_hand):
  #check of de hand meer dan 8 kaarten heeft  
  if len(speler_hand)<=8:
    print(speler_hand)
  else:
    subhanden = []
    intervallen = []
    #maak genoeg subhanden aan voor alle kaarten in speler hand
    for i in range(len(speler_hand)//8+1): 
      subhanden.append(hand())
      # bepaal intervallen voor alle subhanden
      intervallen.append((i+1)*8)
    index_speler_hand = 0
    index_subhand = 0
    #voor alle subhanden 
    while index_subhand != len(subhanden):
      # zolang subhand nog niet vol en er nog kaarten in te delen zijn. Voeg kaart toe aan subhand  
      while index_speler_hand != intervallen[index_subhand] and index_speler_hand < len(speler_hand):
        subhanden[index_subhand].append(speler_hand[index_speler_hand])
        index_speler_hand = index_speler_hand + 1
      index_subhand = index_subhand + 1
    #print subhanden
    for k in range(len(subhanden)):
      print(subhanden[k])
