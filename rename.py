# This script counts the files that exist in a directory, reads and displays
# the first 15 characters of the txt-file.


import os

def count_files(directory):
    n = 0
    for file in os.listdir(directory):
        n += 1
    return n


def read_file(directory):
    c = 0
    for file in os.listdir(directory):
        c += 1
        infile = open(file, 'r')
        filestr = infile.read()
        print '\n%s ----- %d/%d' % (file,c,n)
        print 'File starts with:',filestr[:15]
        infile.close()

source_dir = '/home/bluesdio/Documents/My_Python/exercises/finaltxts'
os.chdir(source_dir)
print source_dir

n = count_files(source_dir)
print 'Number of files:',n

read_file(source_dir)

