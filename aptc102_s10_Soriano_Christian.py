#Se define como se ocuparán los espacios en la tabla Hash
def hashing(H,v):
    return v%len(H)
        
#Se define el reHashing por si hay una colisión, toma el siguiente espacio en blanco
def reHashing(H,indiceHash):
    return indiceHash+1%len(H)

#Se definen los espacios de la tabla Hash y muestra donde ubicó cada dato con su número de ubicación
def hashTabla(datosA,datosB):
    print("ID  INDICE HASH")
    tablaLibros = [None] * 35

    for id in datosA:
        indiceHash = hashing(tablaLibros,id)
        while tablaLibros[indiceHash] != None:
            indiceHash = reHashing(tablaLibros,indiceHash)
        print(id,indiceHash)
        tablaLibros[indiceHash] = id

    for id in datosB:
        indiceHash = hashing(tablaLibros,id)
        while tablaLibros[indiceHash] != None:
            indiceHash = reHashing(tablaLibros,indiceHash)
        print(id,indiceHash)
        tablaLibros[indiceHash] = id

    return len(tablaLibros),tablaLibros
    
#Se indican los parámetros para la intersección entre los datos de los listados de libros A y B
def interseccion(n,H):
    res = []
    for i in range(n):
        if H[i] in datosA and H[i] in datosB and H[i] not in res:
            res.append(H[i])
    res.sort()
    print("\nINTERSECCIÓN RESULTANTE:\n" , res)

#Se indican los parámetros para la unión entre los datos de los listados de libros A y B
def union(n,H):
    res = []
    for i in range(n):
        if H[i] not in res and H[i] != None:
            res.append(H[i])
    res.sort()
    print("\nUNION RESULTANTE:\n",res)
    
#Carga los datos desde las planillas libros-A.csv y libros-B.csv
# y los asigna en variables para ubicarlos en la tabla Hash
with open('libros-A.csv', 'r') as t1, open('libros-B.csv', 'r') as t2:
    libros1 = t1.readlines()
    libros2 = t2.readlines()
    datosA = []
    datosB = []
    for linea in libros1:
        datosA.append(int(linea.split(',')[0]))
        
    for linea in libros2:
        datosB.append(int(linea.split(',')[0]))

    n,H = hashTabla(datosA,datosB)
    print("TAMAÑO DE LA TABLA HASH: ",n,"\nLISTADO DE LIBROS A + LIBROS B:\n",H)
    interseccion(n,H)
    union(n,H)
