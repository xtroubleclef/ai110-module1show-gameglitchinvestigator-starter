# Problem 1
# Step 1: Understand
    # We want to return candidate's name along with vote count if candidate is in the votes dictionary. 
    # If candidate is not in the votes dictionary, we want to update the dictionary to include the candidate 
    # with a vote count of 1.
# Step 2: Plan
    # Create an empty dictionary

# Step 3: Implement
# def cast_vote(votes, candidate):
#     count_votes = {}
#     if candidate in votes:
#         votes[candidate] += 1
#     else:
#         votes[candidate] = 1


# # Test cases
# votes = {"Alice": 5, "Bob": 3}
# cast_vote(votes, "Alice")
# print(votes)
# cast_vote(votes, "Gina")
# print(votes)

# Example output:
# {'Alice': 6, 'Bob': 3}
# {'Alice': 6, 'Bob': 3, 'Gina': 1}


# Problem 2
# Step 1: Understand
# We want to return a list of keys that are common between two dictionaries.
# Step 2: Plan

# def common_keys(dict1, dict2):
#     common_list = []
#     for key in dict1:
#         if key in dict2:
#             common_list.append(key)
#     return common_list
            



# # Test cases
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
# common_list = common_keys(dict1, dict2)
# print(common_list)

# Problem 3
# def count_occurrences(nums):
#     counter = {}
#     for n in nums:
#         if n in counter:
#             counter[n] += 1
#         else:
#             counter[n] = 1
#     return counter
# nums = [1, 2, 2, 3, 3, 3, 4]
# print(count_occurrences(nums))

# Problem 4

def get_highest_priority_task(tasks):
    for key in sorted(tasks):
        priority = tasks.pop(key)
        return priority


tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)