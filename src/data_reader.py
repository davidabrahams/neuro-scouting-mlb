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

    return at_bats


def final_three_pitches(at_bat):
    """
    @param at_bat: the at-bat to examine
    @return: a list containing the final three pitches of the at-bat, if the at bat was at least three pitches long
    """

    #get all the pitches in an at-bat sequence
    pitches = list(at_bat.iter('pitch'))

    if (len(pitches) >= 3):
        return pitches[len(pitches) - 3:]


def get_dict_entry(three_pitch_sequence):
    """
    @param three_pitch_sequence: a list object of a final three pitch sequence
    @return: a three element list of pitch_type strings
    """

    dict_entry = [None] * len(three_pitch_sequence)
    for i in range(0, len(three_pitch_sequence)):
        dict_entry[i] = three_pitch_sequence[i].get('pitch_type')
    return dict_entry