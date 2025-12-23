# Vamos a crear varios ficheros(archivos) en python
texto = '''
Vamos a crear un fichero en python. Desde aqui me puedo apoyar para programar mis\n
clases creando un archivo para eso.
'''

fichero = open("01_fichero.txt", "w") # w indica escritura
print(type(fichero))
print(fichero)

fichero = open("01_fichero.txt", "r")

texto1 = fichero.read() # creo una nueva variable para poder leer el archivo
print(texto)

#fichero.write(texto) # esto es para escribir el archivo que escribi arriba
fichero.close()



