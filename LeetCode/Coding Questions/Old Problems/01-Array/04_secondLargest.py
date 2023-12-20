def secondLargest(arr):
    max1 = 0
    max2 = 0

    for n in arr:
        if n > max1:
            max2 = max1  # updating max2 to max1 as max1 has a new max now.
            max1 = n

        elif n < max1 and n > max2:  # max1 = 5, n = 4, max2 was 3, then max2 now will be 4.
            max2 = n

    return max2


print(secondLargest([5, 6, 9, 1, 3]))