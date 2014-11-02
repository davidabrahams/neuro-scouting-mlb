from data_reader import get_at_bats, final_three_pitches, get_dict_key, process_at_bat

#main method
if __name__ == "__main__":
    root = 'data'
    results = {}
    at_bats = get_at_bats(root)
    print "processing at bats based on final three pitches..."
    for at_bat in at_bats:
        process_at_bat(at_bat, results)
    print results