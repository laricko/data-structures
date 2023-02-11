from typing import Any, List, Self


class Node:
    def __init__(self, val: Any, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head: Node) -> None:
        self.head: Node = head

    def __str__(self) -> str:
        return str(self.to_list())

    def add_value(self, value: Any) -> None:
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(value)

    def search_value(self, value: Any) -> int | None:
        cur = self.head
        index = 0
        while True:
            if cur.val == value:
                return index
            if not cur.next:
                break
            cur = cur.next
            index += 1

    def has_value(self, value: Any) -> bool:
        cur = self.head
        while True:
            if cur.val == value:
                return True
            if not cur.next:
                return False
            cur = cur.next

    def get_value_by_index(self, index: int) -> Any | None:
        cur = self.head
        temp_index = 0
        while True:
            if index == temp_index:
                return cur.val
            if not cur.next or temp_index > index:
                return
            temp_index += 1
            cur = cur.next

    def remove_item_by_index(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return
        cur = self.head
        temp_index = 0
        while cur and cur.next:
            if temp_index == index - 1:
                cur.next = cur.next.next
            temp_index += 1
            cur = cur.next

    def delete_value(self, value: Any) -> None:
        if value == self.head.val:
            self.head = self.head.next
            return
        cur = self.head
        while cur and cur.next:
            if cur.next.val == value:
                cur.next = cur.next.next
            cur = cur.next

    def delete_dublicates(self) -> None:
        cur = self.head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

    def buble_sort(self) -> None:
        if self.head is None:
            return
        end = None
        while end != self.head:
            cur = self.head
            while cur.next != end:
                if cur.val > cur.next.val:
                    cur.val, cur.next.val = cur.next.val, cur.val
                cur = cur.next
            end = cur

    def insertion_sort(self) -> None:
        if self.head is None:
            return
        sorted_list = None
        cur = self.head
        while cur:
            next_node = cur.next
            sorted_list = self._insert_in_order(sorted_list, cur)
            cur = next_node
        self.head = sorted_list

    def _insert_in_order(self, sorted_list: Node, node: Node) -> Node:
        if sorted_list is None or sorted_list.val >= node.val:
            node.next = sorted_list
            sorted_list = node
        else:
            cur = sorted_list
            while cur.next and cur.next.val < node.val:
                cur = cur.next
            node.next = cur.next
            cur.next = node
        return sorted_list

    def merge_sort(self) -> None:
        self.head = self._merge_sort_recursive(self.head)

    def _merge_sort_recursive(self, head: Node) -> Node:
        if head is None or head.next is None:
            return head
        middle_node = self._get_middle_node(head)
        next_of_middle = middle_node.next
        middle_node.next = None
        left_side = self._merge_sort_recursive(head)
        right_side = self._merge_sort_recursive(next_of_middle)
        sorted_list = self._merge(left_side, right_side)
        return sorted_list

    def _get_middle_node(self, head: Node) -> Node:
        slow_pointer = head
        fast_pointer = head
        while fast_pointer.next is not None and fast_pointer.next.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer

    def _merge(self, left_side: Node, right_side: Node) -> Node:
        dummy_node = Node(0)
        cur = dummy_node
        while left_side is not None and right_side is not None:
            if left_side.val < right_side.val:
                cur.next = left_side
                left_side = left_side.next
            else:
                cur.next = right_side
                right_side = right_side.next
            cur = cur.next
        if left_side is not None:
            cur.next = left_side
        else:
            cur.next = right_side
        return dummy_node.next

    def to_list(self) -> List:
        result = []
        cur = self.head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result

    @classmethod
    def list_to_linked_list(cls, l: List) -> Self:
        li = None
        l.reverse()
        for element in l:
            list_node = Node(element, li)
            li = list_node
        return cls(li)
