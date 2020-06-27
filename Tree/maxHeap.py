import math
class Heap:
    def __init__(self):
        self.heap = []
        self.swap = []
    def parent(self,i):
        return math.floor((i-1)/2)

    def getMax(self):
        return self.heap[0]
    
    def shiftUp(self,i):
        while(i>0 and self.heap[self.parent(i)]>self.heap[i]):
            self.heap[i],self.heap[self.parent(i)] = (self.heap[self.parent(i)], self.heap[i])
            self.swap.append((self.parent(i),i))
            i = self.parent(i)
            
        
    def choice(self,i):
        if(self.heap[2*i+1]<self.heap[2*i+2]):
            return 2*i+1
        else:
            return 2*i+2

    def shiftDown(self,i):
        while(i<len(self.heap) and self.heap[i] > self.heap[self.choice(i)]):
            self.heap[i],self.heap[self.choice(i)] = self.heap[self.choice(i)],self.heap[i]
            

    def extractMax(self):
        maximum = self.getMax()
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.shiftDown(0)
        return maximum

    def insert(self,array):
        self.heap = array
        for index in range(len(self.heap)-1,-1,-1):
            print(index)
            self.shiftUp(index)

if __name__ == '__main__':
    heap = Heap()
    heap.insert([1,2,3,4,5])
    print(heap.swap)
