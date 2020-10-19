
import os, sys, re
#exo1
def f(directory):
	for i in os.listdir(directory):
		i=directory+"/"+i
		if os.path.isdir(i):
			f(i)
		print(i)
f(sys.argv[1])

#exo2

dic1=open("dico1.txt",'r',encoding='utf-8')
dic2=open("dico2.txt",'r',encoding='utf-8')
sortie=open("resultat.txt",'w',encoding='utf-8')
a = []
b = []
for i in dic1.readlines():
	commun=False
	for j in dic2.readlines():
		if i == j:
			sortie.write("entrée commune : "+i.rstrip()+'\n')
			commun=True
	if commun==False:
		b.append(i)
	dic2.seek(0)
for c in b:
	sortie.write("entrée non commune dans dico1 : "+c)

#exo3

dic1=open("dico1.txt",'r',encoding='utf-8')
dic2=open("dico2.txt",'r',encoding='utf-8')
sortie=open("resultat.txt",'w',encoding='utf-8')
a = []
b = []
cpt1=1
cpt2=1
for i in dic1.readlines():
	commun=False
	for j in dic2.readlines():
		if i == j:
			cpt1+=1
			sortie.write("entrée commune : "+i.rstrip()+'\n')
			commun=True
	if commun==False:
		cpt2+=1
		b.append(i)
	dic2.seek(0)
for c in b:
	sortie.write("entrée non commune dans dico1 : "+c)
fact=1
for k in range(1,cpt1+1):
	fact=fact*k
print("la factorielle de la première catégorie est :",fact)
fact=1
for k in range(1,cpt2+1):
	fact=fact*k
print("la factorielle de la première catégorie est :",fact)
