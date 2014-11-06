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
    @return: a three element tuple of pitch_type strings
    """

    #initialize the return variable
    dict_entry = [None] * len(three_pitch_sequence)

    #loop over the three pitch sequence
    for i in range(0, len(three_pitch_sequence)):
        pitch_type = three_pitch_sequence[i].get('pitch_type') #extract the pitch type
        processed_type = process_pitch_type(pitch_type) #convert it to either 'FA', 'CU', 'SL', 'CH', or None
        dict_entry[i] = processed_type #place the converted pitch type in the return variable


    return tuple(dict_entry)


def process_pitch_type(pitch_type):
    """
    @param pitch_type: the pitch type to convert
    converts the pitch type to 'FA' for fastball, 'CU' for curveball, or 'SL' for slider, or None if it is none of those three
    """

    fastballs = ['FT', 'FF', 'FA', 'FS']
    curveballs = ['CU', 'CB', 'KC']
    sliders = ['SL']
    changeups = ['CH']

    if pitch_type in fastballs:
        return 'FA'
    elif pitch_type in curveballs:
        return 'CU'
    elif pitch_type in sliders:
        return 'SL'
    elif pitch_type in changeups:
        return 'CH'
    else:
        return None


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
    hits_out = ['Groundout', 'Flyout', 'Lineout', 'Pop Out', 'Grounded Into DP', 'Double Play', 'Bunt Groundout', 'Bunt Pop Out', 'Triple Play', 'Bunt Lineout']
    strikeout = ['Strikeout', 'Strikeout - DP']
    walk = ['Walk']
    others = ['Forceout', 'Fielders Choice Out', 'Field Error', 'Intent Walk', 'Hit By Pitch', 'Sac Fly', 'Sac Bunt', 'Fan interference', 'Runner Out', 'Fielders Choice', 'Batter Interference', 'Catcher Interference', 'Sac Fly DP', 'Sacrifice Bunt DP']

    #return the correct result
    if at_bat_result in hits:
        return 'Hit'
    elif at_bat_result in hits_out:
        return 'Hit (out)'
    elif at_bat_result in strikeout:
        return 'Strikeout'
    elif at_bat_result in walk:
        return 'Walk'
    elif at_bat_result in others:
        return 'Other'
    else:
        print "An error occurred when processing the at bat result: ", at_bat_result


def process_at_bats(at_bats, sequence_results_dict):
    """
    @param at_bats: a list of at-bats to add into the sequence results dictionary
    @param sequence_results_dict: a dict mapping from the final three pitch sequence of an at-bat to the results breakdown of that sequence
    """

    for at_bat in at_bats:

        final_pitches = final_three_pitches(at_bat) #extract the final pitch sequence
        at_bat_result = get_at_bat_result(at_bat) #extract the result from the at_bat

        #check to make sure there was a final three pitch sequence
        if final_pitches is not None:

            #get the dictionary key that corresponds to the three pitch sequence
            at_bat_key = get_dict_key(final_pitches)

            #only process at_bats where the final pitch sequence contained fastballs, curveballs, changeups, and sliders
            if None not in at_bat_key:

                #if there is no key in the dict corresponding to this at_bat, make a new key
                if at_bat_key not in sequence_results_dict:
                    sequence_results_dict[at_bat_key] = {'Hit': 0, 'Hit (out)': 0, 'Strikeout': 0, 'Walk': 0, 'Other': 0}

                results_breakdown_dict = sequence_results_dict[at_bat_key] # get the dictionary that hold the results counts for that particular pitch sequence

                #If the result was either a Hit, Hit (out), Strikeout, or Walk, increment the count for that result
                if at_bat_result is not None:
                    results_breakdown_dict[at_bat_result] += 1

