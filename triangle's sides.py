#!/usr/bin/env python
# coding: utf-8

# In[7]:


side1=float(input('enter side1:'))
side2=float(input('enter side2:'))
side3=float(input('enter side3:'))
if side1 < side2+side3 and side2 < side1+side3 and side3 < side2+side1:
    print('It is possible to draw a triangle.')
else:
        print('It is not possible to draw a triangle!!!')
  


# In[ ]:




