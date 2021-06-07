from SLLQueue import SLLQueue


class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)

    def add(self, x: object):
        super().add(x)

    def remove(self) -> object:
        return super().remove()

    def size(self):
        super().size()

    def max(self):
        return max(self)
