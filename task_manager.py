import heapq
from collections import deque
task=[]
heapq.heappush(task,(2,"study"))
heapq.heappush(task,(1,"eat"))
heapq.heappush(task,(3,"sleep"))
heapq.heappush(task,(4,"wake up early"))
todo=deque()
todo.append("complete assignment")
todo.append("attend meeting")
print("Tasks in priority order:")
while task:
    priority, t=heapq.heappop(task)
    print(f"Priority {priority}: {t}") 
print("\nTo-Do List:")
while todo:
    print(f"- {todo.popleft()}")

import heapq
from collections import deque
task=[]
heapq.heappush(task,(2,"study"))
heapq.heappush(task,(1,"eat"))
heapq.heappush(task,(3,"sleep"))
heapq.heappush(task,(4,"wake up early"))
todo=deque()
todo.append("complete assignment")
todo.append("attend meeting")
print("Tasks in priority order:")
while task:
    priority, t=heapq.heappop(task)
    print(f"Priority {priority}: {t}") 
print("\nTo-Do List:")
while todo:
    print(f"- {todo.popleft()}")             