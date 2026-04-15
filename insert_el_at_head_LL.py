class Node:
    def __init__(self,data,next=None):
        self.data= data
        self.next = next
def insertion_at_head(head,val):
    new_node = Node(6)
    new_node.next=head
    return new_node
# Helper function to print list
def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")
# Example usage
head = Node(2)
head.next = Node(5)
head.next.next = Node(8)

print("Before:")
print_list(head)

# Insert at head
head = insertion_at_head(head, 1)

print("After:")
print_list(head)    
