# the destination folder must not already exist!!!

import shutil
import time
import sys

def copy_directories(source, destination):
    shutil.copytree(source, destination)
    toolbar_width = 50
    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
    for i in xrange(toolbar_width):
        time.sleep(0.1) # do real work here
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()
    sys.stdout.write("\nDONE!!!!!!!\n")



source_dir1= '/home/bluesdio/Documents/Attiki'
destination_dir1 = '/home/bluesdio/Documents/My_Python/destination/test1'

source_dir2 = '/home/bluesdio/Documents/My_Python/Pele'
destination_dir2 = '/home/bluesdio/Documents/My_Python/destination/test2'

copy_directories(source_dir1, destination_dir1)
time.sleep(3)
copy_directories(source_dir2, destination_dir2)
