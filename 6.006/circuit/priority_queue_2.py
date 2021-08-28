class PriorityQueue:
    """Array-based priority queue implementation."""

    def __init__(self):
        """Initially empty priority queue."""
        self.queue = []

    def __len__(self):
        # Number of elements in the queue.
        return len(self.queue)

    def append(self, key):
        """Inserts an element in the priority queue."""
        leaf_idx = len(self.queue)
        self.queue.append(key)
        if leaf_idx == 0:
            return
        else:
            self._max_heapify_up(leaf_idx)
        # print(self.queue)

    def min(self):
        """The smallest element in the queue."""
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def pop(self):
        """Removes the minimum element in the queue.

        Returns:
            The value of the removed element.
        """
        idx = len(self.queue)
        if idx == 0:
            return None

        if idx == 1:
            val = self.queue[0]
            self.queue = []
            return val

        val = self.queue[0]
        self.queue[0] = self.queue[idx - 1]
        del self.queue[idx - 1]
        self._max_heapify_down(0)
        # print(val, self.queue)
        return val

    def _max_heapify_up(self, idx):
        if idx == 0:
            return
        parent = idx // 2
        if self.queue[parent] > self.queue[idx]:
            self.queue[parent], self.queue[idx] = self.queue[idx], self.queue[parent]
            self._max_heapify_up(parent)

    def _max_heapify_down(self, idx):
        if idx >= len(self.queue) // 2:
            return

        left = idx * 2 + 1
        right = idx * 2 + 2

        if self.queue[idx] <= self.queue[left]:
            if right >= len(self.queue) or self.queue[idx] <= self.queue[right]:
                return

        swap_idx = left
        if right < len(self.queue) and self.queue[swap_idx] > self.queue[right]:
            swap_idx = right

        self.queue[idx], self.queue[swap_idx] = self.queue[swap_idx], self.queue[idx]
        self._max_heapify_down(swap_idx)
