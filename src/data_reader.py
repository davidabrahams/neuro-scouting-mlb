import os

#import the C implementation of ElementTree for speed
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


def get_at_bats(root_dir):
    """
    @param root_dir: the directory to scan for inning.xml files
    @return: a list containing all at-bat elements in the inning.xml files in the folder
    """

    #initialize the return variable
    at_bats = []

    #move up one directory to enter the data directory
    cwd = os.getcwd()
    os.chdir(os.path.pardir)

    print "parsing through root directory..."

    #traverse all the files and subdirectories in the directory
    for path, subdirs, files in os.walk(root_dir):

        #only look at files
        for name in files:

            #only look in the inning files
            if name.endswith('inning.xml'):

                inning_file_path = os.path.join(path, name)

                #if we are able to parse an inning file, iterate over it adding all at-bats to the return variable
                try:
                    inning_file_root = ET.ElementTree(file=inning_file_path).getroot()
                    at_bat_iterator = inning_file_root.iter('atbat')
                    for at_bat in at_bat_iterator:
                        at_bats.append(at_bat)

                except ET.ParseError:
                    print "An error occurred when parsing " + inning_file_path

    #change back to the original working directory
    os.chdir(cwd)

    print str(len(at_bats)) + " at_bats found."

    return at_bats