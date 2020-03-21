#!/usr/bin/env python
# coding: utf-8

# In[75]:


n=int(input('請輸入一個整數'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print("\n")


# In[50]:


n=int(input('請輸入一個整數'))

for i in range(1,n+1):
    for j in range(0,3-i):
        print(" ",end=" ")
    for k in range(0,2*i-1):
        print("*",end=" ")
    print("\n")


# In[40]:


n=int(input('請輸入一個整數'))
for i in range(1,n+1):
    for j in range(0,2*i-1,1):
        print('*',end="")
    print("\n")    


# In[38]:


n=int(input('請輸入一個整數'))
for i in range(0,n+1):
    print(1)


# In[46]:


n=int(input('請輸入一個整數'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1 :
            print('@',end=' ')
        else:
            print('',end=' ')
    print('\n')


# In[63]:


n=int(input('請輸入一個整數'))
for i in range(1,n+1):
    for j in range(1,2*n):
        if n+1<= i+j  :
            print('@',end=' ')
        else:
            print('',end=' ')
    print('\n') 


# In[70]:


n=int(input('請輸入一個整數'))
for i in range(1,n+1):
    for j in range(0,n-i):
        print(' ',end=' ')
    for k in range(0,2*i-1):
        print('@',end=' ')
    print('\n')


# In[ ]:




