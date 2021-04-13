import random

noun = ['dog ','Ryan ','Louie ','Rebecca ']
verb = ['play','eat','watch','sing']

for i in range(4):
    
     n = random.sample(noun,1)
     v = random.sample(verb,1)
     s = n[0]+v[0]
     print(s)
     