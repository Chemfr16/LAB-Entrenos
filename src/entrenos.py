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

def entrenos_duracion_superior(lista_entrenos,d):

    """entrenos_duracion_superior recibe una lista de tuplas de tipo Entreno
      y un valor entero d, y devuelve una lista con todos los entrenamientos
        que tienen una duración superior al valor d.

    :param lista_entrenos: lista de tuplas de tipo Entreno
    :type lista_entrenos: _type_
    :param d: _description_
    :type d: _type_
    :return: _description_
    :rtype: _type_
    """
    tiempos=set()
    for Entreno in lista_entrenos:
        if  Entreno.duracion>d:
            tiempos.add(Entreno)
            
    
    return list(tiempos) 


def suma_calorias(lista_entrenos,fecha1, fecha2):
    """suma_calorias _summary_

    :param lista_entrenos: recibe una lista de tuplas de tipo Entreno y dos fechas f_inicio y f_fin, 
    y devuelve la suma de  las calorías quemadas en todos los entrenamientos realizados 
    entre las dos fechas f_inicio y f_fin, ambas incluidas.
    :type lista_entrenos: _type_
    :param fecha1: _description_
    :type fecha1: date
    :param fecha2: _description_
    :type fecha2: date
    :return: _description_
    :rtype: int
    """
    #Agregado
    calorias= Entreno.calorias
    suma=0
    for Entreno in lista_entrenos:
        if (fecha1<=Entreno.fechahora<=fecha2):
            suma += calorias

    return suma
