import os
import shutil

pasta_raiz = os.chdir("E:\Downloads\Cosmos")

for folder in os.listdir():
    if os.path.isdir(folder):
        os.chdir("E:\Downloads\Cosmos"+ "\\" + str(folder))
        for file in os.listdir():
            if '.mkv' in file:
                shutil.move("E:\Downloads\Cosmos"+ "\\" + str(folder) + "\\" + str(file), "E:\Downloads\Cosmos"+ "\\" + str(file))
    os.chdir("E:\Downloads\Cosmos")


