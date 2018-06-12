def print_breuk(c):
  m = c.versimpel()
  print(m.a,'/',m.b, sep='')

class breuk:

  def __init__(self, a=0, b=1): 
    self.a = a
    self.b = b

  def __str__(self):
    self.versimpel()
    return str(self.a) + '/' + str(self.b)

  def __add__(self,other):
    if isinstance(other,breuk):
      result = breuk(1)
      result.a = other.b*self.a + self.b * other.a
      result.b = other.b*self.b
    elif isinstance(other,int):
      result = breuk(1)
      result.a = self.a + self.b * other
      result.b = self.b
    return result

  def __radd__(self,other):
    if isinstance(other,int):
      result = breuk(1)
      result.a = self.a + self.b * other
      result.b = self.b
    return result

  def __sub__(self,other):
    if isinstance(other,breuk):
      result = breuk(1)
      result.a = other.b*self.a - self.b * other.a
      result.b = other.b*self.b
    elif isinstance(other,int):
      result = breuk(1)
      result.a = self.a - self.b*other
      result.b = self.b
    return result
  
  def __rsub__(self,other):
    if isinstance(other,int):
      result = breuk(1)
      result.a = self.b*other - self.a
      result.b = self.b
    return result

  def __mul__(self,other):
    if isinstance(other,breuk):
      result = breuk(1)
      result.a = self.a*other.a
      result.b = other.b*self.b
    elif isinstance(other,int):
      result = breuk(1)
      result.a = self.a*other
      result.b = self.b
    return result
  
  def __rmul__(self,other):
    if isinstance(other,int):
      result = breuk(1)
      result.a = self.a*other
      result.b = self.b
    return result
  
  def __truediv__(self,other):
    if isinstance(other,breuk):
      result = breuk(1)
      result.a = self.a*other.b
      result.b = other.a*self.b
    elif isinstance(other,int):
      result = breuk(1)
      result.a = self.a
      result.b = self.b*other
    return result

  def __rtruediv__(self,other):
    if isinstance(other,int):
      result = breuk(1)
      result.a = self.b*other
      result.b = self.a
    return result

  def __float__(self):
    return float(self.a/self.b)

  def __int__(self):
    return int(self.a/self.b)
    
  def __eq__(self, other):
    return self.a * other.b == self.b * other.a

  def __ne__(self,other):
    return self.a * other.b != self.b * other.a

  def __lt__(self,other):
    return self.a * other.b < self.b * other.a

  def __le__(self,other):
    return self.a * other.b <= self.b * other.a

  def __gt__(self,other):
    return self.a * other.b > self.b * other.a

  def __ge__(self,other):
    return self.a * other.b >= self.b * other.a

  def __pos__(self):
    return self

  def __neg__(self):
    return self*(-1)

  def __abs__(self):
    if self.a >= 0 and self.b > 0:
      return self
    elif self.a < 0 and self.b < 0:
      return breuk(-self.a,-self.b)
    elif self.a > 0 and self.b < 0:
      return breuk(self.a,-self.b)
    elif self.a < 0 and self.b > 0:
      return breuk(-self.a,self.b)

  def versimpel(self):
    n = max(self.a,self.b)
    m = min(self.a,self.b)
    t = n
    while m !=0:
      t = m
      m = n % m
      n = t
    self.a = int(self.a/t)
    self.b = int(self.b/t)
    return self 
 
class vector(list):

  def __add__(self,other):
    result = vector([0]*len(self))
    for i in range(len(self)):
      result[i]=self[i]+other[i]
    return result
  
  def __sub__(self,other):
    result = vector([0]*len(self))
    for i in range(len(self)):
      result[i]=self[i]-other[i]
    return result

  def __mul__(self,other):
    if isinstance(other, int):
      result = vector([0]*len(self))
      for i in range(len(self)):
        result[i]=other*self[i]
      return result
    if isinstance(other, vector):
      a = [0]*len(self)
      for i in range(len(self)):
        a[i]=self[i]*other[i]
      result = sum(a)
      return result
    
  def __rmul__(self,other):
    if isinstance(other, int):
      result = vector([0]*len(self))
      for i in range(len(self)):
        result[i]=other*self[i]
      return result

class polynoom(list):
  
  def __init__(self,items):
    self.waarde = items
    self.waarde += ([0]*(100-len(self.waarde)))

  def __call__(self,x):
    result = list()
    for i in range(0,100):
      result.append(self.waarde[i]*(x**i))
    result = sum(result)
    return result

  def __repr__(self):
    return repr(self.waarde)

  def __add__(self,other):
    result = list()
    for i in range(len(self.waarde)):
      result.append(self.waarde[i]+other.waarde[i])
    return polynoom(result)
  
  def __sub__(self,other):
    result = list()
    for i in range(len(self.waarde)):
      result.append(self.waarde[i]-other.waarde[i])
    return polynoom(result)

  def __mul__(self,other):
    result = list()
    if isinstance(other, int):
      for i in range(len(self.waarde)):
        result.append(self.waarde[i]*other)
    return polynoom(result)

  def __rmul__(self,other):
    result = list()
    if isinstance(other, int):
      for i in range(len(self.waarde)):
        result.append(self.waarde[i]*other)
    return polynoom(result)
