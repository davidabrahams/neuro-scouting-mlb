from data_reader import get_at_bats
from data_processor import process_at_bats
from data_visualizer import visualize_results


def interact_with_user():
    print "-----------------------------------------------------"
    print "| End of At Bat Pitch Pattern Results Visualization |"
    print "-----------------------------------------------------"
    print ""
    print "This program will show you a results breakdown of a an end-of-at-bat pitch sequence over the course of a season"
    print ""
    root_folder = raw_input("What is the name of the folder containing the PITCHf/x data? >> ")
    print "parsing through directory..."
    at_bats = get_at_bats(root_folder)
    print "...parsing through directory complete."
    print str(len(at_bats)) + " at bats found."
    print ""
    print "processing obtained data..."
    results_dict = {}
    process_at_bats(at_bats, results_dict)
    print "...data processing complete."
    print ""
    print "You can now visualize the results of any three pitch sequence at the end of an at bat."
    print "Key: FA=fastball, CU=curveball, SL=slider"
    pitch1 = raw_input("First pitch in the three pitch sequence >> ")
    pitch2 = raw_input("Second pitch in the three pitch sequence >> ")
    pitch3 = raw_input("Third pitch in the three pitch sequence >> ")
    user_input_key = (pitch1, pitch2, pitch3)
    visualize_results(user_input_key, results_dict)