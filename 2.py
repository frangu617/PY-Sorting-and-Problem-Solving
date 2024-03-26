# Write your solution for algorithm 2 below
def sort_list(lst):
    """
    Takes an unsorted numerical list as an argument and creates a new sorted list using the sorted() function.
    """
    return sorted(lst)

unsorted_list = [5, 10, 4, 7, 6, 2]
sorted_list = sort_list(unsorted_list)
print(sorted_list)