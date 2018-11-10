
# coding: utf-8

# # '박씨네 집' 클래스 만들기

# ## 클래스 구상하기

# ### 어떤 클래스를 만들지 대충 그림 그리기

# - 박씨 가족의 '이름'을 설정하려면?
#     - setname 메서드
# - 박씨 가족 중 한 사람이 여행 가고 싶은 곳을 출력하려면?
#     - travel 메서드

# - 1.클래스 이름은 HousePark 으로 하자. 다음처럼 pey라는 인스턴스를 만든다.
#     - ```>>> pey = HousePark()```

# - 2.pey.lastname을 출력하면 '박씨네 집'이라는 클래스에 걸맞게 '박'이라는 성을 출력하게 만들기로 하자.
#     - ``>>> print(pey.lastname)
#     - '박
#     

# - 3.이름을 설정하면 pey.fullname이 성을 포함한 값을 가지도록 만든다.
#     - ``>>> pey.setname("지성") 
#     - ``>>> print(pey.fullname)
#     - '박지성' 
#      

# - 4. 여행 가고 싶은 장소를 입력으로 주면 다음과 같이 출력해 주는 travel 함수도 만들어 보자.
#       - ``>>>pey.travel("부산")
#       - '박지성, 부산여행을 가다.'

# ### 클래스 기능 만들기

# - 1.먼저 아무런 기능 없이 단순히 객체만 생성할 수 있는 클래스

# In[2]:


class HousePark:
    pass


# - ```2.이렇게 클래스를 생성하면 pey = HousePark()처럼 입력해서 객체를 만들 수 있다. 
#      이번에는 pey.lastname을 수행하면 '박'을 출력하기 위해 pass를 삭제한 후 만들어 보자.```

# In[4]:


class HousePark:
    lastname = '박'


# - lastname은 클래스 변수이다. 이 클래스 변수 lastname은 HousePark 클래에 의해서 생성되는 인스턴스 모두에 '박'이라는 값을 갖게 된다

# - 예시

# In[6]:


pey = HousePark()


# In[7]:


print(pey.lastname)


# In[8]:


jey = HousePark()


# In[9]:


print(jey.lastname)


# - 위의 예시에서 봤듯이 HousePark 클래스에 의해서 생긴 인스턴스 pey와 jey 모두 lastname이 '박'으로 설정되는 것을 확인할 수 있다.

# - 3.이름은 설정하고 print(pey.fullname)을 수행하면 성을 포함한 이름은 출력하도록 만들어 보자.

# In[10]:


class HousePark:
    lastname = '박'
    def setname(self, name):
        self.fullname = self.lastname + name


# - 우선 이름을 설정하기 위해 setname이라는 메서드를 만들었다. 이 메서드는 다음처럼 사용 할 수 있다

# In[11]:


pey = HousePark()
pey.setname('지성')


# - setname 함수에 '지성' 이라는 값을 인수로 주면 self.fullname에는 결국  '박' + '지성' 이라는 값이 대입된다

# - '지성'을 입력으로 주었을 때 '박지성'이 생성되는 과정
#     - 다음은 성을 포함한 이름을 만드는 문장
#     - self.fullname = self.lastname + name
#     

# - setname 메서드에서 두 번째 입력값 name은 '지성' 이므로 위의 문장은 다음과 같이 바뀐다.
#     - self.fullname = self.lastname + '지성'

# - 이 문장에서 self는 setname 함수의 첫 번째 입렵으로 들어오는 pey라는 인스턴스이기 때문에 다시 다음과 같이 바뀐다.
#     - pey.fullname = pey.lastname + '지성'

# - pey.lastname은 클래스 변수로 항상 '박' 이라는 값을 갖기 때문에 다음과 같이 바뀐다.
#     - pey.fullname = '박' + '지성'

# - 따라서 pey.fullname을 출력하면 다음과 같은 결과를 얻을 수 있다.

# In[13]:


print(pey.fullname)


# - 4.이제 우리가 만들려고 했던 클래스의 기능 중 입력받은 장소로 박지성이 여행을 간다고 출력해 주는 travel 메서드를 HousePark 클래스에 구현

# In[14]:


class HousePark:
    lastname = '박'
    def setname(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다"%(self.fullname,where))


# - ```travel 메서드는 입력값으로 인스턴스(self)와 장소(where)를 받는다. 
#   그리고 해당 값들은 문자열 포매팅 연산자(%s)를 이용하여 문자열에 삽입한 후 출력한다```

# In[15]:


pey = HousePark()


# In[16]:


pey.setname('지성')


# In[17]:


pey.travel('부산')

