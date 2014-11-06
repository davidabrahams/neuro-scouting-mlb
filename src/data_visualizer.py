import numpy as np
import matplotlib.pyplot as plt


def visualize_results(pitch_sequence_key, sequence_results_dict):
    results = sequence_results_dict[pitch_sequence_key]  #get a dict of the results of a given pitch sequence
    result_counts = (results['Walk'], results['Strikeout'], results['Hit'], results['Hit (out)'], results['Other']) #load the values of the results

    #plot the values
    n_groups = len(results)
    index = np.arange(n_groups)
    bar_width = 0.8
    rects1 = plt.bar(index, result_counts, bar_width, color='rybgk')

    #set the labels
    plt.xlabel('At bat result', fontsize=16)
    plt.ylabel('Number of occurrences', fontsize=16)
    plt.title('At bat results for pitch sequences\nending in ' + pitch_sequence_key[0] + ', ' + pitch_sequence_key[1] + ', ' + pitch_sequence_key[2], fontsize=20)
    plt.xticks(index + bar_width / 2, ('Walk', 'Strikeout', 'Hit', 'Hit (out)', 'Other'))
    plt.show()