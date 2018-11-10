
# coding: utf-8

# # if 문

# ## if문은 왜 필요할까?

# 조건을 판단하여 해당 조건에 맞는 상황을 수행하는 데 쓰이는 것

# In[2]:


money = 1
if money:
    print("take a cap")
else:
    print("go to walk")


# # 3.조건문이란?

# if 조건문에서 "조건문"이란 참과 거짓을 판단하는 문장을 말한다.

# - 자료형의 참과 거짓

# - 숫자 자료형 : 참 = 0이 아닌 숫자 , 거짓 = 0
# - 문자열 자료형 : 참 = "abc" , 거짓 = " "
# - 리스트 자료형 : 참 = [1,2,3] , 거짓 = [ ]
# - 튜플 자료형 : 참 = (1,2,3) , 거짓 = ( )
# - 딕셔너리 자료형 : 참 = {"a":"b"} , 거짓 = { }

# ## 3-1.비교연산자

# - x < y , x 가 y 보다 작다
# - x > y , x 가 y 보다 크다
# - x == y , x 와 y가 같다
# - x != y , x 와 y는 같지 않다
# - x >= y , x 가 y보다 크거나 같다
# - x <= y , x 가 y보다 작거나 같다

# "만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라"

# In[7]:


money = 2000
if money >= 3000:
    print("take a cap")
else:
    print("go to walk")


# ## 3-2 .and, or, not

# - 조건을 판단하기 위해 사용하는 다른 연산자로는 and, or, not이 있다.

# - x or y = x 와 y 둘중에 하나만 참이면 참이다.
# - x and y = x 와 y 모두 참이어야 참이다.
# - not x = x 가 거짓이면 참이다.

# "돈이 3000원 이상이 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라"

# In[9]:


money = 2000
card = 1
if money >= 3000 or card == 1:
    print("take a cap")
    
else:
    print("go to walk")


# ## 3-3. x in s, x not in s

# - 더 나아가 파이썬은 다른 프로그래밍 언어에서 쉽게 볼 수 없는 재미있는 조건문들을 제공한다.

#  - x in List
#  - x in Tuple
#  - x in String
#  ---------------------------------------------------------------------
#  - x not in List
#  - x not in Tuple
#  - x not in String
#  
#  in 이라는 영어 단어의 뜻이 "~ 안에" 라는 것을 생각해 보면 다음 예들이 쉽게 이해될 것이다.

# In[10]:


1 in [1,2,3]


# - [1,2,3]이라는 리스트 안에 1이 있는가? 라는 조건문
# - 1은 [1.2.3] 안에 있으므로 True를 리턴

# In[11]:


1 not in [1,2,3]


# - [1,2,3]이라는 리스트 안에 1이 없는가? 라는 조건문
# - 1은 [1,2,3]안에 있으므로 거짓이 되어 False를 리턴

# In[12]:


'a' in ('a', 'b', 'c')


# In[13]:


'j' not in 'python'


# "만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라"
# - in 을 적용해 보자

# In[17]:


pocket = ['paper' , 'cellphone' , 'money']
if 'money' in pocket:
    print("take a cap")

else:
    print("go to walk")


# ### [조건문에서 아무 일도 하지 않게 설정하고 싶다면?]

# 가끔 조건문의 참, 거짓에 따라 실행할 행동을 정의할 때, 아무런 일도 하지 않도록 설정하고 싶을 때가 있다. 다음의 예를 보자.

# "주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라"

# 이럴 때 사용하는 것이 바로 pass이다

# In[19]:


pocket = ['paper' , 'money' , 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")


# - pocket이라는 리스트 안에 money라는 문자열이 있기 때문에 if문 다음 문장인 pass가 수행 되고 아무런 결과값도 보여 주지 않는다.

# # 4. 다양한 조건을 판단하는 elif
# ----------------------------------------------------------------------

# if 와 else만으로는 다양한 조건을 판단하기 어렵다.

# "주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라"

# 위의 문장을 보면 조건을 판단하는 부분이 두 군데가 있다. 먼저 주머니에 돈이 있는지를 판단해야 하고 주머니에 돈이 없으면 다시 카드가 있는지 판단해야 한다.

# if 와 else만으로 위의 문장을 표현

# In[20]:


pocket = ['paper', 'handphone']
card = 1
if 'money' in pocket:
    print("take a cap")
else:
    if card:
        print("take a cap")
    else:
        print("go to walk")


# 위의 예를 elif를 사용하면 다음과 같이 바꿀 수 있다.

# In[21]:


pocket = ['paper' , 'cellphone']
card = 1
if 'money' in pocket:
    print("take a cap")
    
elif card:
    print("take a cap")
    
else:
    print("go to walk")


# elif 는 이전 조건문이 거짓일 때 수행된다

# # 5. 조건부 표현식

# In[24]:


'''
if score >= 60:
    message = 'success'
else:
    message = 'failure'
'''


# 파이썬의 조건부 표현식(conditional expression)을 이용하면 위 코드를 다음과 같이 간단히 표현 할 수 있다.

# In[25]:


'''massage = "success" if score >= 60 else "failure"'''


# 조건부 표현식은 가독성에 유리하고 한 라인으로 작성할 수 있어 활용성이 좋다.

# 조건부 표현식 정의는 다음과 같이 정의된다.

# - 조건문이 _ 참인 _ 경우   if 조건문 else   조건문이 _ 거짓인 _ 경우
