from llist import LList, Node, append


def length(lst):
    """return the length of a finite linked list"""
    count = 0
    if lst.head: 
        node = lst.head
        count = 1
        while node.next:
            count += 1
            node = node.next  
    else:
        count = 0
    print (count) 

def llprint(lst):
    """print a finite linked list"""
    current = lst.head
    while current:
        print(current.data, end = " ")
        current = current.next
    print()

    print("Linked List:")
    llprint(llist)

if __name__ == "__main__":

    llist = LList()
    append(llist, Node(1))
    append(llist,Node(2))
    append(llist,Node(4))
    append(llist,Node(8))
    append(llist,Node(16))
    append(llist,Node(32))
    append(llist,Node(64))
    append(llist,Node(128))
    append(llist,Node(256))
    append(llist,Node(512))

    
    

from genfinite import lst
print("Length of linked list is", length(llist))
 


    #
    # your tests go here
    #llist = LList()
    #for numbers in [1,2,4,8,16,32,64,128,256,512]:
     #   llist.append(Node(numbers))
