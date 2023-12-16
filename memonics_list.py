import random

# sampling with replacement
original_list = [20, 30, 40, 50, 60, 70, 80]

# k = number of items to select
sample_list = random.choices(original_list, k=64)
print(sample_list)

# Output [60, 20, 60]