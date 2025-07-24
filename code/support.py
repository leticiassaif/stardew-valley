from os import walk

def import_folder(path):
    surface_list = []
    
    for _, __, img_files in walk(path):
        print(img_files)
    
    return surface_list