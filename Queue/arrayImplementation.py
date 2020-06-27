class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear  = -1

    def enqueue(self,value):
        if(self.isEmpty()):
            self.front=0
            self.rear=0
            self.queue.append(value)
        else:
            self.rear+=1
            self.queue.append(value)

    def dequeue(self):
        if(self.isEmpty()):
            return "Queue is Empty"
        else:
            self.front+=1
    
    def peek(self):
        return self.queue[self.front]

    def isEmpty(self):
        if(self.front==-1 and self.rear==-1):
            return True
        else:
            return False


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.dequeue()
    queue.dequeue()
    print(queue.peek())
