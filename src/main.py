from data_reader import get_at_bats, final_three_pitches, get_dict_entry

#main method
if __name__ == "__main__":
    root = 'data_test/'
    at_bats = get_at_bats(root)
    three = final_three_pitches(at_bats[0])
    for pitch in three:
        print pitch.attrib
    print get_dict_entry(three)