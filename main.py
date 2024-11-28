data_structure = [ [1, 2, 3],  {'a': 4, 'b': 5},  (6, {'cube': 7, 'drum': 8}),  "Hello",
 ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(*args):
 resylt = 0
 a = args[0]
 if isinstance(a, int):
  return resylt + a
 for i in a:
  if i == ():
   continue
  elif isinstance(i, dict):
   resylt +=  sum(i.values())
   b = list(i.keys())
   resylt += len(b[0]) + len(b[1])
   continue
  elif isinstance(i, int):
   resylt += i
  elif isinstance(i, str) and (i.lower()).islower():
   resylt += len(i)
  elif len(i) > 1:
   for j in i:
    if j == ():
     continue
    if isinstance(j, dict):
     resylt += sum(j.values())
     b = list(j.keys())
     resylt += len(b[0]) + len(b[1])
     continue
    if isinstance(j, int):
     resylt += j
    elif isinstance(j, str) and (j.lower()).islower():
     resylt += len(j)
    elif len(j) > 1:
     for k in j:
      if k == ():
       continue
      if isinstance(k, dict):
       resylt += (len(k.keys()) + sum(k.values()))
       continue
      if isinstance(k, int):
       resylt += k
       return resylt
      elif isinstance(k, str) and (k.lower()).islower():
       resylt += len(k)
       continue
 return resylt + calculate_structure_sum(i)

print(calculate_structure_sum(data_structure))

