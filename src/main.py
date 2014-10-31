from os import walk
import os.path

#import the C implementation of ElementTree for speed
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


def inning_files(root_dir):
    """
    @param root_dir: the directory to scan for inning.xml files
    @return: a list of path names of all the inning.xml files
    """

    #initialize the return variable
    inning_file_list = []

    #traverse all the files in the directory
    for path, subdirs, files in walk(root_dir):
        for name in files:
            #add the inning files to the return variable
            if name.endswith('inning.xml'):
                inning_file_list.append(os.path.join(path, name))

    return inning_file_list

def get_pitches(inning_file_path):
    """
    @param inning_file_path: the pathname of the inning.xml file
    @return: a list of the pitch elements
    """
    tree = ET.ElementTree(file=inning_file_path)
    return tree.iter(tag='pitch')

#main method
if __name__ == "__main__":
    root = 'data/'
    inning_file = inning_files(root)[0]
    pitches = get_pitches(inning_file)
    for pitch in pitches:
        print pitch.attrib