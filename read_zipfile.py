import zipfile


#LIST CONTENTS OF A ZIPFILE
def list_zip_file(filepath):
    myzip = zipfile.ZipFile(filepath)

    return myzip.namelist()

list_zip_file('mjh.zip')


#ADD FILE TO A ZIPFILE
def add_file_to_zip(file,ziparchive,comment=None,pwd=None):

    with zipfile.ZipFile(ziparchive,'a') as myzip:
        myzip.write(file)
        if comment is not None:
            myzip.comment=comment.encode()

    myzip.close()
    print(file+' has been added to the zip file: '+ziparchive)

add_file_to_zip('code2run.log','mjh2.zip','code2run added by Marcus')

#EXTRACT FILE(S) FROM ZIPFILE
def extract_from_zip(filelist='ALL',ziparchive=None,trg_dir='.',pwd=None):

    with zipfile.ZipFile(ziparchive,'r') as myzip:
        if filelist=='ALL':            
            myzip.extractall(trg_dir,pwd)
            print('All files have been extracted from the zip file: '+ziparchive+' to folder: '+trg_dir)
        else:
            for file in filelist:
                myzip.extract(file,trg_dir,pwd)
                print(file+' has been extracted from the zip file: '+ziparchive+' to folder: '+trg_dir)                

    myzip.close()
    print('Extraction has finished')

extract_from_zip('ALL','mjh2.zip','./extract/log')






# # https://pypi.org/project/ruamel.std.zipfile/
# def remove_file_from_zip(file,ziparchive,pwd=None):

#     from ruamel.std.zipfile import delete_from_zip_file

#     #NOTE THE DOT IN PATTERN IS REQUIRED
#     delete_from_zip_file('mjh2.zip', pattern='.file_list.py')  



