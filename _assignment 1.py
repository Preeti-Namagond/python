#!/usr/bin/env python
# coding: utf-8

# In[19]:


list=[2,4,5,6,3,7,1,8,9,10]
print(list[4:8])


# In[5]:


l1=[10,20,[30,40,[50,60],80],90,100]
l1[2][2].insert(2,70)
print(l1)


# In[18]:


l2=[1,2,[3,4,5,6],9]
l2[2].append([7,8])
print(l2)


# In[17]:


dict1 = { 
   "april_batch":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "python":80,
            "maths":70
         }
      }
   }
}
#from the above dict1
print(dict1["april_batch"]["student"]["name"])
print(dict1["april_batch"]["student"]["marks"]["python"])
dict1["april_batch"]["student"]["name"] = "preeti rn"
print(dict1["april_batch"]["student"]["name"])
dict1["april_batch"]["student"]["marks"]["ML"] = 80
dict1["april_batch"]["student"]["marks"]["DL"] = 80
print(dict1)


# In[3]:


### Task6 - Add and remove the elements from a tuple. (Refer workaroud to modify the tuples)
tup1 = (1,2,3,4,5)
print("original tuple", tup1)


# In[6]:


###Convert to list 
tup1=(1,2,3,4,5)
list1=list(tup1)
print(list1)


# In[8]:


num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
choice = int(input("Press 1 for addition, 2 for Subtraction, 3 for Multiplication and 4 for Division: "))
if(choice == 1):
    print("addition= ",num1 + num2)
elif(choice == 2):
    print("subtraction= ",num1 - num2)
elif(choice == 3):
    print("Multiplication= ",num1 * num2)
else:
    print("Division= ",num1 / num2)


# In[9]:


num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
choice = int(input("Press 1 for addition, 2 for Subtraction, 3 for Multiplication and 4 for Division: "))
if(choice == 1):
    print("addition= ",num1 + num2)
elif(choice == 2):
    print("subtraction= ",num1 - num2)
elif(choice == 3):
    print("Multiplication= ",num1 * num2)
else:
    print("Division= ",num1 / num2)


# In[10]:


num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
choice = int(input("Press 1 for addition, 2 for Subtraction, 3 for Multiplication and 4 for Division: "))
if(choice == 1):
    print("addition= ",num1 + num2)
elif(choice == 2):
    print("subtraction= ",num1 - num2)
elif(choice == 3):
    print("Multiplication= ",num1 * num2)
else:
    print("Division= ",num1 / num2)


# In[12]:


i = 10
while i>0:
    print(i)
    i =i- 1


# In[14]:


list = [2,4,6,8]
for i in list:
    print(i*2)


# In[15]:


t = (1,3,5,7,9)

for i in t:
    print(i**3)


# In[16]:


dict = {"student no":5,"name":"preeti","age":20}
print("keys")
for i in dict:
    print(i)
print("\nvalues")
for i in dict:
    print(dict[i])


# In[ ]:




