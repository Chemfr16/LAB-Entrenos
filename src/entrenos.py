from collections import namedtuple
import csv
from datetime import*


Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, \
                     duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(ruta_archivo):
    """lee_entrenos función que lee el archivo de entrenos y lo interpreta

    :param rutaarchivo: ruta del archivo .csv
    :type rutaarchivo: str
    :return: lista de tuplas con los datos
    :rtype: list[Tuple(Entreno)]
    """
    
    with open (ruta_archivo, encoding="utf-8") as f:
        lista_entrenos=[]
        lector=csv.reader(f)
        next(lector)
     
        for tipo, fechahora, ubicacion, duracion, \
             calorias, distancia, frecuencia, compartido in lector:
            fechahora= datetime.strptime(fechahora,"%d/%m/%Y %H:%M")
             
            duracion = int(duracion)
            calorias = int(calorias)
            distancia =float(distancia)
            frecuencia = int(frecuencia)
            compartido = compartido== "S"
            tupla= Entreno(tipo, fechahora, ubicacion, \
                     duracion, calorias, distancia, frecuencia, compartido)
            lista_entrenos.append(tupla)

            
    
    return lista_entrenos

def tipos_entreno(lista_entrenos):
    """tipos_entreno recibe una lista de tuplas de tipo Entreno

    :param lista_entrenos: lista de tuplas de tipo entreno
    :type lista_entrenos: list[Tuple(Entreno)]
    :return: Lista con los tipos de entrenamiento en orden alfabético
    :rtype: list(str)
    """
    tipos= set()
    for tupla in lista_entrenos:
        tipos.add(tupla.tipo)
    return sorted(list(tipos))



