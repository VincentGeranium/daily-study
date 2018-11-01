
# coding: utf-8

# In[1]:


def sum(a, b):
    return a + b

def safe_sum(a, b):
    if type(a)!=type(b): #객체 a와 객체 b의 자료형이 같지 않으면
        print("더할수 있는 것이 아닙니다.") #메세지 출력
        return #메세지 출력
    else:#객체 a와 객체 b의 자료형이 같다면
        result = sum(a,b)#두 객체를 더한다
        return result
    
if __name__=="__main__":
    print(safe_sum('a', 1))
    print(safe_sum(1, 4))
    print(sum(10, 10.4))

