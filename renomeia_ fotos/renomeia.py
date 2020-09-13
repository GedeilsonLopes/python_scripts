import os

listaFotos = []

os.chdir("renomeia_ fotos\img")

for foto in os.listdir():
    listaFotos.append(foto)

for i in range(len(listaFotos)):
    os.rename(listaFotos[i],f'Lianna_{str(i+1)}')

print(listaFotos)