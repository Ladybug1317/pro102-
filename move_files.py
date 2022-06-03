from distutils import extension
import os
import shutil
from_dir = "C:/Users/Jigna/Downloads"
to_dir = "C:/Users/Jigna/Desktop"
list_of_files = os.listdir(from_dir)
for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)

    if extension == " ":
        continue
    elif extension in ['.txt','.pdf','.doc','.docx','.jpeg']:
        path_1 = from_dir+'/'+file_name
        path_2 = to_dir+'/'+'document_files'
        path_3 = to_dir+'/'+'document_files'+'/'+file_name

        if os.path.exists(path_2):
            print("moving..."+file_name)
            shutil.move(path_1,path_3)

        else:
            os.makedirs(path_2)
            print("moving..."+file_name)
            shutil.move(path_1,path_3)