'''Remove Duplicates for unsorted array.'''

def removeDuplicates(arr):
    unique_Element = []
    seen = set()

    for n in arr:
        if n not in seen:
            unique_Element.append(n)
            seen.add(n)

    return unique_Element

print(removeDuplicates([1,7,6,7,2,5]))