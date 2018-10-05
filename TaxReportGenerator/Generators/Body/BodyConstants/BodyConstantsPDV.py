# -*- encoding: utf-8 -*-

#Create a list of XML tags
number_list_8XX = list(range(810,816)) + [820] + list(range(830,834)) + list(range(840,871,10))

list_of_1XX_tags =  ["Podatak"+str(x) for x in range(100,111)]
list_of_2XX_tags =  ["Podatak"+str(x) for x in range(200,216)]
list_of_3XX_tags =  ["Podatak"+str(x) for x in range(300,316)]
list_of_4567_tags = ["Podatak"+str(x) for x in range(400,701,100)]
list_of_8XX_tags = ["Podatak"+str(x) for x in number_list_8XX]

#Initialize who is whose child
child_tags = {"Tijelo" : ["Podatak000"] + list_of_1XX_tags + list_of_2XX_tags + list_of_3XX_tags +
                          list_of_4567_tags + list_of_8XX_tags,
              }

#Add child tags to the rest of tags
porez_vrijednost_tags = list_of_2XX_tags + list_of_3XX_tags
porez_vrijednost_tags = porez_vrijednost_tags[:-1]
for tag in porez_vrijednost_tags:
  child_tags[tag] = ["Vrijednost", "Porez"]
  
broj_vrijednost_tags = ["Podatak"+str(x) for x in range(831, 834)]
for tag in broj_vrijednost_tags:
  child_tags[tag] = ["Vrijednost", "Broj"]
  