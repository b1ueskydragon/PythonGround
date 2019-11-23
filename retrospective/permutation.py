def permutation(xs):
  res = []
  for i, x in enumerate(xs):
    _xs = xs[:i] + xs[i + 1:]
    for _x in _xs: # TODO
      res.append(x + _x)
    
  return res
  
xs = ['a', 'b', 'c', 'd']
print(permutation(xs))
