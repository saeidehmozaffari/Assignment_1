#!/usr/bin/env python
# coding: utf-8

# In[ ]:



name=input('enter your name:')

score1=float(input('enter your score1:'))
score2=float(input('enter your score2:'))
score3=float(input('enter your score3:'))

if 0 < score1 <= 20 and 0 < score2 <= 20 and 0 < score3<=20:     
    average=(score1+score2+score1)/3
    if average >=17:
        print(average,'   great')
    elif 17 > average >= 12:
        print(average,'   normal')
    elif average <12:
        print(average,'   failed')
else:
    print('score is wrong!!!')


# In[ ]:




