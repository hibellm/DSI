
import os


def file_list(path):

    file_list = []

    for root,dir,files in (os.walk(path)):
        
        for file in files:
            file_list.append(os.path.join(root,dir,file))

    for file in file_list:
        print(file)

    return file_list    




x=file_list('.')    
