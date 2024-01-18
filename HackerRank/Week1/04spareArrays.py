def matchingStrings(strings, queries):
    # Create a dictionary to store the counts of each string in strings
    countStrs = {}
    
    # Count occurrences of each string in strings
    for x in strings:
        countStrs[x] = countStrs.get(x, 0) + 1
    
    # Initialize a list to store the results for each query
    results = []
    
    # Count occurrences of each query in strings and append to the results list
    for query in queries:
        results.append(countStrs.get(query, 0))
    
    return results
