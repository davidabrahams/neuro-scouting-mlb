from data_reader import get_at_bats
from data_processor import process_at_bats
from data_visualizer import visualize_results
from time import sleep
sleep_time = 1

yes_no_dict = {'Y': True, "N": False, "YES": True, "NO": False}


def interact_with_user():
    """
    this function allows the user to input the location of data files, and what pitches they would like to visualize.
    """

    keep_running = True  # set this flag to true so the program runs at least once
    ask_for_new_directory = False  # set this flag to false because the program will prompt the user to enter a directory by default, it should not prompt them again

    print "-----------------------------------------------------"
    print "| End of At Bat Pitch Pattern Results Visualization |"
    print "-----------------------------------------------------"
    print ""
    print "This program will show you a results breakdown of an end-of-at-bat pitch sequence over the course of a season"
    print ""

    results_dict = process_directory()  # ask the user where the data files are

    while keep_running:  # this loop allows the user to visualize multiple sets of data

        if ask_for_new_directory: # check if we should prompt the user for a new directory
            if user_wants_new_directory():  # prompt the user for a new directory
                print ""
                results_dict = process_directory()  # process the data from the inputted directory

        print ""
        user_input_key = get_three_pitches()  # prompt the user to enter a three pitch sequence
        print ""

        print "...opening graphic. To continue program execution close the graphic."
        visualize_results(user_input_key, results_dict)  # display a graphic for the results of the three pitch sequence
        print ""

        keep_running = continue_execution()  # after closing the graphic, ask the user if they would like to visualize another set of data
        ask_for_new_directory = True

    print "...program terminated."


def process_directory():
    """
    prompts the user to enter a directory name and then parses through and stores the data in that directory
    """
    root_folder = raw_input("What is the name of the folder containing the PITCHf/x data? >> ")
    print "parsing through directory..."
    at_bats = get_at_bats(root_folder)
    print "...parsing through directory complete."
    print str(len(at_bats)) + " at bats found."
    sleep(sleep_time)
    print ""
    print "processing obtained data..."
    results_dict = {}
    process_at_bats(at_bats, results_dict)
    print "...data processing complete."
    return results_dict


def get_pitch(pitch_number):
    """
    @param pitch_number: The number pitch in the sequence currently being entered ('First', 'Second', or 'Third')
    @return: A pitch abbreviation entered by the user ('FA', 'CU', or 'SL')
    """
    valid_inputs = ['FA', 'CU', 'SL', 'CH']
    while True:
        pitch = (raw_input(pitch_number + " pitch in the three pitch sequence >> ")).upper().strip()
        if pitch in valid_inputs:
            return pitch
        else:
            print "invalid pitch abbreviation entered. Valid inputs listed in the key above"
            print ""


def continue_execution():
    """
    asks the user if they would like to visualize another pitch sequence
    @return: a boolean of the user's response
    """
    while True:
        continue_program_execution = raw_input("Would you like to visualize another pitch sequence [Y/N]? >> ").upper().strip()
        if continue_program_execution in yes_no_dict:
            return yes_no_dict[continue_program_execution]
        else:
            print "invalid input entered"
            print ""


def user_wants_new_directory():
    """
    asks the user if they would like to load data from a different directory
    @return: a boolean of the user's response
    """
    while True:
        continue_program_execution = raw_input("Would you like to load data from a different directory [Y/N]? >> ").upper().strip()
        if continue_program_execution in yes_no_dict:
            return yes_no_dict[continue_program_execution]
        else:
            print "invalid input entered"
            print ""


def get_three_pitches():
    """
    allows the user to enter a three pitch sequence
    @return: a tuple of the three pitch sequence entered (ex: ('FA', 'FA', 'CU'))
    """
    print "You can now visualize the results of any three pitch sequence at the end of an at bat."
    print "Key: FA=fastball, CU=curveball, SL=slider, CH=changeup"
    print ""
    pitch1 = get_pitch("First")
    pitch2 = get_pitch("Second")
    pitch3 = get_pitch("Third")
    user_input_key = (pitch1, pitch2, pitch3)
    return user_input_key