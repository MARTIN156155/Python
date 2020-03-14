#!/usr/bin/env python
# coding: utf-8

# In[3]:


N=int(input('請輸入一個數字'))
if N%2 == 0 :
    print('是偶數')
else:        
    print('是奇數')


# In[7]:


a=int(input('輸入數字'))
b=int(input('輸入數字'))
c=int(input('輸入數字'))


if a+b>c and b+c>a and a+c>b:
    print('可構成三角形')
else :
    print('不行')


# In[34]:


tri=[]

for i in range(3):
    tri.append(int(input("請輸入一個數字")))
    
print(tri)

for i in range(len(tri)):
    print(tri[i])
    
    
for i in tri  :
    print(i)


# In[23]:


num=['a','b','c']
for i in range(len(num)):
    print(num[i] )
    
# print(len(num))


# In[22]:


for i in range(1,6,2):
    print(i)


# In[26]:


tri=[]

for i in range(3):
    tri.append(int(input("請輸入一個數字")))
    

for i in tri :
    print(i)
    
for i in range(len(tri)):
    print(tri[i])
    
    

