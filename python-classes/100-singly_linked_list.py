#!/usr/bin/python3
"""
module 100-singly_linked_list.py

This module defines a Node class to define a node and its data
It also defines a SinglyLinkedList class to define
a singly linked list by its head
"""


class Node:
    """
    Class that defines a node

    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new node 
        
        Args:
            data (int) : data of the node
            next_node (Node or None) : node after the current one
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves data of the current node
        """

        return self.__data
    
    @data.setter
    def data(self, value):
        """
        Sets the data of the current node
        """

        if not isinstance(self.__data, int):
            raise TypeError("data must be an integer")
        
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node of the current node
        """

        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node of the current node
        """

        if not isinstance(self.__next_node, None):
            if not isinstance(self.__next_node, Node):
                raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """
    Class that defines a singly linked list

    """


    def __init__(self):
        """
        Initialize a singly linked list 
        
       """

        self.__head = Node()

    def __str__(self):
        
