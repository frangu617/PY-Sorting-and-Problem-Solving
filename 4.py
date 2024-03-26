#Write an algorithm that takes in a string and sorts the words in the string in alphabetical order. The comparison should be case-insensitive.

# Sample input: 'I love software engineering'
# Sample output: ['engineering', 'I', 'love', 'software']
# Note that a key parameter will need to be used here in order for the sorting to be case-insensitive (sort in alphabetical order regardless of whether string is uppercase or lowercase).

def sort_words_alphabetically(string):
    # Split the string into words
    words = string.split()
    
    # Sort the words in alphabetical order (case-insensitive)
    sorted_words = sorted(words, key=lambda word: word.lower())
    
    return sorted_words

# Sample input
input_string = 'I love software engineering'

# Sort the words alphabetically
sorted_words = sort_words_alphabetically(input_string)

# Print the sorted words
print(sorted_words)
