# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_linked_list

import unittest
import time
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        Test 1: An LinkedList exists.
        """
        try:
            LinkedList()
        except NameError:
            self.fail("Could not instantiate LinkedList.")

    def test_no_initial_value(self):
        """
        Test 2: A list instantiated without a value has a head with a value of None.
        """
        ll = LinkedList()
        self.assertEqual(None, ll.value)

    def test_initial_value(self):
        """
        Test 3: A list/node instantiated with a value retains that value.
        """
        value = fake_value()
        ll = LinkedList(value)
        self.assertEqual(value, ll.value)

    def test_next(self):
        """
        Test 4: A node's `next` attribute initially refers to itself.
        """
        ll = LinkedList()
        self.assertEqual(ll, ll.next)

    def test_previous(self):
        """
        Test 5: A node's `previous` attribute initially refers to itself.
        """
        ll = LinkedList()
        self.assertEqual(ll, ll.previous)

    # """
    # Sentinel Node
    # """

    def test_sentinel_node(self):
        """
        Test 6: A list node with a value of `None` is a sentinel node.
        (See https://en.wikipedia.org/wiki/Sentinel_node)
        """
        ll = LinkedList()
        self.assertTrue(ll.is_sentinel())

    def test_not_sentinel_node(self):
        """
        Test 7: A list node with a value is not a sentinel node.
        """
        ll = LinkedList(fake_value())
        self.assertFalse(ll.is_sentinel())

    # """
    # Empty List
    # """

    def test_empty(self):
        """
        Test 8: A list is initially empty.
        """
        ll = LinkedList()
        self.assertTrue(ll.is_empty())

    def test_not_empty(self):
        """
        Test 9: A list node with a previous or next refering to anything other than itself
        is not empty.
        """
        ll = LinkedList()
        ll.next = fake_value()
        self.assertFalse(ll.is_empty())
        ll.previous = fake_value()
        self.assertFalse(ll.is_empty())
        ll.next = ll
        self.assertFalse(ll.is_empty())

    def test_empty_is_last_node(self):
        """
        Test 10: In an empty list, the sentinel is_last_node().
        """
        ll = LinkedList()
        self.assertTrue(ll.is_last_node())

    def test_last_of_empty(self):
        """
        Test 11: The last node of an empty list is the sentinel node itself.
        """
        ll = LinkedList()
        self.assertEqual(ll, ll.last_node())

    def test_append_to_empty_list_sets_next_of_sentinel_to_new_node(self):
        """
        Test 12: Appending to an empty list sets the sentinel's `next` to the new node.
        """
        ll = LinkedList()
        appendee = LinkedList(fake_value())
        ll.append(appendee)
        self.assertEqual(appendee, ll.next)

    def test_append_to_empty_list_sets_previous_of_sentinel_to_new_node(self):
        """
        Test 13: Appending to an empty list sets the sentinel's `previous` to the new node.
        """
        ll = LinkedList()
        appendee = LinkedList(fake_value())
        ll.append(appendee)
        self.assertEqual(appendee, ll.previous)

    def test_append_to_empty_list_sets_previous_of_new_node_to_sentinel(self):
        """
        Test 14: Appending to an empty list sets the sentinel's `previous` to the new node.
        Appending to an empty list sets the new node's `previous` to the sentinel.
        """
        ll = LinkedList()
        appendee = LinkedList(fake_value())
        ll.append(appendee)
        self.assertEqual(ll, appendee.previous)

    def test_append_to_empty_list_sets_next_of_new_node_to_sentinel(self):
        """
        Test 15: Appending to an empty list sets the new node's `next` to the sentinel.
        """
        ll = LinkedList()
        appendee = LinkedList(fake_value())
        ll.append(appendee)
        self.assertEqual(ll, appendee.next)

    # """
    # Two-Node List
    # """

    def test_list_with_two_nodes_is_not_empty(self):
        """
        Test 16: A list with two nodes is not empty.
        """
        ll = LinkedList()
        appendee = LinkedList(fake_value())
        ll.append(appendee)
        self.assertFalse(ll.is_empty())

    def test_first_of_two_nodes_is_not_last(self):
        """
        Test 17: In a two-node list, the first node is not last.
        """
        ll = LinkedList()
        appendee = LinkedList(fake_value())
        ll.append(appendee)
        self.assertFalse(ll.is_last_node())

    def test_second_of_two_nodes_is_last_node(self):
        """
        Test 18: In a two-node list, the second node is last.
        """
        ll = LinkedList()
        appendee = LinkedList(fake_value())
        ll.append(appendee)
        self.assertTrue(appendee.is_last_node())

    def test_last_of_two_nodes(self):
        """
        Test 19: In a two-node list, the second node is the last node.
        """
        ll = LinkedList()
        appendee = LinkedList(fake_value())
        ll.append(appendee)
        self.assertEqual(appendee, ll.last_node())

    # def test_append_to_two_node_list_next_of_sentinel_is_second(self):
    #     """
    #     Test 20: When appending a third node to a two-node list, the sentinel's `next`
    #     remains the second node.
    #     """
    #     ll = LinkedList()
    #     second_node = LinkedList(fake_value())
    #     third_node = LinkedList(fake_value())
    #     ll.append(second_node)
    #     ll.append(third_node)
    #     self.assertEqual(second_node, ll.next)

    # def test_append_to_two_node_list_previous_of_second_is_sentinel(self):
    #     """
    #     Test 21: When appending a third node to a two-node list, the second node's `previous`
    #     remains the sentinel node.
    #     """
    #     ll = LinkedList()
    #     second_node = LinkedList(fake_value())
    #     third_node = LinkedList(fake_value())
    #     ll.append(second_node)
    #     ll.append(third_node)
    #     self.assertEqual(ll, second_node.previous)

    # def test_append_to_two_node_list_next_of_second_is_third(self):
    #     """
    #     Test 22: When appending a third node to a two-node list, the second node's `next`
    #     is the third node.
    #     """
    #     ll = LinkedList()
    #     second_node = LinkedList(fake_value())
    #     third_node = LinkedList(fake_value())
    #     ll.append(second_node)
    #     ll.append(third_node)
    #     self.assertEqual(third_node, second_node.next)

    # def test_append_to_two_node_list_previous_of_third_is_second(self):
    #     """
    #     Test 23: When appending a third node to a two-node list, the third node's `previous`
    #     is the second node.
    #     """
    #     ll = LinkedList()
    #     second_node = LinkedList(fake_value())
    #     third_node = LinkedList(fake_value())
    #     ll.append(second_node)
    #     ll.append(third_node)
    #     self.assertEqual(second_node, third_node.previous)

    # def test_append_to_two_node_list_sets_next_of_third_node_to_sentinel(self):
    #     """
    #     Test 24:When appending to a two-node list, the third node's `next` is the sentinel.
    #     """
    #     ll = LinkedList()
    #     second_node = LinkedList(fake_value())
    #     third_node = LinkedList(fake_value())
    #     ll.append(second_node)
    #     ll.append(third_node)
    #     self.assertEqual(ll, third_node.next)

    # def test_append_to_two_node_list_sets_previous_of_sentinel_to_third_node(self):
    #     """
    #     Test 25: When appending to a two-node list, the sentinel's `previous` is the third node.
    #     """
    #     ll = LinkedList()
    #     second_node = LinkedList(fake_value())
    #     third_node = LinkedList(fake_value())
    #     ll.append(second_node)
    #     ll.append(third_node)
    #     self.assertEqual(third_node, ll.previous)

    # # """
    # # Three-Node List
    # # """

    # def test_last_of_three_nodes(self):
    #     """
    #     Test 26: In a three-node list, the third node is the last node.
    #     """
    #     ll = LinkedList()
    #     second_node = LinkedList(fake_value())
    #     third_node = LinkedList(fake_value())
    #     ll.append(second_node)
    #     ll.append(third_node)
    #     self.assertEqual(third_node, ll.last_node())

    # def test_append_to_three_node_list(self):
    #     """
    #     Test 27: When appending to three-node list, the fourth node should be inserted
    #     between the third node and the sentinel node.
    #     """
    #     ll = LinkedList()
    #     second_node = LinkedList(fake_value())
    #     third_node = LinkedList(fake_value())
    #     fourth_node = LinkedList(fake_value())
    #     ll.append(second_node)
    #     ll.append(third_node)
    #     ll.append(fourth_node)
    #     self.assertEqual(fourth_node, ll.previous)
    #     self.assertEqual(ll, fourth_node.next)
    #     self.assertEqual(third_node, fourth_node.previous)
    #     self.assertEqual(fourth_node, third_node.next)

    # # """
    # # Deletion
    # # """

    # def test_delete(self):
    #     """
    #     Test 28: Deleting a node from the middle of a list removes it from the list.
    #     """
    #     ll = LinkedList()
    #     second_node = LinkedList(fake_value())
    #     third_node = LinkedList(fake_value())
    #     fourth_node = LinkedList(fake_value())
    #     ll.append(second_node)
    #     ll.append(third_node)
    #     ll.append(fourth_node)
    #     third_node.delete()
    #     self.assertEqual(fourth_node, second_node.next)
    #     self.assertEqual(second_node, fourth_node.previous)

    # # """
    # # Insertion
    # # """

    # def test_insert(self):
    #     """
    #     Test 29: Inserting a node between two nodes places it between the two nodes.
    #     """
    #     ll = LinkedList()
    #     second_node = LinkedList(fake_value())
    #     third_node = LinkedList(fake_value())
    #     insertee = LinkedList(fake_value())
    #     ll.append(second_node)
    #     ll.append(third_node)
    #     second_node.insert(insertee)
    #     self.assertEqual(insertee, second_node.next)
    #     self.assertEqual(second_node, insertee.previous)
    #     self.assertEqual(insertee, third_node.previous)
    #     self.assertEqual(third_node, insertee.next)

    # # """
    # # Retrieval
    # # """

    # def test_at(self):
    #     """
    #     Test 30: at_position(N) returns the Nth node in the list (where 0 is the sentinel.)
    #     """
    #     ll = LinkedList()
    #     second_node = LinkedList(fake_value())
    #     third_node = LinkedList(fake_value())
    #     fourth_node = LinkedList(fake_value())
    #     ll.append(second_node)
    #     ll.append(third_node)
    #     ll.append(fourth_node)
    #     self.assertEqual(second_node, ll.at_position(1))
    #     self.assertEqual(third_node, ll.at_position(2))
    #     self.assertEqual(fourth_node, ll.at_position(3))

    # # """
    # # Search
    # # """

    # def test_search_returns_none_when_not_found(self):
    #     """
    #     Test 31: Searching for a node with a particular value that does not exist in the
    #     linked list returns None.
    #     """
    #     ll = LinkedList()
    #     second_node = LinkedList("FAKE")
    #     self.assertEqual(None, ll.search("X"))

    # def test_search_returns_node_when_found(self):
    #     """
    #     Test 32: Searching for a node with a particular value returns that node, if it
    #     exists in the linked list.
    #     """
    #     value = "FAKE"
    #     ll = LinkedList()
    #     second_node = LinkedList(value)
    #     ll.append(second_node)
    #     self.assertEqual(second_node, ll.search(value))

    # # """
    # # Maintaining Order
    # # """

    # def test_insert_in_order_when_empty(self):
    #     """
    #     Test 33: Inserting a node in an empty sorted list just appends the new node.
    #     """
    #     ll = LinkedList()
    #     ll.insert_in_order(LinkedList(8))
    #     self.assertEqual(None, ll.at_position(0).value)
    #     self.assertEqual(8, ll.at_position(1).value)

    # def test_insert_in_order_less_than(self):
    #     """
    #     Test 34: Inserting a node in a sorted list when the node's value is less than an
    #     existing node's value places the new node before the existing one.
    #     Example: None -> 8 becomes None -> 6 -> 8
    #     """
    #     ll = LinkedList()
    #     ll.insert_in_order(LinkedList(8))
    #     ll.insert_in_order(LinkedList(6))
    #     self.assertEqual(6, ll.at_position(1).value)

    # def test_insert_in_order_greater_than(self):
    #     """
    #     Test 35: Inserting a node in a sorted list when the node's value is greater than
    #     an existing node's value places the new node after te existing one.
    #     Example: None -> 8 becomes None -> 8 -> 9
    #     """
    #     ll = LinkedList()
    #     ll.insert_in_order(LinkedList(8))
    #     ll.insert_in_order(LinkedList(9))
    #     self.assertEqual(9, ll.at_position(2).value)

    # def test_insert_in_order_maintains_order_of_values(self):
    #     """
    #     Test 36: Inserting nodes of arbitrary values results in the list maintaining the
    #     sorted order of nodes based on their value.
    #     Example: inserting 8, 6, 7, 5, 3, 0, 9 results in: 0, 3, 5, 6, 7, 8, 9
    #     """
    #     values = [8, 6, 7, 5, 3, 0, 9]
    #     ll = LinkedList()
    #     for value in values:
    #         ll.insert_in_order(LinkedList(value))
    #     self.assertEqual(None, ll.at_position(0).value)
    #     self.assertEqual(0, ll.at_position(1).value)
    #     self.assertEqual(3, ll.at_position(2).value)
    #     self.assertEqual(5, ll.at_position(3).value)
    #     self.assertEqual(6, ll.at_position(4).value)
    #     self.assertEqual(7, ll.at_position(5).value)
    #     self.assertEqual(8, ll.at_position(6).value)
    #     self.assertEqual(9, ll.at_position(7).value)


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
