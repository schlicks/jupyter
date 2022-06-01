def show(string):
  """split, eval, print a string of semi-colon separated python expressions"""
  from inspect import stack
  namespace = stack()[1][0].f_globals # get global namespace from caller 
  namespace = dict((k,v) for (k,v) in namespace.items() if k[0] != '_')
  for exp in string.split(';'):
    exp = exp.strip(); head, tail = exp[:1], exp[-1:]
    head, exp = (head, exp[1:]) if head == '*' else ('', exp) 
    tail, exp = (tail, exp[:-1]) if tail == '#' else ('', exp)
    val = eval(exp, namespace) if exp else ''
    if exp: print(head+exp if head else exp, '=', end=('\n' if tail else ' '))
    print(*val) if head else print(val)