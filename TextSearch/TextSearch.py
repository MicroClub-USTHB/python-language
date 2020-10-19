import sys,re
texte=open(sys.argv[1],'r',encoding='utf-8')
sortie=open("resultat.txt",'w',encoding='utf-8')
dic = {}
long = int(sys.argv[2])
freq = int(sys.argv[3])
lenfirst = int(sys.argv[4])
lenlast = int(sys.argv[5])
list = []
for ligne in texte :
    m = re.split("\W+",ligne.lower())
    for i in range(len(m)):
        if(len(m[i])==lenfirst):
            ch = m[i]
            for j in range(i+1,i+long):
                if(j<len(m)):
                    ch += " " + m[j]
                    if(len(m[j])==lenlast):
                        list.append(ch)
for c in list :
    dic[c] = dic.get(c,0)+1
for k in sorted(dic):
    if dic.get(k)<=freq:
        sortie.write(k+" : "+str(dic.get(k))+"\n")