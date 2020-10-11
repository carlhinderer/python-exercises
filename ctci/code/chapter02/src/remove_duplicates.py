#
# 2.1 Remove Dups: 
#
# Write code to remove duplicates from an unsorted linked list. 
#
# FOLLOW UP How would you solve this problem if a temporary buffer is not allowed?
#

def remove_dups(linked_list):
    elements = []
    current = linked_list.head
    elements.append(current.data)
    while current.next:
        if current.next.data in elements:
            current.next = current.next.next
        else:
            elements.append(current.next.data)
        current = current.next
    return linked_list


def remove_dups_no_buffer(linked_list):
    pass