#!/usr/bin/python3
"""Linked lists with Python"""


class Node:
    """Blueprint for Node of a linked list
    Attributes:
        data (int): number field of node
        next_node (Node): next node - instance of a Node
            class or None
    """
    def __init__(self, data, next_node=None):
        """Initializes a Node
        Args:
            data (int): number field of node
            next_node (Node): next node - instance of a Node
                class or None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets or set the data attribute of a Node instance"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get or set the next_node attribute of a Node instance"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Blueprint for a SinglyLinkedList
    Attributes:
        head (Node): head node of linked list
    """
    def __init__(self):
        """Initializes a SinglyLinkedList"""
        self.__head = None

    def __str__(self):
        """String representation of list"""
        data = []
        current = self.__head
        while current is not None:
            data.append(str(current.data))
            current = current.next_node
        return "\n".join(data)

    def sorted_insert(self, value):
        """Inserts a new node into the correct position (increasing order)
        Args:
            value (int): number field of new node
        """
        current = self.__head
        new_node = Node(value)
        if current is None:
            self.__head = new_node
        elif current.data > value:
            new_node.next_node = current
            self.__head = new_node
        else:
            while current.next_node is not None:
                if current.next_node.data > value:
                    new_node.next_node = current.next_node
                    current.next_node = new_node
                    break
                current = current.next_node
            else:
                current.next_node = new_node
