import os

listaFotos = []

os.chdir("renomeia_ fotos\img") #Seleciona o diretório

for foto in os.listdir():       #Adiciona os nomes dos arquivos a uma lista
    listaFotos.append(foto)

for i in range(len(listaFotos)):
    os.rename(listaFotos[i],f'Lianna_{str(i+1)}')   # Modifica os nome dos arquivos

print(listaFotos)