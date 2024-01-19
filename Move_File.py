import os
import shutil

from_dir = 'Arquivos_Documentos'
to_dir = 'Arquivos_Imagem'

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.png','.jpg','.jpeg','.gif', '.avif']:
        path1 = from_dir +'/'+ file_name
        path2 = to_dir +'/'+ 'Imagens'
        path3 = to_dir +'/'+ 'Imagens'+'/'+ file_name

        if os.path.exists(path2):
            print('Movendo '+file_name+'...')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('Movendo '+file_name+'...')   
            shutil.move(path1,path3) 

