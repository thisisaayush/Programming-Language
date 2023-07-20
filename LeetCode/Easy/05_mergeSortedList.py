def mergeSortedList(list1, list2):
    dummy_list = list
    tail = dummy_list

    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        
        tail = tail.next
    
    if list1:
        tail.next = list1
    else:
        tail.next = list2
    
    return dummy_list
