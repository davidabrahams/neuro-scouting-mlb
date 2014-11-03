import numpy as np
import matplotlib.pyplot as plt


def visualize_results(pitch_sequence_key, sequence_results_dict):
    results = sequence_results_dict[pitch_sequence_key]
    n_groups = len(results)
    result_counts = (results['Walk'], results['Strikeout'], results['Hit'], results['Hit (out)'])
    index = np.arange(n_groups)
    bar_width = 0.8

    rects1 = plt.bar(index, result_counts, bar_width)
    plt.xlabel('At bat result')
    plt.ylabel('Number of occurrences')
    plt.title('At bat result for pitch sequences ending in ' + pitch_sequence_key[0] + ' ' + pitch_sequence_key[1] + ' ' + pitch_sequence_key[2])
    plt.xticks(index + bar_width / 2, ('Walk', 'Strikeout', 'Hit', 'Hit (out)'))
    plt.show()