# Write your solution for algorithm 3 below
def descending_sorted_list(lst):
    """
    Takes an unsorted numerical list as an argument and creates a new sorted list in descending order using the sorted() function.
    """
    return sorted(lst, reverse=True)

unsorted_list = [5, 10, 4, 7, 6, 2]
sorted_descending = descending_sorted_list(unsorted_list)
print(sorted_descending)