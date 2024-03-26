def find_all_pairs_with_sum(nums, target):
    # Create a dictionary to store each number and its corresponding index
    num_index_map = {}
    pairs = []

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target sum
        complement = target - num

        # If the complement exists in the dictionary, a pair is found
        if complement in num_index_map:
            # Add the pair to the list of pairs
            pairs.append([complement, num])

        # Store the current number and its index in the dictionary
        num_index_map[num] = i

    # If no pairs are found, return a message
    if not pairs:
        return 'no pairs sum to the target'
    else:
        return pairs

# Example usage
nums = [5, 10, 4, 7, 6, 2]
target = 9
result = find_all_pairs_with_sum(nums, target)
print(result)
