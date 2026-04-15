class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def delete_head(head):
    if head is None:
        return None
    return head.next


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


# Create list: 2 → 5 → 8 → 7
head = Node(2, Node(5, Node(8, Node(7))))

print("Before:")
print_list(head)

head = delete_head(head)

print("After:")
print_list(head)