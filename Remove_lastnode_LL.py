class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Function to delete last node
def delete_last(head):
    # Case 1: empty list
    if head is None:
        return None

    # Case 2: only one node
    if head.next is None:
        return None

    # Traverse to second last node
    temp = head
    while temp.next.next:
        temp = temp.next

    # Remove last node
    temp.next = None

    return head


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
head.next.next.next = Node(7)

print("Before:")
print_list(head)

head = delete_last(head)

print("After:")
print_list(head)