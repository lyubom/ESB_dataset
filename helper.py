import os
import random
import math

"""change all spaces to _ (run several times)"""
def remove_spaces():
    basedir = '.'
    for fn in os.listdir(basedir):
        if not os.path.isdir(os.path.join(basedir, fn)):
            continue # Not a directory
        if ',' in fn:
            continue # Already in the correct form
        if ' ' not in fn:
            continue # Invalid format
        firstname,_,surname = fn.rpartition(' ')
        os.rename(os.path.join(basedir, fn),
                os.path.join(basedir, firstname + '_' +surname ))
    print("Spaces are removed")

"""rename .STL to .stl"""
def rename_stl():
    for (dirname, dirs, files) in os.walk('.'):
        for filename in files:
            if filename.endswith('.STL') :
                print(dirname)
                infile = filename.split('.')[0]
                inp = os.path.join(dirname, filename)
                outp = os.path.join(dirname, infile+'.stl')
                os.rename(inp, outp)
    print("STL renamed")

"""count points in file"""
def count_points():
    count_min = 1000000
    count = 0
    for (dirname, dirs, files) in os.walk('.'):
        for filename in files:
            if filename.endswith('.txt'):
                infile = os.path.join(dirname, filename)
                num_lines = sum(1 for line in open(infile))
                if num_lines < 600:
                    print(filename, num_lines)
                    # os.remove(infile)
                    count += 1
        
                if num_lines < count_min:
                    count_min = num_lines
    print("file under 500 points", count)

"""write to file all filenames"""
def filelist():
    filelist = "filelist.txt"
    with open(filelist, 'w') as f:
        for (dirname, dirs, files) in os.walk('.'):
            for filename in files:
                if filename.endswith('.txt') and filename != filelist:
                    f.write(filename+'\n')
    print("Filenames written to file")

"""write to file all class names"""
def classes_list():
    classes = "shape_names.txt"                 
    with open(classes, 'w') as f:
        for (dirname, dirs, files) in os.walk('.'):
            last_dir_name = dirname.split('\\')[-1]
            if not last_dir_name.startswith('.'):
                print(last_dir_name)
                f.write(last_dir_name+'\n')
    print("Class list written to file")

"""split to train/test data"""
def split_dataset():
    train = []
    test = []

    for (dirname, dirs, files) in os.walk('.'):
        print(dirname)
        if len(dirname) != 1: # ignore root folder
            dir_files = []
            for filename in files:
                if filename.endswith('.txt'):
                    infile = filename.split('.')[0]
                    dir_files.append(infile)
            random.Random(4).shuffle(dir_files)
            size = len(dir_files)
            train_part = int(round(0.7 * size, 0))
            for i in range(0, train_part):
                train.append(dir_files[i])
            for i in range(train_part, len(dir_files)):
                test.append(dir_files[i])
        

    with open ("train.txt", "w") as f:
        for i in train:
            f.write(str(i) + "\n")

    with open ("test.txt", "w") as f:
        for i in test:
             f.write(str(i) + "\n")
    
    print("Dataset is split")
        
count_points()        
split_dataset()     