#!/usr/bin/env python
# coding: utf-8

# In[1]:


#these are the packages you'll need, pyfirmata will need to be installed yourself
import pyfirmata as pf
import time
import matplotlib.pyplot as plt


# In[2]:


#this code allows you to update your plot real time
get_ipython().run_line_magic('matplotlib', 'notebook')
plt.rcParams['animation.html'] = 'jshtml'


# In[3]:


#this code creates a board object and tells python where to find the board
#the port will change from user to user
#you can find the address to your port in the lower right side of your arduino IDE
#something like "Arduino Uno on /dev/cu.usbmodem411"
import pyfirmata as pf
from pyfirmata import Arduino
port = 'COM3'
board = pf.Arduino(port) 

#this code is alagous to the sketch you made in the arduino IDE
#analog pins you're using are being initialized, [0] and [1] = pins A0 and A1
board.analog[0].mode = pf.INPUT 
board.analog[1].mode = pf.INPUT

#this is the portion of your code that will iterate continuously on your arduino
#all we need to do is start the loop and read the output from the pins we have initialized
it = pf.util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
board.analog[1].enable_reporting()


# In[4]:


#creating a figure with matplotlib
fig = plt.figure(figsize=(3, 3))
ax = fig.add_subplot()
fig.show()

#initializing our while loop counter and two lists (x and y) to record our data 
i = 0
x, y = [], []

#a file named data_file.txt will be created in the same directory as this notebook
#if you want to run the notebook multiple times without overwriting the file, change the file name
data_file = open('data_file.txt', 'w')
from pyfirmata import Arduino
port = 'COM3'
board = pf.Arduino(port) 

#this while loop is set up to run a fixed number of times, then exit
while i<= 200:
    #pyfirmata scales analog pin signal between 0 and 1 (0-1023 for arduino)
    V_drop = 5*(board.analog[0].read())
    
    #adjusting time_interval will change the interval between data points, units are in seconds
    time_interval = 1
    t = i * time_interval
    
    x.append(t)
    y.append(V_drop)
    
    #plotting our data and drawing it on the plot
    #the x and y axis limits can be changed here
    ax.plot(x, y, color = 'b')
    fig.canvas.draw()
    ax.set_xlim(left=max(0, t-10), right=t)
    ax.set_ylim(0, 5.1)
    
    #writing the data for each iteration, time won't be an integer if your time interval isn't an integer
    data_file.write("%i %f\n" % (t, V_drop))

    i += 1
    
    #time.sleep adds a pause for some number of seconds between each loop iteration
    time.sleep(time_interval) 

#after the while loop exits your data file will be closed
data_file.close()
        
    


# In[ ]:





# In[ ]:





# In[ ]:




