import os
import shutil

list_of_files = []

from_dir = r"C:\Users\Dell\Downloads"
to_dir = r"C:\Users\Dell\Pictures\Arquivos_documentos"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for files in list_of_files:
    files = os.path.splitext(files)
    print(files)
    