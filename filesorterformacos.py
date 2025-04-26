import shutil, os
checks = [0,0,0,0]
# folder path
dir_path = input('Folder Path:')
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    f = os.path.join(dir_path, path)
    if os.path.isfile(f):
        l = len(str(f))
        if f[(-4):(l)] == '.png':
            if checks[0] == 0:
                path = os.path.join(dir_path, 'Images')
                os.mkdir(path)
                checks[0] = 1
            shutil.move(f, os.path.join(dir_path, 'Images'))
        elif f[(-4):(l)] == '.jpg':
            if checks[0] == 0:
                path = os.path.join(dir_path, 'Images')
                os.mkdir(path)
                checks[0] = 1
            shutil.move(f, os.path.join(dir_path, 'Images'))
        elif f[(-5):(l)] == '.jpeg':
            if checks[0] == 0:
                path = os.path.join(dir_path, 'Images')
                os.mkdir(path)
                checks[0] = 1
            shutil.move(f, os.path.join(dir_path, 'Images'))
        elif f[(-4):(l)] == '.pdf':
            if checks[1] == 0:
                path = os.path.join(dir_path, 'PDFs')
                os.mkdir(path)
                checks[1] = 1
            shutil.move(f, os.path.join(dir_path, 'PDFs'))
        elif f[(-5):(l)] == '.xlsx':
            if checks[2] == 0:
                path = os.path.join(dir_path, 'Excel Spreadsheets')
                os.mkdir(path)
                checks[2] = 1
            shutil.move(f, os.path.join(dir_path, 'Excel Spreadsheets'))
        elif f[(-5):(l)] == '.pptx':
            if checks[3] == 0:
                path = os.path.join(dir_path, 'PowerPoint Presentations')
                os.mkdir(path)
                checks[3] = 1
            shutil.move(f, os.path.join(dir_path, 'PowerPoint Presentations'))
