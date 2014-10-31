from os import walk
import os.path

def inning_files(root):
    """
    @param root: the directory to scan for inning.xml files
    @return: a list of path names of all the inning.xml files
    """

    #initialize the return variable
    inning_file_list = []

    #traverse all the files in the directory
    for path, subdirs, files in walk(root):
        for name in files:
            #add the inning files to the return variable
            if name.endswith('inning.xml'):
                inning_file_list.append(os.path.join(path, name))

    return inning_file_list

if __name__ == "__main__":
    root = 'data/'
    print inning_files(root)
