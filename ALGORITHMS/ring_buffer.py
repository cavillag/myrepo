
#### The below code implements a Ring Buffer as requested by LeetCode Stack data structures lesson 1


from collections import deque

class MyCircularQueue:
    def __init__(self,length):
        self.length=length
        self.que=deque([])

    def enQueue(self,enq):
        if len(self.que) == self.length:
            print("Queue is full")
            return False
        else:
            self.que.append(enq)
            return True

    def Rear(self):
        if len(self.que) == 0:
            return -1
        else:
            return self.que[-1]

    def isFull(self):
        if len(self.que) == self.length:
            return True
        else:
            return False

    def deQueue(self):
        if len(self.que) == 0:
            print("Queue is Empty")
            return False
        else:
            self.que.popleft()
            return True

    def Front(self):
        if len(self.que) == 0:
            return -1
        else:
            return self.que[0]

hachiko=MyCircularQueue(3)
hachiko.enQueue(1)
hachiko.enQueue(2)
print(hachiko.Front())
print(hachiko.Rear())
hachiko.enQueue(3)
print(hachiko.isFull())
hachiko.deQueue()
print(hachiko.isFull())
hachiko.deQueue()
print(hachiko.Front())
hachiko.enQueue(5)
print(hachiko.Rear())
