class Node:
    def __init__(self,value):
        self.key = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self,value):
        if(self.isEmpty()):
            self.front = Node(value)
            self.rear = self.front
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next

    def dequeue(self):
        if(self.isEmpty()):
            print("queue is Empty")
        else:
            if(self.front == self.rear):
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next

    def peek(self):
        return self.front.key

    def isEmpty(self):
        if(self.front==None and self.rear == None):
            return True
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
