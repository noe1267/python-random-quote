import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rdn = random.randint(0,last)
  print(quotes[rdn])

if __name__== "__main__":
  primary()
