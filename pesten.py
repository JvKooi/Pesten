suits={'schoppen':'♠','ruiten':'♦','harten':'♥','klaver':'♣','J':' '}

class kaart:
  def __init__(self,symbool,waarde):
    self.symbool = symbool
    self.waarde = waarde

  def __str__(self,return_string=True):
    lines = [[] for i in range(9)]
    if self.waarde == '10':
      rank = self.waarde
      space = ''
    else:
      rank = self.waarde
      space = ' '

    a=suits[self.symbool]

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
