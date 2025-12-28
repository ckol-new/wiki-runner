class FrontierQueue:
    def __init__(self):
        self.__queue = []
    
    def push(self, item):
        self.__queue.insert(0, item)
    
    def pop(self):
        return self.__queue.pop(-1)
    
    def size(self): return len(self.__queue)