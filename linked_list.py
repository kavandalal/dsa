class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # get length of linked list
    def get_length(self):
        i = 0
        x = self.head
        while x != None:
            i += 1
            x = x.next
        return i

    # insert new node at the beginning
    def insert_begin(self, data):
        node = Node(data, self.head)
        self.head = node

    # insert new node at the end
    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        x = self.head
        while x.next != None:
            x = x.next
        x.next = Node(data)

    # insert new node at the index given
    def insert_at(self, at, data):
        if at < 0 or at > self.get_length():
            raise Exception('Invalid Index')
        if at == 0:
            self.head = Node(data, self.head)
            return
        if self.head == None:
            self.head = Node(data)
            return
        i = 0
        x = self.head
        while x:
            if i == at - 1:
                x.next = Node(data, x.next)
                return
            i += 1
            x = x.next

    # insert data2 after data1
    def insert_after_value(self, data1, data2):
        i = 0
        x = self.head
        while x:
            if x.data == data1:
                self.insert_at(i + 1, data2)
                return
            i += 1
            x = x.next
        print(f'Node with value == {data1} not found')

    # get the node of linked list at index given
    def get_element_at(self, at):
        if int(self.get_length()) <= int(at) or at < 0:
            raise Exception('Invalid Index')
        i = at
        x = self.head
        while i != 0:
            i -= 1
            x = x.next
        return x

    # remove the node of index given
    def remove_at(self, at):
        if at < 0 or at >= self.get_length():
            raise Exception('Invalid Index')
        if at == 0:
            self.head = self.head.next
            return

        i = 0
        x = self.head
        while x:
            if i == at - 1:
                x.next = x.next.next
                break
            i += 1
            x = x.next

    # remove the node which has the value given
    def remove_value(self, value):
        i = 0
        x = self.head
        while x:
            if x.data == value:
                self.remove_at(i)
                return
            i += 1
            x = x.next
        print(f'Element with value == {value} not found')

    # make new linked list from the list given
    def ll_from_list(self, data_list):
        self.head = None
        for i in data_list:
            self.insert_end(i)

    # reverse linked list
    def reverse_ll(self):
        prev = None
        x = self.head
        while x:
            next_ele = x.next
            x.next = prev
            prev = x
            x = next_ele
        self.head = prev

    # merge 2 sorted linked list and return new linked list head
    # it will change both the linked list as the address of all the linkedlist will be the same
    def merge_sorted_ll(h1, h2):
        a = h1
        b = h2
        new_node_start = Node()
        new_node = new_node_start
        while True:
            if a is None:
                new_node.next = b
                break
            if b is None:
                new_node.next = a
                break

            if a.data >= b.data:
                new_node.next = b
                b = b.next
            else:
                new_node.next = a
                a = a.next

            new_node = new_node.next
        return new_node_start.next

    # print the linked list from start to end

    def print_linked_list(self):
        if self.head == None:
            print('LinkedList Empty')
            return
        itr = self.head
        ans = ''
        while itr != None:
            ans += str(itr.data) + ' => '
            itr = itr.next
        print(ans)


if __name__ == "__main__":
    ll = LinkedList()
    ll2 = LinkedList()
    ll3 = LinkedList()
    # ll.insert_begin( 7) # data
    # ll.insert_end( 1) # data
    # ll.insert_at( 4 ,  69) # index , data
    # print("Linked List Length =", ll.get_length( ))  # will return length
    ll.ll_from_list(['a', 'd', 'f', 'g', 'h'])  # make linked list from list
    ll2.ll_from_list(['b', 'c', 'e', 'i', 'j'])  # make linked list from list
    # ll.print_linked_list()
    # print("Linked List Length =", ll.get_length( ))
    # print ( ll.get_element_at( 2).data ) # index to get that element
    # ll.remove_at(1 ) # index to remove from
    # ll.remove_value( 'c') # data which has to be removed
    # ll.insert_after_value( 'c' , 'x') # data1, data2 # insert data2 after data1
    # ll.reverse_ll() # reverse linked list
    # ll3.head = ll.merge_sorted_ll(ll.head, ll2.head) # merge 2 sorted linked list
    ll3.print_linked_list()


# LINKS https://www.youtube.com/watch?v=qp8u-frRAnU&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=4
