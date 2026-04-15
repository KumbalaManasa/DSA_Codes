class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def length(head):
    count = 0
    temp = head

    while temp:
        count += 1
        temp = temp.next

    return count


# Create list: 2 → 5 → 8 → 7
head = Node(2, Node(5, Node(8, Node(7))))

print("Length:", length(head))