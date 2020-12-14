class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def insert_value_into_sorted_linked_list(head, value):
    new_node = ListNode(value)

    if head == None:
        return new_node

    if value < head.value:
        newNode.next = head
        return newNode

    node = head
    while node.next != None:
        if value < node.next.value:
            break
        node = node.next

    newNode.next = node.next
    node.next = newNode

    return head
