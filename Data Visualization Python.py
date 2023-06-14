#!/usr/bin/env python
# coding: utf-8

# In[2]:


#slide 6 Menampilkan diagram
import matplotlib.pyplot as plt

#initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

#plotting the data
plt.plot(x,y)

plt.show()


# In[4]:


#slide 7 Membuat judul diagram + css
import matplotlib.pyplot as plt

#initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

#plotting the data
plt.plot(x,y)

#Adding tittle to the plot
plt.title("Linear graph", fontsize=25, color="green")

plt.show()


# In[5]:


#slide 8 menambahkan label pada garis x,y
import matplotlib.pyplot as plt

#initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

#plotting the data
plt.plot(x,y)

#Adding tittle to the plot
plt.title("Linear graph", fontsize=25, color="green")

#Adding label on the y-axis
plt.ylabel('Y-Axis')

#Adding Label on the x-axis
plt.xlabel('X-Axis')


plt.show()


# In[6]:


#slide 9 Menambahkan Legend
import matplotlib.pyplot as plt

#initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

#plotting the data
plt.plot(x,y)

#Adding tittle to the plot
plt.title("Linear graph", fontsize=25, color="green")

#Adding label on the y-axis
plt.ylabel('Y-Axis')

#Adding Label on the x-axis
plt.xlabel('X-Axis')

#Setting the limit of y-axis
plt.ylim(0, 80)

#Setting the labels of x-axis
plt.xticks(x, labels=["one", "two", "three", "four"])

#Adding legends
plt.legend(["GFG"])

plt.show()


# In[11]:


#slide 10 
#Python program to show pyplot module 
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure

#initializing the data
x = [10, 20, 30, 40] 
y = [20, 25, 35, 55]

# Creating a new figure with width - 5 inches 
# and height = 4 inches 
fig = plt.figure(figsize =(5, 4))

#Creating first axes for the figure 
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Creating second axes for the figure 
ax2 = fig.add_axes ([1, 0.1, 0.8, 0.8])

#Adding the data to be plotted 
ax1.plot(x, y) 
ax2.plot(y, x)

plt.show()


# In[12]:


#slide 11
import matplotlib.pyplot as plt

#initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

#plotting the data
plt.plot(x,y)

#Adding tittle to the plot
plt.title("Linear graph", fontsize=25, color="green")

#Adding label on the y-axis
plt.ylabel('Y-Axis')

#Adding Label on the x-axis
plt.xlabel('X-Axis')

#Setting the limit of y-axis
plt.ylim(0, 80)

#Setting the labels of x-axis
plt.xticks(x, labels=["one", "two", "three", "four"])

#Adding legends
plt.legend(["GFG"])

plt.show()


# In[15]:


#slide 12 Memvisualisasikan data Bank

import pandas as pd

#reading the databases
data = pd.read_csv("data bank.csv")

#printing the top 10 rows
display(data.head(10))


# In[37]:


#slide 13
import pandas as pd
import matplotlib.pyplot as plt

#reading the database
data = pd.read_csv("data bank.csv")

#Scatter plot with day againts tip
plt.scatter(data['age'], data['marital'])

#Adding Title to the Plot
plt.title("Scatter Plot")

#Setting the X and Y labels
plt.xlabel('age')
plt.ylabel('marital')

plt.savefig("Scatter Plot.jpg")
plt.show()


# In[27]:


#slide 14
import pandas as pd
import matplotlib.pyplot as plt

#reading the database
data = pd.read_csv("data bank.csv")

#Scatter plot with day againts tip
plt.scatter(data['age'], data['marital'], c=data['day'], 
            s=data['duration'])

#Adding Title to the Plot
plt.title("Scatter Plot")

#Setting the X and Y labels
plt.xlabel('age')
plt.ylabel('marital')

plt.savefig("Scatter Plot2.jpg")
plt.show()


# In[29]:


#slide 15
import pandas as pd
import matplotlib.pyplot as plt

#reading the database
data = pd.read_csv("data bank.csv")

#Scatter plot with day againts tip
plt.plot(data['age']) 
plt.plot(data['marital'])

#Adding Title to the Plot
plt.title("Scatter Plot")

#Setting the X and Y labels
plt.xlabel('age')
plt.ylabel('marital')

plt.savefig("Line Chart.jpg")
plt.show()


# In[31]:


#slide 16
import pandas as pd
import matplotlib.pyplot as plt

#reading the database
data = pd.read_csv("data bank.csv")

#Scatter plot with day againts tip
plt.bar(data['age'], data['marital'])

#Adding Title to the Plot
plt.title("Bar Chart")

#Setting the X and Y labels
plt.xlabel('age')
plt.ylabel('marital')

plt.savefig("Bar Chart.jpg")
plt.show()


# In[39]:


#slide 17
import pandas as pd
import matplotlib.pyplot as plt

#reading the database
data = pd.read_csv("data bank.csv")

#Histogram
plt.hist(data['duration'])

#Adding Title to the Plot
plt.title("Histogram")

plt.savefig("Histogram.jpg")
plt.show()


# In[38]:


#slide 18
import pandas as pd
import matplotlib.pyplot as plt

#reading the database
data = pd.read_csv("data bank.csv")

#Initiating the data
job = ['admin.', 'services', 'management', 'retired', 'technician']
age = [41, 42, 54, 56, 59]

#plotting the data
plt.pie(age, labels=job)

#adding tittle to the plot
plt.title("Bank Data")

plt.savefig("Pie Chart.jpg")
plt.show()


# In[ ]:




