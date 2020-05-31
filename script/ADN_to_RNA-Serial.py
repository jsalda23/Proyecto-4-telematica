import sys
import os
from os import listdir
from os.path import isfile, join
from datetime import datetime

def main():
    print(os.getcwd())
    start = datetime.now()
    fichero = (os.getcwd() + '\\') ##  "C:\\Users\\JuanDiego\\Desktop\\Topicos_Telematica\\Proyecto4\\" #sys.argv[1] #1
    
    datasets = [archivotexto for archivotexto in listdir(fichero) if archivotexto[-4:] == ".txt"]  #Selecciona los archivos .txt 
    
    for archivodna in datasets: #Ciclo para que haga todos los archivos .txt
        fileName =  fichero + archivodna
        print("File: " + fileName) #Ruta archivos TXT
        f = open(fileName, 'r') #Lee string de texto 
        resultado = open(os.getcwd() + '\\resultadosRNA\\resultadoRNA_' + archivodna, 'w') ##Crea resultado en la carpeta indicada con el nombre indicado
        resultLine = ""
        print(resultLine)
        for line in f:
            #print(line)
            if line[0] == '>': continue
   
            for i in line:
            #print(i)
                if i == 't':
                    resultLine += 'a'
                elif i == 'a':
                    resultLine += 'u'
                elif i == 'c':
                    resultLine += 'g'
                elif i == 'g':
                    resultLine += 'c'  
                else:
                    resultLine += i
            resultLine += '\n'
        resultado.write(resultLine)
        #f.close()   
        resultado.close()
  
    end = datetime.now()
    total = end - start
    tiempo_total = total.seconds
    print("Tiempo de ejecución: " + str(tiempo_total) + "s")
    print("Numero de archivos transcritos: " + str(len(datasets)))
    #print("Hola")

if __name__ == '__main__':
 main()
