import os
import shutil

def getExtension (file):
    return (os.path.splitext(file)[1][1:])
    
def organizeAll():
    file_no = 0
    for file in all_files:
        cur_ext = getExtension(file)
        new_path = os.path.join(path, cur_ext)
        if cur_ext != "":
            if cur_ext not in ext_list and not os.path.exists(new_path):
                os.mkdir(new_path)
                ext_list.append(cur_ext)
            shutil.move(path+"/"+file, new_path+"/"+file)
            file_no += 1
    print(file_no , "files organized!")

#dir
path = "C:/Users/Batu/test" 
all_files = os.listdir(path)
ext_list = []
organizeAll()