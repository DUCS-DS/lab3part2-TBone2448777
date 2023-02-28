from llist import *
from gencyclic import lst

def llprint(lst, num):
    """print the first num terms of linked list lst"""
    i = 0
    if lst.head:
        node = lst.head
        while node.next and i <= num:
            print(node.val, end=", ")
            node = node.next
            i += 1
        print(node.val)

def find_cycle(lst):
    """return the start index and length of the cycle"""
    tortoise = lst.head
    hare = lst.head.next.next
    i = 0
    while tortoise is not hare:
        tortoise = tortoise.next
        hare = hare.next.next
        i += 1
    saved = tortoise
    tortoise = tortoise.next
    j = 0
    while saved is not tortoise:
        tortoise = tortoise.next
        j += 1
    return i, j

if __name__ == "__main__":
    start, length = find_cycle(lst)
    print("The cycle begins at node " + str(start) + ".")
    print("The cycle is " + str(length) + " items long.")
