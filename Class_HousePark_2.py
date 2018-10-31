
# coding: utf-8

# # 초기값 설정하기

# ## $__init__$ 메서드로 초깃값을 설정

# In[3]:


class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s 여행을 가다."%(self.fullname, where))


# In[4]:


pey = HousePark()


# ``` 위와 같은 오류 메세지를 볼 수 있다. pey = HousePark() 이 라고 입력하는 순간 $__init__$ 메서드가 호출 된다
# $__init__$ 메서드는 2개의 입력값 (self,name)이 필요한데 1개의 입력값만 받았기 때문에 오류가 발생한 것이다.
# 여기서 $__init__$ 메서드가 받은 입력값 1개는 입력인수 self를 통해 받은 pey라는 객체이다.```

# #### 객체를 만들 때 어떻게 $__inti__$ 메서드에 입력값을 2개 줄 수 있을까?

# In[5]:


pey = HousePark("지성")


# #### 객체를 생성하는 순간에 입력값으로 "지성" 이라는 값을 주기만 하면 된다

# #### $__init__$ 메서드를 이용하면 인스턴스를 만드는 동시에 초깃값을 줄 수 있기 때문에 훨씬 편하다
# #### $__init__$ 메서드는 생성자(Constructor)라고도 한다.

# In[6]:


pey = HousePark("지성")


# In[7]:


pey.travel("NewYork")


# ## 클래스의 상속

# #### 상속(Inheritance)란 '물려받다'라는 뜻, '재산을 상속받다'라고 할 때의 상속과 같은 의미
# #### 클래스에도 이런 개념을 적용할 수 있다
# #### 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것이다.

# In[8]:


class HouseKim(HousePark):
    lastname = "김"


# ### 클래스명 뒤 괄호 안에 다른 클래스명을 넣어 주면 상속을 받게 된다
# #### class 상속 받을 클래스 명(상속할 클래스 명)

# In[9]:


taehee = HouseKim("태희")
taehee.travel("대전")


# #### HouseKim 클래스는 HousePark 클래스의 모든 기능을 그대로 상속받음
# #### $__init__$ 메서드와 travel 메서드를 구현하지 않아도 HousePark 클래스와 완전히 동일하게 동작

# ### 메서드 오버라이딩

# #### 상속의 개념 중 하나
# #### 클래스를 만들다 보면 상속받을 대상인 클래스의 메서드와 이름은 같지만 그 행동을 다르게 해야 할 때 사용

# In[12]:


class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s여행 %d일 가네"%(self.fullname, where, day))


# #### travel 함수를 다르게 설정하고 싶으면 동일한 이름의 travel 함수를 HouseKim 클래스 내에서 다시 구현하면 됨
# #### 이렇게 메서드 이름을 동일하게 다시 구현하는 것을 메서드 오버라이딩(Overriding)이라고 한다.

# ### 연산자 오버로딩

# #### 연산자 오버로딩(Overloading)이란 연산자(+ , - , * , / , ...)를 객체끼리 사용할 수 있게 하는 기법

# In[13]:


class HouseChoi:
    lastname = "최"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s 여행을 가다."%(self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네"%(self.fullname, other.fullname))
    def __add__(self, other): # <- 연산자 오버로딩 사용
        print("%s, %s 결혼했네, 평생 서로를 사랑하네" %(self.fullname, other.fullname))


# In[14]:


class HouseKim(HouseChoi):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s여행 %d일 가네" %(self.fullname, where, day))


# In[15]:


SuA = HouseChoi("수아")


# In[16]:


KwangJun = HouseKim("광준")


# In[17]:


SuA.love(KwangJun)


# In[18]:


SuA + KwangJun


# #### 실행부분 살펴보기

# In[19]:


SuA = HouseChoi("수아") # <- SuA 객체 생성
KwangJun = HouseKim("광준") # <- KwangJun 객체 생성
SuA.love(KwangJun) # <- love 메서드 호출
SuA + KwangJun


# #### 먼저 SuA = HouseChoi("수아")으로 SuA라는 객체를 만들고 KwangJun이라는 객테도 생성
# #### 그 다음 SuA.love(KwangJun)으로 love 메서드를 호출

# #### love 메서드를 보면 입력 인수로 2개의 객체를 받는 것을 알 수 있다.
# ```def love(self, other):
#         print("%s, %s 사랑에 빠졌네"%(self.fullname, other.fullname))```

# #### SuA.love(KwangJun)과 같이 호출하면 self에는 SuA가 들어가고 other에는 KwangJun이 들어간다
# #### "최수아, 김광준 사랑에 빠졌네"라는 문장이 출력된다.

# #### SuA + KwangJun
# #### 더하기 기호인 +를 이용해서 객체끼리 더하려고 한다.
# #### 이렇게 + 연산자를 객체에 사용하게 되면 HouseChoi 클래스의 $__add__$ 라는 함수가 호출된다.

# #### HouseChoi 클래스에서 $__add__$ 함수가 선언된 부분 살펴보기
# ```def __add__(self, other): # <- 연산자 오버로딩 사용
#         print("%s, %s 결혼했네, 평생 서로를 사랑하네" %(self.fullname, other.fullname))```

# #### SuA + KwangJun 처럼 호출되면 $__add__(self, other)$ 메서드의 self는 SuA가 되고 other은 KwangJun이 된다
# #### "최수아, 김광준 결혼했네, 평생 서로를 사랑하네"라는 문자열이 출력된다
