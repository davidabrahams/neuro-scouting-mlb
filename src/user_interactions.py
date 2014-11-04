from data_reader import get_at_bats
from data_processor import process_at_bats
from data_visualizer import visualize_results
from time import sleep
from multiprocessing import Process
sleep_time = 1

yes_no_dict = {'Y': True, "N": False, "YES": True, "NO": False}


def interact_with_user():
    keep_running = True
    ask_for_new_directory = False
    print "-----------------------------------------------------"
    print "| End of At Bat Pitch Pattern Results Visualization |"
    print "-----------------------------------------------------"
    print ""
    print "This program will show you a results breakdown of an end-of-at-bat pitch sequence over the course of a season"
    print ""
    results_dict = process_directory()
    while keep_running:
        if ask_for_new_directory:
            if user_wants_new_directory():
                print ""
                results_dict = process_directory()
        print ""
        print "You can now visualize the results of any three pitch sequence at the end of an at bat."
        print "Key: FA=fastball, CU=curveball, SL=slider"
        print ""
        pitch1 = get_pitch("First")
        pitch2 = get_pitch("Second")
        pitch3 = get_pitch("Third")
        user_input_key = (pitch1, pitch2, pitch3)
        #process = Process(target=visualize_results, args=((user_input_key, results_dict)))
        visualize_results(user_input_key, results_dict)
        #process.start()
        print ""
        keep_running = continue_execution()
        ask_for_new_directory = True
    print "program terminated"


def process_directory():
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
    valid_inputs = ['FA', 'CU', 'SL']
    while True:
        pitch = (raw_input(pitch_number + " pitch in the three pitch sequence >> ")).upper().strip()
        if pitch in valid_inputs:
            return pitch
        else:
            print "invalid pitch abbreviation entered. Valid inputs listed in the key above"
            print ""


def continue_execution():
    while True:
        continue_program_execution = raw_input("Would you like to visualize another pitch sequence [Y/N]? >> ").upper().strip()
        if continue_program_execution in yes_no_dict:
            return yes_no_dict[continue_program_execution]
        else:
            print "invalid input entered"
            print ""


def user_wants_new_directory():
    while True:
        continue_program_execution = raw_input("Would you like to load data from a different directory [Y/N]? >> ").upper().strip()
        if continue_program_execution in yes_no_dict:
            return yes_no_dict[continue_program_execution]
        else:
            print "invalid input entered"
            print ""