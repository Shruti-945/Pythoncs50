#random is  a library
#from random import choice       

import random

#number=random.randint(1,10)
cards=["jack","queen","king"]
random.shuffle(cards)
for card in cards:
  print(card)

