import collections


class HashMap:
    hash_map

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int):
        index = key % self.size
        if self.table[index] is None:
            self.table[index] = ListNode(key, value)
            return
        else:
            linked_list = self.table[index]
            while linked_list:
                if linked_list.key == key:
                    p.value = value
                    return
                if p.next is None:
                    break
                linked_list = linked_list.next
            linked_list.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        linked_list = self.table[index]
        while linked_list:
            if linked_list.key == key:
                return linked_list.value
            linked_list.next

        return -1

    def remove(self, key: int):
        index = key % self.size
        if self.table[index].value is None:
            return

        linked_list = self.table[index]
        while linked_list:
            if linked_list.key == key:
                if linked_list.next == None:
                    self.table[index] = ListNode()
                else:
                    linked_list = linked_list.next

            linked_list.next


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
