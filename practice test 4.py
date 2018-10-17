
# coding: utf-8

# In[12]:


#Q1 틀림
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return n >= 2 == fib(n+n)


# In[24]:


#Q2 틀림
# f = open('sample.txt')
# lines = f.readlines()
# f.close()

# total = 0 
# for line in lines:
#     score = int(line)
#     total += score

# average = total/len(line)

# f = open("result.txt","w")
# f.write("sample.txt")
# f.close()


# In[25]:


#Q1 답지
#재귀호출을 이용
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2)+fib(n-1)


# In[26]:


for i in range(10):
    print(fib(i))


# In[27]:


f = open('sample.txt')
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score
    
average = total/len(lines)

f = open('result.txt','w')
f.write(str(average))
f.close()

