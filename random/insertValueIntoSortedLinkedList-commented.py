class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def insert_value_into_sorted_linked_list(head, value):
    """Given the head of a sorted linked list and a value, insert a new
node into the list at the sorted position.

    """
    # Create the node we will be inserting
    new_node = ListNode(value)

    # Check if they gave us an empty list. If they did, return our new
    # node. Every newly created Node is a 1 element list
    if head == None:
        return new_node

    # Check if our new node has a lower value than the first node. If
    # it does, point our node at the head, and return our node. Every
    # node is also a list, by pointing our node at the head of the
    # original list, we make our node a new list, identical to the
    # original except with our new node as the head.
    if value < head.value:
        newNode.next = head
        return newNode

    # find the node our new node is to be inserted after by using a
    # linear search. When the search is complete, the variable `node`
    # will hold the node we need to insert our new node after
    node = head
    while node.next != None: # stop when we have searched the whole list
        # or when we find a node with a lower value than our node
        if value < node.next.value:
            break
        # advance search to the next node
        node = node.next

    # Insert our new node after the node we found. That means we point
    # our new node at the found node's next node, then we point the
    # found node at our node.  point our new node to the found node's
    newNode.next = node.next
    node.next = newNode

    return head
