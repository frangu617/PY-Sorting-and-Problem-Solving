# Write your solution for algorithm 1 below
def sort_list(lst):
    """
    Takes an unsorted numerical list as an argument and sorts it using the sort() method.
    """
    lst.sort()
    return lst

unsorted_list = [5, 10, 4, 7, 6, 2]
sort_list(unsorted_list)
print(unsorted_list)