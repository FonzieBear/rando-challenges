class Orderer:
  def __init__(self, n):
    self.squares = []
    x = 1
    #print(n)
    while x*x <= 2*n:
      self.squares.append(x*x)
      x += 1

    self.possibilities = self.buildLists([], [x for x in range(1, n+1)])
      
  def buildLists(self, curList, candidates):
    if not candidates:
      return [curList]

    ret = []

    for idx, x in enumerate(candidates):
      if not curList or curList[-1] + x in self.squares:
        ret.extend(self.buildLists(curList + [x], candidates[:idx] + candidates[idx+1:]))

    return ret

  def getLists(self):
    return self.possibilities

for n in range(1, 100000):
  o = Orderer(n)
  orders = o.getLists()
  
  if orders:
    print('n = %s; Found %s possible orderings:' % (n, len(orders)))
    for o in orders:
      print('\t', o)
    #print('\t' + orders)