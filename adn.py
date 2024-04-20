Table_codonAA = [['Ph','TTT','TTC'],['Le','TTA','TTG','CTA','CTC','CTT','CTG'],['Iso','ATT','ATC','ATA'],['Me','ATG'],['Va','GTA','GTG','GTC','GTT'],['Se','TCA','TCG','TCT','TCC','AGT','AGC'],['Pr','CCA','CCG','CCC','CCT'],['Th','ACA','ACG','ACC','ACT'],['Al','GCA','GCG','GCC','GCT'],['Ty','TAT','TAC'],['Hi','CAT','CAC'],['Gl','CAA','CAG'],['As','AAT','AAC'],['Ly','AAA','AAG'],['Aa','GAT','GAC'],['Ag','GAA','GAG'],['Cy','TGT','TGC'],['Tr','TGG'],['Ar','CGA','CGG','CGC','CGT','AGA','AGG'],['Gy','GGA','GGG','GGC','GGT'],['STOP','TAA','TAG','TGA']]



ADN_1 = "ATGTACACAAACGCTTATTTGCGCTCTAACGTATAG"
#Se traduit par:    ['Me', 'Ty', 'Th', 'As', 'Al', 'Ty', 'Le', 'Ar', 'Se', 'As', 'Va']


ADN_2 = "ATGTACACAAACGCTTATTTGCGCTCTAACGTATAGATGTACACAAACGCTTATTTGCGCTCTAACGTATAG"

ADN_3 = "ATGCAAGTAGCGAATGATGTTTGCTAAATGTGTCCTGATCGGCTATTACTGTTTCTGTGAATGAACCGGATGCTGCCTAAGATTTCACTGACAGGCTTTACTGTTCATAACTAAATGCAACGGCGTAAGGCAAGAGAAAAGAAACGACCGTAGATGGAAGTCTGTCACTGTTTGACGAAGCATGGCGGTACAGTGAATCACTAAATGTGGGAGTTGACTGGATGAATGAACCGACGAGGAAGGATGTGAATGCCAGACCATTGCATTGTCAGAACTTCACATTGCTGAATGCCTTATGTACGAACAGCACCACTACACTCATGAATGTTCAAAGTTATTGGAGCTCCCCCAAACTTGGGATCTAGTATGGACCTTCATTGGCGTTAAATGAACCCAGGCTCCTCAATATAAATGACCGACACGGAAGAATGCTCTTCTTGA"
# La séquence contient 12 gène(s):
# ['Me', 'Gl', 'Va', 'Al', 'As', 'Aa', 'Va', 'Cy']
# ['Me', 'Cy', 'Pr', 'Aa', 'Ar', 'Le', 'Le', 'Le', 'Ph', 'Le']
# ['Me', 'As', 'Ar', 'Me', 'Le', 'Pr', 'Ly', 'Iso', 'Se', 'Le', 'Th', 'Gy', 'Ph', 'Th', 'Va', 'Hi', 'As']
# ['Me', 'Gl', 'Ar', 'Ar', 'Ly', 'Al', 'Ar', 'Ag', 'Ly', 'Ly', 'Ar', 'Pr']
# ['Me', 'Ag', 'Va', 'Cy', 'Hi', 'Cy', 'Le', 'Th', 'Ly', 'Hi', 'Gy', 'Gy', 'Th', 'Va', 'As', 'Hi']
# ['Me', 'Tr', 'Ag', 'Le', 'Th', 'Gy']
# ['Me', 'As', 'Ar', 'Ar', 'Gy', 'Ar', 'Me']
# ['Me', 'Pr', 'Aa', 'Hi', 'Cy', 'Iso', 'Va', 'Ar', 'Th', 'Se', 'Hi', 'Cy']
# ['Me', 'Pr', 'Ty', 'Va', 'Ar', 'Th', 'Al', 'Pr', 'Le', 'Hi', 'Se']
# ['Me', 'Ph', 'Ly', 'Va', 'Iso', 'Gy', 'Al', 'Pr', 'Pr', 'As', 'Le', 'Gy', 'Se', 'Se', 'Me', 'Aa', 'Le', 'Hi', 'Tr', 'Ar']
# ['Me', 'As', 'Pr', 'Gy', 'Se', 'Se', 'Iso']
# ['Me', 'Th', 'Aa', 'Th', 'Ag', 'Ag', 'Cy', 'Se', 'Se']








def Codons(adn) :
  lst = [] #on crée une liste vide
  n = 0 #on crée 3 variables qui représentent 3 lettres
  l = 1
  f = 2
  p = int(len(adn) / 3) #on cherche le nombre de lettre et on divise par 3 pour savoir jusqu'ou s'étend la boucle (ce qui nous assure que le nombre de nucléotides sont des multiples de 3)
  for g in range (0, p):
    lst.append([]) #on ajoute des mini listes dans la grande liste
    lst[g].append(adn[n] + adn[l] + adn[f]) #on ajoute à la liste les 3 lettres, puis encore 3 diférentes et ainsi de suite.
    #print(g)
    #print((adn[n] + adn[l] + adn[f]))
    n += 3
    l += 3 #les variables n, l et f augmentent de 3 à chaque tout de boucle (elles passent de : 0, 1, 2 à 3, 4, 5 et ainsi de suite)
    f += 3
    
  return lst #on met fin à la fonction
#print(Codons(ADN_1))
#print(Codons(ADN_2))
#print(Codons(ADN_3))





def Traduire(Codons) :
  lst = []
  for i in Codons: #on parcoure la liste des codons
    #print(i[0])
    for g in range (0, 21):
      #print(g)
      #print(Table_codonAA[g])
      #print(Table_codonAA[g][0])
      if i[0] in (Table_codonAA[g]): #on vérifie si les éléments de la liste des codons se trouvent dans la liste "Table_codonAA"
        lst.append(Table_codonAA[g][0]) #Et, si oui, on ajoute l'acide aminé qui lui correspond à la liste
  return lst #on met fin à la fonction

#print(Traduire(Codons(ADN_1)))
#print(Traduire(Codons(ADN_2)))
#print(Traduire(Codons(ADN_3)))
#['Me', 'Ty', 'Th', 'As', 'Al', 'Ty', 'Le', 'Ar', 'Se', 'As', 'Va', 'STOP']





def LireGenes(Traduire):
  lst = []
  t = [index for index, value in enumerate(Traduire) if value == "STOP"] #on cherche tous les index de "STOP" et on les mets dans une liste
  f = 0
  for i in t: #On parcoure tous les index de "STOP"
    #print(i)
    lst.append(Traduire[f :i]) #on ajoute à la liste les valeurs entre les index de 0 et "STOP", puis entre "STOP" et "STOP"
    f = i #on stocke l'index de STOP pour le réutiliser
  for h in range (0, len(lst)):
    if "STOP" in lst[h]:
      lst[h].remove('STOP') #On suprime touts les "STOP"
  return lst #on met fin à la fonction

#print(LireGenes(Traduire(Codons(ADN_1))))
#print(LireGenes(Traduire(Codons(ADN_2))))
#print(LireGenes(Traduire(Codons(ADN_3))))






def LireADN(LireGenes):
  print("La séquence contient ", len(LireGenes)," gène(s):") #on affiche le nombre de gènes
  for i in range (0, len(LireGenes)):
    print(LireGenes[i]) #on afiche la séquence de gènes
  return "" #on fait en sorte que le messsage "none" ne s'affiche pas

#print(LireADN(LireGenes(Traduire(Codons(ADN_1)))))
#print(LireADN(LireGenes(Traduire(Codons(ADN_2)))))
#print(LireADN(LireGenes(Traduire(Codons(ADN_3)))))
