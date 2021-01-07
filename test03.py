# english-german dictionary wordlist
e2g = {
  'stork': 'storch', 
  'hawk': 'falke', 
  'woodpecker': 'specht', 
  'owl': 'eule'
}

# print translation for owl
print(e2g["owl"])

# add 2 words and translation
e2g["tree"]= "baum"
e2g["river"]= "fluss"

# print words and translation
for key, value in e2g.items():
  print (key, " : ", value)
