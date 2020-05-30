import sys
from os import listdir
from os.path import isfile, join
from datetime import datetime

def main():
 
 start = datetime.now()
 directory = "C:\\Users\\JuanDiego\\Desktop\\Topicos_Telematica\\Proyecto4\\" #sys.argv[1] #1
 
 fna = [filename for filename in listdir(directory) if filename[-4:] == ".txt"]  #Selecciona los archivos .txt 

 for fnafile in fna: #Ciclo para que haga todos los archivos .txt
  
  fileName =  directory + fnafile
 
  print("File: " + fileName) #Ruta archivos TXT

  f = open(fileName, 'r') #Crea string de texto 
  
  res = open('C:\\Users\\JuanDiego\\Desktop\\Topicos_Telematica\\Proyecto4\\opt\\dna\\results\\' + fnafile + '.result', 'w') ##Crea resultado en la carpeta indicada
  resLine = ""
  
  for line in f:
   #print(line)
   if line[0] == '>': continue
   
   for i in line:
    #print(i)
    if i == 't':
     resLine += 'a'
    elif i == 'a':
     resLine += 'u'
    elif i == 'c':
     resLine += 'g'
    elif i == 'g':
     resLine += 'c'  
    else:
     resLine += i
   resLine += '\n'
  res.write(resLine)

  f.close()   
  res.close()
  
 end = datetime.now()
 total = end - start
 total_time = total.seconds
 print("Total time: " + str(total_time) + "s")
 
 
 #print("Hola")

if __name__ == '__main__':
 main()