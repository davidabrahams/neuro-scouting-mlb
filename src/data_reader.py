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

    #return the final three pitches
    if len(pitches) >= 3:
        return pitches[len(pitches) - 3:]


def get_dict_key(three_pitch_sequence):
    """
    @param three_pitch_sequence: a list object of a final three pitch sequence
    @return: a three element list of pitch_type strings
    """

    #initialize the return variable
    dict_entry = [None] * len(three_pitch_sequence)

    #loop over the three pitch sequence
    for i in range(0, len(three_pitch_sequence)):
        pitch_type = three_pitch_sequence[i].get('pitch_type') #extract the pitch type
        processed_type = process_pitch_type(pitch_type) #convert it to either 'FA', 'CU', 'SL', or leave it
        dict_entry[i] = processed_type #place the converted pitch type in the return variable

    return dict_entry


def process_pitch_type(pitch_type):
    """
    @param pitch_type: the pitch type to convert
    converts the pitch type to 'FA' for fastball, 'CU' for curveball, or 'SL' for slider, or leaves it the same
    """

    fastballs = ['FT', 'FF', 'FA', 'FS']
    curveballs = ['CU', 'CB']
    sliders = ['SL']

    if pitch_type in fastballs:
        return 'FA'
    elif pitch_type in curveballs:
        return 'CU'
    elif pitch_type in sliders:
        return 'SL'
    else:
        print 'pitch_type: ' + pitch_type + ", not grouped."
        return pitch_type


def get_at_bat_result(at_bat):
    """
    extracts the result from at_bat and groups it into 'Hit', 'Hit (out)', 'Strikeout' or 'Walk'
    @param at_bat: the at_bat to extract a result from
    @return: the grouped result
    """
    #extract the at_bat result
    at_bat_result = at_bat.get('event')

    #declare the groups
    hits = ['Single', 'Double', 'Triple', 'Home Run']
    hits_out = ['Groundout', 'Flyout', 'Lineout']
    strikeout = ['Strikeout']
    walk = ['Walk']

    #return the correct result
    if at_bat_result in hits:
        return 'Hit'
    elif at_bat_result in hits_out:
        return 'Hit (out)'
    elif at_bat_result in strikeout:
        return 'Strikeout'
    elif at_bat_result in walk:
        return 'Walk'
    else:
        print "An error occurred when processing the at bat result: ", at_bat_result


def process_at_bat(at_bat, sequence_results_dict):
    """
    @param at_bat: the at-bat to add into the sequence results dictionary
    @param sequence_results_dict: a dict mapping from the final three pitch sequence of an at-bat to the results breakdown of that sequence
    """

    final_pitches = final_three_pitches(at_bat) #extract the final pitch sequence
    at_bat_result = get_at_bat_result(at_bat) #extract the result from the at_bat

    #check to make sure there was a final three pitch sequence
    if final_pitches is not None:

        #get the dictionary key that corresponds to the three pitch sequence
        at_bat_key = get_dict_key(final_pitches)


        print type(sequence_results_dict)
        #if there is not a key corresponding to the final pitch sequence of this at bat, add the key to the dictionary
        if at_bat_key not in sequence_results_dict:
            sequence_results_dict[at_bat_key] = {'Hit': 0, 'Hit (out)': 0, 'Strikeout': 0, 'Walk': 0}

        results_breakdown_dict = sequence_results_dict[at_bat_key] #get the dictionary that hold the results counts for that particular pitch sequence
        results_breakdown_dict[at_bat_result] += 1 #increase the count for that particular result by one

