neuro-scouting-mlb
==================

-Author: David Abrahams, 11/5/2014

- How to Run -
Using a Python interpreter run executable.py from the src directory. Place your data files in a separate directory adjacent to src.

- Python package dependencies -
numpy
matplotlib

- How the script works -
1. The user enters the directory where the inning.xml files are located.
2. The script parses through each file ending in 'inning.xml'
3. The script stores every 'at_bat' element in a list
4. The script builds a dictionary that maps from pitch-sequence to a list of result counts by doing the following:
4a. Extract the final three pitches of an at bat.
4b. Check if the dictionary has a key for that specific three pitch series.
4c. If it does, increment the correct result count. Example (at bat strikeout ending in FA, FA, CU):

    sequence_results_dict[(FA, FA, CU)] = {'Hit': 14, 'Hit (out)': 29, 'Strikeout': 10, 'Walk': 3, 'Other': 1}
    {'Hit': 14, 'Hit (out)': 29, 'Strikeout': 10, 'Walk': 3, 'Other': 1} ==> {'Hit': 14, 'Hit (out)': 29, 'Strikeout': 11, 'Walk': 3, 'Other': 1}

4d. If it doesn't, create a new key-value pair in the dictionary and increment the correct value. Example:

    sequence_results_dict[(FA, FA, CU)] = {'Hit': 0, 'Hit (out)': 0, 'Strikeout': 1, 'Walk': 0, 'Other': 0}

5. The user enters a three pitch sequence, and using that sequence as a key, the script finds the result counts for that sequence. Example:

    sequence_results_dict[(FA, FA, CU)] = {'Hit': 14, 'Hit (out)': 29, 'Strikeout': 11, 'Walk': 3, 'Other': 1}

6. The script displays the result counts in a bar graph.

- Code organization -
