class Node:
    def __init__(self,data):
        self.data= data
        self.next = next
def main():
    arr = [1,2,3,4,5]
     # Create first node
    node1 = Node(arr[0])
    node2 = Node(arr[1])
    node3 = Node(arr[2])
    node4 = Node(arr[3])
    node5 = Node(arr[4])
    
    # Print memory location of node
    print(node1)
    ## Print data stored in node
    print(node1.data)
    
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None
    print(node3.next.data)
    
main()