from collections import defaultdict

# Create a defaultdict with a default value of an empty list
my_dict = defaultdict(list)

# Add elements to the defaultdict
my_dict['fruits'].append('apple')
my_dict['vegetables'].append('carrot')

# Print the defaultdict
print(my_dict)