
# coding: utf-8

# # 문자열 내 p와 y의 개수

# ## 문제 설명

# ```대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요.
# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 
# 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
# 예를들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.```

# In[1]:


def solution(s):
    if s.lower().count('p') == s.lower().count('y'):
        return True
    else:
        return False


# In[2]:


## 테스트로 출력해 보기 위한 코드입니다.
print(solution("pPoooyY"))
print(solution("pPy"))

