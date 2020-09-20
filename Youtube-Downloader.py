#!/usr/bin/env python
# coding: utf-8

# <html>
#     <h1><center>Youtube Dowloader

# ## Importing Required Libraries

# In[4]:


import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from pytube import YouTube
import os


# ## Creating Widgets

# In[6]:


# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    linkLabel = Label(root, text="YOUTUBE LINK  :", bg="cornsilk4")
    linkLabel.grid(row=1, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=55, textvariable=videoLink)
    root.linkText.grid(row=1, column=1, pady=5, padx=5, columnspan = 2)

    destinationLabel = Label(root, text="DESTINATION    :", bg="cornsilk4")
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=38, textvariable=downloadPath)
    root.destinationText.grid(row=2, column=1, pady=5, padx=5)

    browseButton = Button(root, text="BROWSE", command=Browse, width=15)
    browseButton.grid(row=2, column=2, pady=5, padx=5)

    dwldButton = Button(root, text="DOWNLOAD VIDEO", command=Download, width=30)
    dwldButton.grid(row=3, column=1, pady=5, padx=5)


# ## Browse Directory

# In[39]:


# Defining Browse() to select a destination folder to save the audio file
def Browse():
    #os.getcwd is used to get the current directory
    #os.chdir('Set Your Directory')  by this you can change your directory 
    #if we are not providing any directory it automatically download the video in the current directory
    dwldDirectory = filedialog.askdirectory(initialdir=os.getcwd())
    #print(dwldDirectory)
    downloadPath.set(dwldDirectory)


# ## Code To Dowload Video

# In[40]:


# Defining Download() to download the video as audio file
def Download():
    # Fetching the user-input Youtube Link and storing it in yt_link variable
    yt_link = videoLink.get()
    # Fetching the Destination Directory and storing it in dwldFolder variable
    dwldFolder = downloadPath.get()
    #dowloading the video with highest quality
    try:
        #object creation using YouTube which was imported in the beginning
        video= YouTube(yt_link)
    except:
        messagebox.showinfo("Un-Success","Enter The Valid Link")
    youtube=video.streams.first()
    try: 
        #downloading the video 
        youtube.download(dwldFolder)
        messagebox.showinfo("SUCCESS", "VIDEO IS DOWNLOADED ")
    except:
        messagebox.showinfo("Something Went Wrong")
    
    


# ## Creating Required Objects and Calling Functions

# In[38]:


# Creating object of tk class
root = tk.Tk()

# Setting the title, background color and size of the tkinter window and disabling the
# resizing property
root.geometry("650x120")
root.resizable(False, False)
root.title("Youtube Dowloader")
root.config(background="cornsilk4")

# Creating the tkinter Variables
videoLink = StringVar()
downloadPath = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()

