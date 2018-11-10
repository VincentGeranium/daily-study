
# coding: utf-8

# In[2]:


class HouseChoi:
    lastname = "최"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s 여행을 가다."%(self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네"%(self.fullname, other.fullname))
    def forever(self, other):
        print("%s, %s 서로 평생을 사랑하네"%(self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼했네"%(self.fullname, other.fullname))
    def __mul__(self, other):
        print("%s, %s 서로에게 하루 하루가 축복이고 행복하네"%(self.fullname, other.fullname))

class HouseKim(HouseChoi):
    lastname = "김"
    def travel(self, where, day):
        print("%s. %s여행 %d일 가네"%(self.fullname, where, day))


# In[3]:


SuA = HouseChoi("수아")
KwangJun = HouseKim("광준")
SuA.travel("포항")
KwangJun.travel("포항" , 1)
SuA.love(KwangJun)
SuA + KwangJun
SuA.forever(KwangJun)
SuA * KwangJun

