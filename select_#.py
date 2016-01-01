# This script measures the number of files that exist in a directory, then opens and
# reads the txt-files. If the txt file starts with #, the script copies this file to
# a destination directory.


import os
import shutil

def count_files(directory):
    n = 0
    for file in os.listdir(directory):
        n += 1
    return n


def copy_file(directory):
    c = 0
    for file in os.listdir(directory):
        c += 1
        infile = open(file, 'r')
        filestr = infile.read()
        print '\n%s ----- %d/%d' % (file,c,n)
        #print 'File starts with:',filestr[:5]
        infile.close()
        if filestr.startswith('#'):
            file = os.path.abspath(file)
            print 'COPIED!!!!'
            shutil.copy2(file, '/home/bluesdio/Documents/My_Python/exercises/finaltxts')
            
            

source_dir = '/home/bluesdio/Documents/textfiles'
os.chdir(source_dir)
print source_dir

n = count_files(source_dir)
print 'Number of files:',n

copy_file(source_dir)


    