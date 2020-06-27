from collections import deque
class Node:
    def __init__(self,value):
        self.key = value
        self.next = None

class LinkedList:
    def insert(self,head,value):
        if(head == None):
            head = Node(value)
        else:
            temp = head
            while(temp.next!=None):
                temp = temp.next
            temp.next = Node(value)
        return head

    def print(self,head):
        if(head == None):
            return head
        else:
            temp = head
            while(temp!=None):
                print(temp.key)
                temp = temp.next
    
    def reverse(self,head):
        stack = deque()
        if head == None:
            return None
        else:
            temp = head
            while(temp!=None):
                stack.append(temp)
                temp = temp.next
            head = None
            while(len(list(stack))>0):
                if head == None:
                   head = stack.pop()
                   temp = head
                else:
                    node = stack.pop()
                    temp.next = node
                    temp = node
            temp.next = None
            return head



def reverse(string):
    stack = deque()
    reverse =""
    for a in string:
        stack.append(a)
    for a in range(len(string)):
        reverse+=stack.pop()
    return reverse

if __name__ == "__main__":
    ll = LinkedList()
    head = None 
    head = ll.insert(head,10)
    head = ll.insert(head,20)
    head = ll.insert(head,30)
    head = ll.insert(head,40)
    head = ll.insert(head,50)
    ll.print(head)
    head = ll.reverse(head)
    print("after reversing")
    ll.print(head)
