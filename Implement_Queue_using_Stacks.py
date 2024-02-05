'''
232. Implement Queue using Stacks

Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, 
size, and is empty operations are valid. Depending on your language, the stack may not be supported natively. 
You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
 

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? 
In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
'''

from os import system


class MyQueue:

    def __init__(self):
        self.stack = []
        self.queue = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.queue.append(self.stack.pop())        

    def pop(self) -> int:
        if not self.empty():
            popped = self.queue[0]
            self.queue = self.queue[1:len(self.queue)]
            return popped


    def peek(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False

obj = MyQueue()


while(True):
    print("1. Push\n2. Pop\n3. Peek\n4. Check\n5. Exit")
    option = int(input("Enter your option: "))
    system('cls')
    if option == 1:
        value = int(input("Enter Data to be Pushed: "))
        obj.push(value)
    elif option == 2:
        print("Popped",obj.pop())
    elif option == 3:
        print("Top Element:",obj.peek())
    elif option == 4:
        print("Empty:",obj.empty())
    elif option == 5:
        exit(1)
    else:
        print("Enter Valid Option")
    




# Your MyQueue object will be instantiated and called as such:

# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()