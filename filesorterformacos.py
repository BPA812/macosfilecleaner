import shutil
import os
checks = [0,0,0,0]
# folder path
dir_path = input('Folder Path:')
# list to store files
res = []
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    foldervar = os.path.join(dir_path, path)
    if os.path.isfile(foldervar):
        if foldervar[-4] + foldervar[-3] + foldervar[-2] + foldervar[-1] == '.png':
            if checks[0] == 0:
                path = os.path.join(dir_path, 'Images')
                os.mkdir(path)
                checks[0] = 1
            shutil.move(foldervar, os.path.join(dir_path, 'Images'))
        elif foldervar[-4] + foldervar[-3] + foldervar[-2] + foldervar[-1] == '.jpg':
            if checks[0] == 0:
                path = os.path.join(dir_path, 'Images')
                os.mkdir(path)
                checks[0] = 1
            shutil.move(foldervar, os.path.join(dir_path, 'Images'))
        elif foldervar[-5] + foldervar[-4] + foldervar[-3] + foldervar[-2] + foldervar[-1] == '.jpeg':
            if checks[0] == 0:
                path = os.path.join(dir_path, 'Images')
                os.mkdir(path)
                checks[0] = 1
            shutil.move(foldervar, os.path.join(dir_path, 'Images'))
        elif foldervar[-4] + foldervar[-3] + foldervar[-2] + foldervar[-1] == '.pdf':
            if checks[1] == 0:
                path = os.path.join(dir_path, 'PDFs')
                os.mkdir(path)
                checks[1] = 1
            shutil.move(foldervar, os.path.join(dir_path, 'PDFs'))
        elif foldervar[-5] + foldervar[-4] + foldervar[-3] + foldervar[-2] + foldervar[-1] == '.xlsx':
            if checks[2] == 0:
                path = os.path.join(dir_path, 'Excel Spreadsheets')
                os.mkdir(path)
                checks[2] = 1
            shutil.move(foldervar, os.path.join(dir_path, 'Excel Spreadsheets'))
        elif foldervar[-5] + foldervar[-4] + foldervar[-3] + foldervar[-2] + foldervar[-1] == '.pptx':
            if checks[3] == 0:
                path = os.path.join(dir_path, 'PowerPoint Presentations')
                os.mkdir(path)
                checks[3] = 1
            shutil.move(foldervar, os.path.join(dir_path, 'PowerPoint Presentations'))
