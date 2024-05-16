class Node:
    def __init__(self, data=None):
        self.data = data        
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list
     

    def sorted_insert(self, head_ref, new_node):
        if head_ref is None or head_ref.data >= new_node.data:
            new_node.next = head_ref
            head_ref = new_node
        else:
            current = head_ref
            while current.next is not None and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return head_ref

    def merge_sorted(self, second_list):
        merged = LinkedList()
        current_first = self.head
        current_second = second_list.head

        if not current_first:
            merged.head = current_second
            return merged
        if not current_second:
            merged.head = current_first
            return merged

        if current_first and current_second:
            if current_first.data <= current_second.data:
                new_list = current_first
                current_first = new_list.next
            else:
                new_list = current_second
                current_second = new_list.next
            merged.head = new_list

        while current_first and current_second:
            if current_first.data <= current_second.data:
                new_list.next = current_first
                new_list = current_first
                current_first = new_list.next
            else:
                new_list.next = current_second
                new_list = current_second
                current_second = new_list.next

        if not current_first:
            new_list.next = current_second
        if not current_second:
            new_list.next = current_first

        return merged

llist1 = LinkedList()
llist1.insert_at_end(1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)

print("Список №1:")
llist1.print_list()

print("Список №2:")
llist2.print_list()

merged_list = llist1.merge_sorted(llist2)
print("Об'єднаний відсортований список:")
merged_list.print_list()

merged_list.reverse()
print("Реверсований список:")
merged_list.print_list()
