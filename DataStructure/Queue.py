
# coding: utf-8

# # Queue

# #### - 먼저 집어 넣은 데이터를 먼저 꺼내는 데이터 저장 공간
# #### - 예를 들어 양쪽으로 뚫린 파이프에 한쪽으로는 넣기만 하고 한쪽으로는 빼기만 하는 것
# #### - First In First Out [FIFO]

# ## Queue를 구성하는 함수 (Java)

# ### java 함수
# - add()
#     - 맨 끝에 데이터를 넣는것
# - remove()
#     - 맨 앞에서 데이터 꺼내는 것
# - peek()
#     - 맨 앞에 있는 데이터를 보는 것
# - isEmpty()
#     - queue가 비었나 확인하는 것

# In[4]:


#파이썬 내장 함수 확인
builtins = dir(__builtin__)
print(builtins)


# ## 파이썬 리스트를 이용한 큐 구현

# In[13]:


class Queue:
    def __init__(self):
        self.container=list()
        
    def empty(self):
        if not self.container:
            return True
        else:
            return False
        
    def enqueue(self, data):
        self.container.append(data)
        
    def dequeue(self):
#         print(self.container[0])
#         del self.container[0]
        return self.container.pop(0)
        
    def peek(self):
        return self.container[0]


# In[14]:


q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

while not q.empty():
    print(q.dequeue(), end= ' ')

