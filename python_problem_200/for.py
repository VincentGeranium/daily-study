
# coding: utf-8

# # For문

# #### 주어진 범위에서 반복적으로 코드를 실행하는 for문
# #### 반복 실행 코드는 for문을 이용하여 구현

# In[1]:


scope = [1,2,3,4,5]


# In[3]:


for x in scope:
    print(x)


# #### 위 코드 실행시 1 ~ 5까지 정수를 순차적으로 출력
# #### for문은 특정 범위의 자료나 객체에 대해 처음부터 끝까지 하나씩 추출하여 특정 코드를 반복적으로 수행

# ### for문의 기본적인 구문

# ```for 변수 in 범위:
#     반복으로 실행할 코드```

# - for문의 범위로 사용되는 것은 시퀀스 자료형 또는 반복 가능한 자료이어야 한다
#     - 문자열
#     - 리스트나 튜플
#     - 딕셔너리
#     - range()
#     - 그 외 반복 가능한 객체

# - 시퀀스 자료형(Sequence)
#     - 여러 객체를 저장하는 자료형
#     - 자료구조 성격을 지닌다.
#     - 각 객체의 순서를 지난다(큰 특징)
#     - 각 객체를 집합 형태로 지니면서 각 객체에는 순서가 존재한다.
#         - 문자열
#         - 리스트
#         - 튜플

# In[5]:


#문자열을 범위로 지정한 예
str = 'abcdef'
for c in str:
    print(c)


# In[6]:


#리스트를 범위로 지정한 예
list = [1,2,3,4]
for c in list:
    print(c)


# In[10]:


#딕셔너리를 범위로 지정한 예
ascii_codes = {'a':97, 'b':98, 'c':99}
for c in ascii_codes:
    print(c)

# In[11]:

#range함수를 범위로 지정한 예
for c in range(10):
    print(c)