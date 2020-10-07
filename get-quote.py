import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 18
  rnd = random.randint(0, last)
  rnd2 = random.randint(0, last)
  quotesrndlines = (quotes[rnd].replace('\n', '')+ ". " +quotes[rnd2].replace('\n', ''))
  print(quotesrndlines)
  
  current_file = 'quotes.txt'
  new_file = 'my_new_quotes.txt'
  with open(current_file, 'r') as reader, open(new_file, 'w') as writer:
   quotes = reader.readlines()
   for frase in quotes:
    if not frase.strip() == "Anything added dilutes everything else".strip():
     writer.write(frase)
	
if __name__== "__main__":
  primary()
