class PriorityQueue:
    """Array-based priority queue implementation."""

    def __init__(self):
        """Initially empty priority queue."""
        self.queue = []
        self.min_index = None

    def __len__(self):
        # Number of elements in the queue.
        return len(self.queue)

    def append(self, key):
        """Inserts an element in the priority queue."""
        if key is None:
            raise ValueError('Cannot insert None in the queue')
        self.queue.append(key)
        self.min_index = None

    def min(self):
        """The smallest element in the queue."""
        if len(self.queue) == 0:
            return None
        self._find_min()
        return self.queue[self.min_index]

    def pop(self):
        """Removes the minimum element in the queue.

        Returns:
            The value of the removed element.
        """
        if len(self.queue) == 0:
            return None
        self._find_min()
        popped_key = self.queue.pop(self.min_index)
        self.min_index = None
        return popped_key

    def _find_min(self):
        # Computes the index of the minimum element in the queue.
        #
        # This method may crash if called when the queue is empty.
        if self.min_index is not None:
            return
        min = self.queue[0]
        self.min_index = 0
        for i in range(1, len(self.queue)):
            key = self.queue[i]
            if key < min:
                min = key
                self.min_index = i

