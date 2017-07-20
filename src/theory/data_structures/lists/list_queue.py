'''
Created on Jul 13, 2017

@author: ToOro
'''
from collections import deque

queue = deque(["Eric", "John", "Michel"])
queue.append("Terry")
queue.append("Graham")

print(queue.popleft())
print(queue.pop())