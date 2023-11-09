def is_subset(set1, set2):
    return set1.issubset(set2)

set1 = {1, 2}
set2 = {1, 2, 3, 4}
is_subset_result = is_subset(set1, set2)
print(is_subset_result)
