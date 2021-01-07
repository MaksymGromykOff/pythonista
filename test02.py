# dictionary list for rivers and regions
dict = {'Amazon': 'South America'}

# add 2 more rivers and regions
dict['Missouri'] = 'North America'
dict['Dnipro'] = 'Europe'

# print list as separate sentences from dictionary
for key, value in dict.items():
  print (key, " runs through ", value)
