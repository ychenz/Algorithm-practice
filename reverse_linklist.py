class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Linkedlist:
    def __init__(self, head):
        self.head = head

    def reverse(self, N):
        if N.next is None:
            self.head = N
            return
        else:
            self.reverse(N.next)
            N.next.next = N
            N.next = None


if __name__ == '__main__':
    head = Node(0, Node(1, Node(2, Node(3, None))))
    linkedlist = Linkedlist(head)

    node = head
    vals = []
    while node is not None:
        vals.append(node.val)
        node = node.next

    print(vals)

    linkedlist.reverse(head)
    vals = []
    node = linkedlist.head
    while node is not None:
        vals.append(node.val)
        node = node.next

    print(vals)
