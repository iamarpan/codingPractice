from collections import deque
class Queue:
    def __init__(self):
        self.pushStack = deque()
        self.popStack = deque()

    def isEmpty(self,stack):
        if(len(stack)==0):
            return True
        else:
            return False
    
    def enqueue(self,value):
        self.pushStack.append(value)
                
    def dequeue(self):
        if(len(self.popStack)>0):
            return self.popStack.pop()
        else:
            if(self.isEmpty(self.pushStack)):
                return "queue is empty"
            else:
                while(len(self.pushStack)>0):
                    val = self.pushStack.pop()
                    self.popStack.append(val)
                return self.popStack.pop()



if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
