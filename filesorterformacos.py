import shutil
import os

# folder path
dir_path = input('Folder Path:')
# list to store files
res = []
path = os.path.join(dir_path, 'Images') 
os.mkdir(path) 
path = os.path.join(dir_path, 'PDFs') 
os.mkdir(path)
path = os.path.join(dir_path, 'Excel Spreadsheets') 
os.mkdir(path)
path = os.path.join(dir_path, 'PowerPoint Presentations') 
os.mkdir(path)
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    foldervar = os.path.join(dir_path, path)
    if os.path.isfile(foldervar):
        if foldervar[-4] + foldervar[-3] + foldervar[-2] + foldervar[-1] == '.png':
            shutil.move(foldervar, os.path.join(dir_path, 'Images'))
        elif foldervar[-4] + foldervar[-3] + foldervar[-2] + foldervar[-1] == '.jpg':
            shutil.move(foldervar, os.path.join(dir_path, 'Images'))
        elif foldervar[-5] + foldervar[-4] + foldervar[-3] + foldervar[-2] + foldervar[-1] == '.jpeg':
            shutil.move(foldervar, os.path.join(dir_path, 'Images'))
        elif foldervar[-4] + foldervar[-3] + foldervar[-2] + foldervar[-1] == '.pdf':
            shutil.move(foldervar, os.path.join(dir_path, 'PDFs'))
        elif foldervar[-5] + foldervar[-4] + foldervar[-3] + foldervar[-2] + foldervar[-1] == '.xlsx':
                shutil.move(foldervar, os.path.join(dir_path, 'Excel Spreadsheets'))
        elif foldervar[-5] + foldervar[-4] + foldervar[-3] + foldervar[-2] + foldervar[-1] == '.pptx':
                shutil.move(foldervar, os.path.join(dir_path, 'PowerPoint Presentati'))
