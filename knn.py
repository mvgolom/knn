import sys
import os
#for param in sys.argv :
#	print(param)

if(len(sys.argv) != 5) :
 print("knn.py teste treino k  qtTreino->| %25 | %50 | %100 |")
 sys.exit()


if((int(sys.argv[4]) != 25) and (int(sys.argv[4]) != 50) and (int(sys.argv[4]) != 100)) :
 print("qtTreino fora do intervalo "+sys.argv[4])
 print("qtTreino: %25 | %50 | %100|")
 sys.exit()

def getElements(elemn) :
 i = 0
 global teste
 aux2 = []
 aux = []
 aux = elemn.split(",")
 for x in aux:

  if(i == 24):
   aux2.append(x.strip(" "))

  if(i != 24):
   aux2.append(float(x.strip(" ")))

  i = i+1

 teste.append(aux2)

arq = open(sys.argv[1],'r')
arq2 = open(sys.argv[2],'r')
elementosTeste = arq.readlines()
elementosTreino = arq2.readlines()


teste = []
getElements(elementosTeste[0])

for x in teste[0]:
	print(type(x))


k = int(sys.argv[3])
qtElements = int(sys.argv[4])



#os.system('CLS')
#former = arq.readlines()