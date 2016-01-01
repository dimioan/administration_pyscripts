# This script selects all the txt files of a directory and copies them to a
# destination directory!!


import os,shutil

def copy_txt(src, directory):
    dir = os.path.abspath(directory)  # absolute path
    os.chdir(dir)
    c = 0
    for files in os.listdir(dir):
        if files.endswith('.txt'):
            file = os.path.abspath(files)
            shutil.copy2(file, '/home/bluesdio/Documents/My_Python/destination')
            c += 1
            #print file
    print 'Number of copied files: %g' %c
    #shutil.rmtree(dir)                    # remove folder and all of its contents
    os.chdir(src)


file_dir = '/home/bluesdio/Documents/My_Python/source'  # set source directory
os.chdir(file_dir)                # change working directory
print file_dir
for folders in os.listdir(file_dir):   
    print folders
    copy_txt(file_dir, folders)


    