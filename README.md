# Universidad EAFIT
# Curso ST0263 Tópicos Especiales en Telemática, 2020-1
# Estudiante: Juan Diego Saldarriaga - jsalda23@eafit.edu.co
# Trabajo 4 - HPC
### Trabajo individual

# Transcripción ADN a ARN
## 1. Caso de estudio a resolver

Durante le ejecución de este proyecto vamos a resolver el problema descrito en la página: http://rosalind.info/problems/rna/

Este problema consiste en realizar la transcripción de ADN a ARN. Está transcripción es el primer paso de la expresión genética (Proceso por el cual se codifican los ácidos nucleicos en proteínas). Este proceso consta de 3 etapas:
* Iniciación: La ARN polimerasa se une a una secuencia de ADN que se encuentra al inicio del un gen. Una vez unida, la ARN polimerasa separa las cadenas de ADN para proporcionar el molde de cadena sencilla necesario para la transcripción. [2]
* Elongación: El transcrito de ARN tiene la misma información que la cadena de ADN, pero contraria al molde en el gen. Sin embargo, a diferencia de la cadena ADN contiene la base uracilo (U) en lugar de timina (T). [2]
* Terminación: Una vez transcritas, estas secuencias provocan que el transcrito sea liberado de la ARN polimerasa. [2]
Una cadena ADN está compuesta por adenina (A), citosina (C), guanina (G) y timina (T), por lo tanto, para su fácil manejo y comprensión, se trabaja con sus siglas A, C, G y T. La cadena ARN a diferencia de la ADN está compuesta por A, C, G y uracilo (U). Sin embargo, cuando se pasa de ADN a ARN la T cambia por A, la A cambia por U, la C cambia por G, y la G cambia por C, así como se evidencia en la siguiente imagen:

![](Imagenes/ARNpolimerasa.png)
<h20> Imagen e información extraída de: https://es.khanacademy.org/science/biology/gene-expression-central-dogma/transcription-of-dna-into-rna/a/overview-of-transcription </h20>

## 2. Solución Serial
La solución serial se encuentra en el archivo Scripts, bajo el nombre "Trans_ADN-RNA_SL-Secuencial". Consiste en una solución simple, donde se inicia con la lectura de todos los ficheros de texto (los cuales contienen las secuencias de ADN) y posteriormente su conversión. Para está solución simple el programa coge los archivos de texto, uno por uno, linea por linea y realiza la transcripción.

Esta soluición se ejecuta con el comando:

__python3 Trans_ADN-RNA_SL-Secuencial.py__

## 3. Solución Paralela
Para la solución serial se decidió usuar la libreria mpi4py (https://mpi4py.readthedocs.io/en/stable/index.html) la cual nos permite hacer uso de multiples procesadores, ademas de ser adecuado para trabajar con memoria compartida.
Se evaluaron diferentes maneras de realizar una solución usando paralelismo, sin embargo, se determinó que se dividirían las cadenas de ADN (secuencias de 10,000,000 de caracteres), así, cada nodo realiza la transcripción de una secuencia de ADN. Por lo tanto la solución trabaja con 5 nodos, cada nodo con una secuencia de ADN diferente.

Esta soluición se ejecuta con el comando:

__mpirun -n 5 python3 Trans_ADN-RNA_SL-Paralelo.py__

### Nota
Para realizar las pruebas de ambas soluciones se usaron las 5 secuencias de la carpeta "datasets". Estas secuencias fueron generadas aleatoriamente desde la página "https://www.bioinformatics.org/sms2/random_dna.html" con una longitud de 10,000,000 de caracteres cada una.

## 4. Rendimiento

### 4.1. Escenarios:

#### 4.1.1. 1 procesador vs 2 procesadores -> 2 secuencias de DNA
![](Imagenes/2%20archivos%20-%201pVs2p.PNG)

- Tiempo(1 procesador) = 3.947s
- Tiempo(2 procesadores) = 2.268s
- ***SpeedUp Relativo = 3.947s / 2.268s = 1.740***
- ***Eficiencia E(P) = 1.7403 / 2 = 0.870***

#### 4.1.2. 1 procesador vs 3 procesadores -> 3 secuencias de DNA
![](Imagenes/3%20archivos%20-%201pVs3p.PNG)

- Tiempo(1 procesador) = 5.926s
- Tiempo(3 procesadores) = 4.091s
- ***SpeedUp Relativo = 5.926s / 4.091s = 1.448***
- ***Eficiencia E(P) = 1.448 / 3 = 0.482***

#### 4.1.3. 1 procesador vs 4 procesadores -> 4 secuencias de DNA
![](Imagenes/4%20archivos%20-%201pVs4p.PNG)

- Tiempo(1 procesador) = 7.236s
- Tiempo(4 procesadores) = 4.432s
- ***SpeedUp Relativo = 7.236s / 4.432s = 1.632***
- ***Eficiencia E(P) = 1.632 / 4 = 0.408***

#### 4.1.4. 1 procesador vs 5 procesadores -> 5 secuencias de DNA
![](Imagenes/5%20archivos%20-%201pVs5p.PNG)

- Tiempo(1 procesador) = 11.265s
- Tiempo(5 procesadores) = 5.896s
- ***SpeedUp Relativo = 11.265s / 5.986s = 1.882***
- ***Eficiencia E(P) = 1.882 / 5 = 0.376***

#### 4.1.5. 1 procesador vs 2 procesadores -> 1 secuencia de DNA
![](Imagenes/UnaSecuencia-1pVs2p.PNG)

- Tiempo(1 procesador) = 2.007s
- Tiempo(2 procesadores) = 1.414s
- ***SpeedUp Relativo = 2.007s / 1.414s = 1.419***
- ***Eficiencia E(P) = 1.419 / 2 = 0.709***

#### 4.1.6. 1 procesador vs 3 procesadores -> 1 secuencia de DNA
![](Imagenes/UnaSecuencia-1pVs3p.PNG)

- Tiempo(1 procesador) = 2.128s
- Tiempo(3 procesadores) = 1.756s
- ***SpeedUp Relativo = 2.128s / 1.756s = 1.263***
- ***Eficiencia E(P) = 1.263 / 3 = 0.421***

#### 4.1.7. 1 procesador vs 4 procesadores -> 1 secuencia de DNA
![](Imagenes/UnaSecuencia-1pVs4p.PNG)

- Tiempo(1 procesador) = 2.292s
- Tiempo(4 procesadores) = 1.737s
- ***SpeedUp Relativo = 2.292s / 1.737s = 1.319 
- ***Eficiencia E(P) = 1.319 / 4 = 0.329***

#### 4.1.8. 1 procesador vs 5 procesadores -> 1 secuencia de DNA
![](Imagenes/UnaSecuencia-1pVs5p.PNG)

- Tiempo(1 procesador) = 2.082s
- Tiempo(5 procesadores) = 2.027s
- ***SpeedUp Relativo = 2.082s / 2.027s = 1.027
- ***Eficiencia E(P) = 1.027 / 5 = 0.205***

### 4.2. Conclusiones
Luego de realizar los análisis de SpeedUp y de Eficiencia podemos evidenciar inicialmente, que es evidente que el tiempo de ejecución es menor para la solución paralela.

Para los casos de prueba, donde aumentamos el numero de secuencias a transcribir, proporcionalmente al numero de procesadores, evidenciamos que a medida que se aumenta el numero de procesadores el SpeedUp es mayor, a excepción de cuando tenemos 2 procesadores, que inesperadamente tiene el segundo mejor SpeedUP. Sin embargo, cuando vemos la eficiencia, identificamos que es más eficiente (con un 0.87) tener 2 procesadores para realizar la transcripción, que tener 3, 4 o 5, siendo este último el menos eficiente

![](Imagenes/NsecuenciasNprocesadores.PNG) 

Para los casos de prueba, donde aumentamos el numero de procesos, mientras mantenemos solamente 1 secuencia a transcribir, evidenciamos que el SpeedUp es menor a medida que aumentan los procesadores. Esto se debe a que con una sola secuiencia a transcribir, la solución serial siempre se demora aproximadamente lo mismo, mientras para la solución paralela simplemente estamos dividiendo la secuencia y aumentando el numero de comunicaciones necesarias, es decir, aunque se demora menos que la solución secuencial, para este caso, tener más procesadores no es tan beneficioso. Lo mismo pasa con la eficiencia, tenemos una eficiencia más baja para todos los casos, y el tener 2 procesadores sigue siendo la mejor alternativa.

![](Imagenes/1secuenciaNprocesadores.PNG) 

# 5. Video

#### Youtube: https://www.youtube.com/watch?v=L-pQ6vP7zMA
#### MicrosoftStream: https://web.microsoftstream.com/video/49ddfb31-c062-4de3-b642-b1a6dd5ae251
*Nota: Es el mismo video en ambas plataformas*

# 6. Bibliografia
###### [1] http://rosalind.info/problems/rna/
###### [2] https://es.khanacademy.org/science/biology/gene-expression-central-dogma/transcription-of-dna-into-rna/a/overview-of-transcription
###### [3] https://www.genome.gov/es/genetics-glossary/ACGT
###### [4] https://mpi4py.readthedocs.io/en/stable/
###### [5] https://es.wikipedia.org/wiki/MIMD
###### [6] https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html
###### [7] https://www.bioinformatics.org/sms2/random_dna.html
###### [8] https://es.wikipedia.org/wiki/Speedup

