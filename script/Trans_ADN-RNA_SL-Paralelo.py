import sys
import os
from os import listdir
from os.path import isfile, join
from datetime import datetime
#### import MPI #####
from mpi4py import MPI

def main():
    
    #start = datetime.now()
    fichero = (os.getcwd() + '/ADN/') ##  "C:\\Users\\JuanDiego\\Desktop\\Topicos_Telematica\\Proyecto4\\" #sys.argv[1] #1
    datasets = [archivotexto for archivotexto in listdir(fichero) if archivotexto[-4:] == ".txt"]  #Selecciona los archivos .txt 
    #print(datasets)
    ######################## Nuevo Guia: https://mpi4py.readthedocs.io/en/stable/tutorial.html#running-python-scripts-with-mpi  #######################
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    for x in range(len(datasets)):
     if rank == x:
        print(rank)
        data(datasets[x], fichero)


def data(datasets, fichero):

    sys.stdout.flush()
    fileName =  fichero + datasets
    print("File: " + fileName) #Ruta archivos TXT
    f = open(fileName, 'r') #Lee string de texto 
    
    resultado = open(os.getcwd() + '/resultadosRNA/resultadoRNA_' + datasets, 'w') ##Crea resultado en la carpeta indicada con el nombre indicado
    sys.stdout.flush()
    resultLine = ""
    
    
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
    f.close()   
    resultado.close()
  
start = datetime.now()  
sys.stdout.flush()
main()
end = datetime.now()
total = end - start
tiempo_total = total.seconds
print("Procesador: " + MPI.Get_processor_name() + ', Timpo de ejecución:' + str(tiempo_total) + "s")
sys.stdout.flush()
