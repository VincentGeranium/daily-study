
# coding: utf-8

# # if문 개념 배우기 1
# ## if ~ else

# ### 어떤 조건을 참과 거짓으로 판단하기 위한 if문의 개념을 배우는 과정
# ### 참과 거짓을 구분하여 코드를 실행하려면 if ~ else를 사용

# In[1]:


x = 1
y = 2
if x >= y:
    print('x가 y보다 크거나 같습니다')
else:
    print('x가 y보다 작습니다')


# - 코드를 작성하다 보면 조건에 따라 수행하는 일을 달리해야 하는 경우가 있다
# - 조건이 참인지 거짓인지 검사를 하고, 참인 경우레는 이 일을 하고, 거짓인 경우에는 저 일을 하라는 식으로 처리해야 하는 경우
# - if문은 조건이 참인지 아닌지를 판단, 코드를 수행할 때 사용하는 조건문

# #### 파이썬 if문의 기본적인 사용법

# ```
# if 조건:
#     실행 코드 1
# else:
#     실행 코드 2```

# - if 뒤에 조건이 참이면 실행 코드 1 실행
# - if 뒤에 조건이 거짓이면 실행 코드 2 실행

# #### 만약 조건이 참인 경우만 특정 코드를 실행하는 로직을 구현하려면 else문 없이 if문만 사용해서 조건을 체크

# ```
# if 조건:
#     실행 코드 ```

# # if문 개념 배우기 2
# ## if ~ elif

# ### 다양한 조건을 판단하기 위한 if문
# ### 여러 가지 조건들을 각각 검사하고 판단해야 할 경우 if ~ elif 를 사용

# In[2]:


x = 1
y = 2
if x>y:
    print('x가 y보다 큽니다.')
elif x<y:
    print('x가 y보다 작습니다')
else:
    print('x와 y가 같습니다')


# - 여러 개의 조건을 순차적으로 체크하고 해당 조건이 참이면 특정 로직을 수행하고자 할 때 if ~ elif문을 사용

# #### if ~ elif문의 기본적인 사용법

# ```
# if 조건 1:
#     실행 코드1
# elif 조건 2:
#     실행 코드2
# else:
#     실행 코드3```

# - 조건1이 참이면 실행 코드1을 실행
# - 조건2가 참이면 실행 코드2을 실행
# - 조건1과 조건2가 모두 거짓이면 실행 코드3 실행
# - if ~ else문과 같은 개념
