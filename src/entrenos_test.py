from entrenos import*
def test_lee_entrenos():
    print("Prueba de lee_entrenos:")
    entrenos=lee_entrenos("data/entrenos.csv")
    print(entrenos[:3])
    print(entrenos[-3:])

def test_tipos_entreno(entrenos):
    print("Prueba de tipos_entrenos")
    tipos=tipos_entreno(entrenos)
    print(tipos)

def test_entrenos_duracion_superior(entrenos):
    tiempos=entrenos_duracion_superior(entrenos,40)
    print(tiempos)



if __name__=="__main__":
    entrenos=lee_entrenos("data/entrenos.csv")
    #test_lee_entrenos()
    test_entrenos_duracion_superior(entrenos)
