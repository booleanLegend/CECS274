import ArrayQueue
# from drawtree import draw_bst


class BinaryTree:
    class Node:
        def __init__(self, x: object, v=None):
            self.parent = self.left = self.right = None
            self.x = x
            self.v = v

        def set_val(self, x):
            self.x = x

        def insert_left(self):
            self.left = BinaryTree.Node('')
            self.left.parent = self
            return self.left

        def insert_right(self):
            self.right = BinaryTree.Node('')
            self.right.parent = self
            return self.right

    def __init__(self):
        self.r = None
        self.nil = None

    def depth(self, u: Node) -> int:
        if u is None:
            return -1
        d = 0
        while u != self.r:
            u = u.parent
            d += 1
        return d

    def size(self) -> int:
        return self._size(self.r)

    def _size(self, u: Node) -> int:
        if u == self.nil:
            return 0
        return 1 + self._size(u.left) + self._size(u.right)

    def size2(self) -> int:
        u = self.r
        prv = self.nil
        n = 0
        while u != self.nil:
            if prv == u.parent:
                n += 1
                if u.left != self.nil:
                    nxt = u.left
                elif u.right != self.nil:
                    nxt = u.right
                else:
                    nxt = u.parent
            elif prv == u.left:
                if u.right != self.nil:
                    nxt = u.right
                else:
                    nxt = u.parent
            else:
                nxt = u.parent
            prv = u
            u = nxt
        return n

    def height(self) -> int:
        return self._height(self.r)

    def _height(self, u: Node) -> int:
        if u == self.nil:
            return 0
        return 1 + max(self._height(u.left), self._height(u.right))

    def traverse(self, u: Node):
        if u == self.nil:
            return
        self.traverse(u.left)
        self.traverse(u.right)

    def traverse2(self):
        u = self.r
        prv = self.nil
        while u != self.nil:
            if prv == u.parent:
                if u.left != self.nil:
                    nxt = u.left
                elif u.right != self.nil:
                    nxt = u.right
                else:
                    nxt = u.parent
            elif prv == u.left:
                if u.right != self.nil:
                    nxt = u.right
                else:
                    nxt = u.parent
            else:
                nxt = u.parent
            prv = u
            u = nxt

    def bf_traverse(self):
        q = ArrayQueue.ArrayQueue()
        traverseList = []
        if self.r != self.nil:
            q.add(self.r)
            traverseList.append(self.r.v)
        while q.size() > 0:
            u = q.remove
            if u.left != self.nil:
                q.add(u.left)
                traverseList.append(u.left.v)
            if u.right != self.nil:
                q.add(u.right)
                traverseList.append(u.right.v)
        return traverseList

    def first_node(self):
        w = self.r
        if w == self.nil:
            return self.nil
        while w.left != self.nil:
            w = w.left
        return w

    def next_node(self, w):
        if w.right != self.nil:
            w = w.right
            while w.left != self.nil:
                w = w.left
        else:
            while w.parent != self.nil and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w

    def in_order(self, u: Node, l: list):
        if u is None:
            return None
        if u.left != self.nil:
            self.in_order(u.left, l)
        l.append(u.x)
        if u.right != self.nil:
            self.in_order(u.right, l)
        return l

    def pre_order(self, u: Node, l: list):
        if u is None:
            return None
        l.append(u.x)
        if u.left != self.nil:
            self.pre_order(u.left, l)
        if u.right != self.nil:
            self.pre_order(u.right, l)
        return l

    def post_order(self, u: Node, l: list):
        if u is None:
            return None
        if u.left != self.nil:
            self.post_order(u.left, l)
        if u.right != self.nil:
            self.post_order(u.right, l)
        l.append(u.x)
        return l

    def __str__(self):
        l = []
        self.in_order(self.r, l)
        return ', '.join(map(str, l))
