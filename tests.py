# tests

import unittest
from stack import Stack
from queue_ds import Queue
from hash_table import HashTable


class TestStack(unittest.TestCase):

    def test_push_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_peek(self):
        s = Stack()
        s.push(5)
        self.assertEqual(s.peek(), 5)
        self.assertEqual(s.size(), 1)

    def test_pop_vacia(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()


class TestQueue(unittest.TestCase):

    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue("a")
        q.enqueue("b")
        self.assertEqual(q.dequeue(), "a")
        self.assertEqual(q.dequeue(), "b")

    def test_front(self):
        q = Queue()
        q.enqueue(10)
        self.assertEqual(q.front(), 10)
        self.assertEqual(q.size(), 1)

    def test_dequeue_vacia(self):
        q = Queue()
        with self.assertRaises(IndexError):
            q.dequeue()


class TestHashTable(unittest.TestCase):

    def test_put_get(self):
        ht = HashTable()
        ht.put("x", 10)
        self.assertEqual(ht.get("x"), 10)

    def test_remove(self):
        ht = HashTable()
        ht.put("a", 1)
        ht.remove("a")
        self.assertIsNone(ht.get("a"))

    def test_contains(self):
        ht = HashTable()
        ht.put("a", 1)
        self.assertTrue(ht.contains("a"))
        self.assertFalse(ht.contains("b"))


if __name__ == "__main__":
    unittest.main()