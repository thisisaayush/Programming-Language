def total_fruit(tree):
    fruit_count = {}
    start = 0
    max_fruits = 0

    for end in range(len(tree)):
        fruit_count[tree[end]] = fruit_count.get(tree[end], 0) + 1

        while len(fruit_count) > 2:
            fruit_count[tree[start]] -= 1
            if fruit_count[tree[start]] == 0:
                del fruit_count[tree[start]]
            start += 1

        max_fruits = max(max_fruits, end - start + 1)

    return max_fruits

# Example usage:
tree = [1, 2, 1, 2, 1, 3, 1, 7, 8, 2]
print(total_fruit(tree))
# Output: 4
