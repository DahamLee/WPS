class Queue(list):
    enqueue = list.append#1
    
    def dequeue(self):#2
        return self.pop(0)

    def empty(self):#3
        if not self:
            return True
        else:
            return False

    def peek(self):#4
        return self[0]

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    while not q.empty():
        print(q.dequeue(), end = '  ')
