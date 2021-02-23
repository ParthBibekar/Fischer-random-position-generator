import random

piece_list = ['K','Q','R','R','B','B','N','N']
l = random.sample(piece_list,8)

def random_list_generator(lst):
    lst = random.sample(piece_list,8)
    return placing_bishop(lst)
 
def placing_rook(lst1):
    if lst1[0] == 'K' or lst1[7] == 'K':
        return random_list_generator(lst1)
    else:
        for i in range(len(lst1)):
            if lst1[i] == 'K':
                a  = list(lst1[i-1::-1])
                g = a.count('R')
                if g == 1:
                    print(lst1)    
                else:
                    return random_list_generator(lst1)

def placing_bishop(lst2):
      m = lst2.index('B')
      n = lst2.index('B',m+1)
      if (m+n)%2 == 0:
          return random_list_generator(lst2)
      else:
          return placing_rook(lst2)
     
placing_bishop(l)