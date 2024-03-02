from llist import LList, Node, append


def length(lst):
    """return the length of a finite linked list"""
    count = 0 
    current = lst.head
    while current:
        count += 1
        current = current.next
    return count


def llprint(lst):
    """print a finite linked list"""
    current = lst.head
    while current:
        print(current.value, end=" ")
        current = current.next
    print()


if __name__ == "__main__":
   
    values = [1,2,4,8,16,32,64,128,256,512]
    lst = LList()
    for value in values:
        append(lst, Node(value))

    print(length(lst))

    llprint(lst)

 


    #
    # your tests go here
    #llist = LList()
    #for numbers in [1,2,4,8,16,32,64,128,256,512]:
     #   llist.append(Node(numbers))
