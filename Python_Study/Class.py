
# coding: utf-8

# # 클래스

# ## 클래스 개념 잡기

# - 클래스는 빵 틀 또는 뽑기 틀 이라고 생각하면 이해하기 쉽다
#     - 별 모양의 틀(클래스)로 찍으면 별 모양의 뽑기(인스턴스)가 생성된다.
#     
# - 클래스란 똑같은 무엇인가를 계속해서 만들어낼 수 있는 설계 도면 같은 것(뽑기 틀)
# - 인스턴스란 클래스에 의해서 만들어진 피조물 (별 모양 뽑기)를 뜻한다.
#     -인스턴스(instance)와 객체는 같은 말이다, 클래스에 의해서 생성된 객체를 인스턴스라고 부른다.

# - 파이썬 클래스의 간단한 예

# In[6]:


class Simple:
    pass


# - 위에서 만든 Simple 클래스의 인스턴스를 만드는 방법

# In[7]:


a = Simple()


# - Simple()의 결과값을 돌려받은 a가 바로 인스턴스이다.
#     - 함수를 사용해서 그 결과값을 돌려받는 모습과 비슷하다.

# ## 객체와 인스턴스의 차이

# - 예시를 통한 설명
#     - navi = Cat() 이렇게 만들어진 navi는 객체
#     - navi라는 객체는  Cat의 인스턴스
#     - 즉, 인스턴스라는 말은 특정 객체(navi)가 어떤 클래스(Cat)의 객체인지를 관계 위주로 설명할때 사용된다.
#     - 'navi는 인스턴스' 보다 'navi는 객체' 라는 표현이 어울린다
#     - 'navi는 Cat의 객체'보다는 'navi는 Cat의 인스턴스'라는 표현이 훨씬 잘 어울린다.

# ## 클래스 변수

# In[12]:


class Service:
    secret = "Hello It's Mario"


# In[13]:


pey = Service()


# In[14]:


pey.secret


# ## 클래스 함수

# In[15]:


class Service:
    secret = "Hello It's Mario"
    def sum(self, a, b):
        result = a + b
        print("%s + %s = %s입니다"%(a, b, result))


# In[16]:


pey = Service()


# In[17]:


pey.sum(1,1)


# ## Self 간단히 살펴보기

# In[18]:


def sum(self, a, b):
    result = a + b
    print("%s + %s = %s입니다"%(a, b, result))


# - sum함수는 첫 번째 입력값으로 self라는 것을 받고
# - 두 번째, 세 번째 입력값으로 더할 숫자를 받는다.
# - 입력으로 받는 입력 인수의 개수가 총 3개인 것이다.

# In[20]:


pey.sum(1, 1)


# - pey.sum(1, 1)이라는 호출이 발생하면 self는 호출 시 이용했던 인스턴스(즉,pey)로 바뀌게 된다.
# - 그래서 pey.sum(pey, 1, 1)이 아닌 pey.sum(1, 1)이 가능하게 된 것이다

# ## self 제대로 알기

# In[22]:


class Service:
    secret = "Hello It's Mario"
    def setname(self, name):
        self.name = name
    
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다"%(self.name, a, b, result))


# In[24]:


pey = Service()


# In[25]:


pey.setname("Vincent")


# In[26]:


pey.sum(1, 1)


# - setname 살펴보기

# In[27]:


def setname(self, name):
    self.name = name


# In[28]:


pey.setname("Vincent")


# - 위와 같이 pey와 Vincent를 연결해 주는 것이 바로 self다

# #### setname 함수가 실행되는 순서

# - 1.pey라는 인스턴스는 Vincent를 setname 함수에 입력으로 준다

# In[30]:


pey.setname("Vincent")


# - 2.그러면 다음의 문장이 수행된다.
#     - self.name = name

# - 3.self는 첫 번째 입력값으로 pey라는 인스턴스를 받게 되므로 다음과 같이 바뀔 것이다.
#     - pey.name = name

# - 4. name은 두 번째로 입력받은 "Vincent"라는 값이므로 위의 문장은 다시 다음과 같이 바뀔것이다.
#     - pey.name = "Vincent"

# In[35]:


def sum(self, a, b):
    result = a + b
    print("%님 %s + %s = %s입니다"%(self.name, a, b, result))


# In[36]:


pey = Service()
pey.setname("Vincent")
pey.sum(1, 1)


# - sum함수가 어떻게 pey라는 인스턴스의 이름인 vincent를 알게 되었을까?
#     - 먼저 setname 함수에 의해서 'Vincent'라는 이름을 설정해 주었기 때문에 pey.name이 'Vincent'라는 값을 갖게 된다
#     - 따라서 sum함수에서도 self.name은 pey.name으로 치환된다
#     - **self는 Service에 의해서 생성된 인스턴스 (예 :  pey)를 지짗한다는 사실을 잊지 말자.

# ## $__init__$이란 무엇인가?

# In[38]:


class Service:
    secret = "Hello It's Mario"
    def __init__(self, name):
        self.name = name
    
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s 입니다"%(self.name, a, b, result))


# - 위의 Service 클래스를 이전의 클래스와 비교해 보면 바뀐 부분은 딱 한 가지이다.
# - 바로 setname 함수의 이름인 setname이 $__init__$으로 바뀐 것이다.
# - 클래스에서 $__init__$이라는 함수는 특별한 의미를 갖는다
#     - 그 의미는 다음과 같다
#     - $"인스턴스를 만들 때 항상 실행된다."$

# - 이전에는 pey = Service()라고만 입력하면 되었지만 이제는  $__init__$함수 때문에 pey = Service("Vincent")처럼 인스턴스를 만들때 이름까지 함꼐 입력해야 한다.

# In[40]:


pey = Service("Vincent")
pey.sum(1, 1)


# ## 클래스 자세히 알기

# - 클래스란 인스턴스를 만들어내는 공장과도 같다
# - 이 인스턴스를 어떻게 사용할 수 있는지를 알려면 클래스의 구조를 보면 된다.
# - 즉, 클래스는 해당 인스턴스의 청사진(설계도)이라고 할 수 있다.

# ### 클래스 구조

# - 클래스는 기본적으로 다음과 같은 구조를 가지고 있다.

# In[43]:


"""
class 클래스 이름[(상속 클래스명)]:
        <클래스 변수 1>
        <클래스 변수 2>
        <..........>
        <클래스 변수 n>
        
def 클래스 함수 1(self[,인수1 , 인수2,,,]):
    <수행할 문장 1>
    <수행할 문장 2>
    <..........>
    
def 클래스 함수 2(self[,인수1 , 인수2,,,]):
    <수행할 문장 1>
    <수행할 문장 2>
    <..........>

def 클래스 함수 N(self[,인수1 , 인수2,,,]):
    <수행할 문장 1>
    <수행할 문장 2>
    <..........>
"""
pass


# ## 클래스 만들기 (사칙연산)

# ### 클래스를 어떻게 만들지 먼저 구상하기

# - 클래스에 의해서 만들어진 객체를 중심으로 어떤식으로 동작하게 할 것인지 미리 구상.
# - 그 후에 생각했던 것들을 하나씩 해결하면서 완성해 나가야 한다.

# ### 클래스 구조 만들기

# In[48]:


class FourCal:
    pass


# 현재 상태에서 FourCal 클래스는 아무런 변수나 함수도 포함하지 않지만 우리가 원하는 객체 a를 만들 수 있는 기능은 가지고 있다

# In[49]:


#확인
a = FourCal()
type(a)


# - 객체 a의 타입은 ForCal 클래스이다.

# - 위와 같이 a = FourCal()로 a라는 객체를 먼저 만들고 그 다음에 type(a)로 a라는 객체가 어떤 타입인지 알아보앗다.
# - 객체 a가 FourCal 클래스의 인스턴스임을 알 수 있다.
# - type 함수는 파이썬이 자체적으로 가지고 있는 내장 함수로 객체의 타입을 출력한다.

# ### 객체에 숫자 지정할 수 있게 만들기

# - 다음과 같이 연산을 수행할 대상 (4, 2)을 객체에 지정할 수 있게 만들기.
#     - a.setdata(4, 2)

# In[51]:


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second


# - setdata라는 함수를 만들었다
# - 클래스 함수를 다른 말로 메서드(Method)라고도 한다

# In[53]:


def setdata(self, first, second): # 1. 메서드의 입력 인수
        self.first = first        # 2. 메서드의 수행문 (1)
        self.second = second      # 3. 메서드의 수행문 (2)


# - 입력 인수로 self, first, second 라는 3개의 입력값을 받는다.

# In[54]:


a = FourCal()
a.setdata(4, 2)


# - a라는 객체를 만든 다음에 a.setdata(4, 2)처럼 하면 FourCal 클래스의 setdata 메서드가 호출되고 setdata 메서드의 첫 번째 인수에는 자동으로 a라는 인스턴스가 입력으로 들어가게 된다.
#     - 즉, setdata의 입력 인수는 self, first, second로 총 3개이지만 a.setdata(4, 2)처럼 2개의 입력값만 주어도 a라는 인스턴스가 setdata 함수의 첫 번쨰 입력을 받는 변수인 self에 대입되게 된다.

# - self: 객체a , first: 4 , second: 2

# # 사칙연산 클래스 만들기

# In[57]:


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


# In[58]:


a = FourCal()


# In[59]:


b = FourCal()


# In[60]:


a.setdata(4, 2)


# In[61]:


b.setdata(3, 7)


# In[62]:


a.sum()


# In[63]:


a.mul()


# In[64]:


a.sub()


# In[65]:


a.div()


# In[66]:


b.sum()


# In[67]:


b.mul()


# In[68]:


b.sub()


# In[69]:


b.div()

