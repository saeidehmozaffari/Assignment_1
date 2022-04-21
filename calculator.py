#!/usr/bin/env python
# coding: utf-8

# In[15]:


import math
try:        
    num1=float(input('enter num1:'))
    op=input('enter operator * / + - radical sin cot cos tan factorial:')
    if op=='radical':
        out=math.sqrt(num1)
    elif op=='sin':
            out=math.sin(math.radians(num1))
    elif op=='cot':
        try:
            out=1/math.tan(math.radians(num1))
        except:
            out='cant divide by 0 '
    elif op=='cos':
        out=math.cos(math.radians(num1))
    elif op=='tan':
        out=math.tan(math.radians(num1))
    elif op=='factorial':
        out=math.factorial(num1)
    else:
        num2=float(input('enter num2:'))
        if op=='+':
            out=num1+num2
        elif op=='-':
            out=num1-num2
        elif op=='*':
            out=num1*num2
        elif op=='/':
            try:
                out=num1/num2
            except:
                out='cant divide by 0 '
        else:
           out= 'the operator is not valid'
    print(out)
except:
    print("something is wrong!!!")


# In[ ]:




