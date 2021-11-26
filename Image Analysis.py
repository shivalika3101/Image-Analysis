#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
from skimage import data , color
from skimage import data, io, filters
from skimage import io
import tkinter
from tkinter import *
from tkinter import filedialog
import PIL
from PIL import ImageTk, Image, ImageFilter, ImageDraw, ImageFont 
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.image as img
from PIL import Image
import numpy as np


def new_window():
    if __name__=="__main__":
        sc = Toplevel(root)
        sc.configure(bg="light blue") 
        sc.title("Image Analysis")  
        sc.geometry("575x400") 
        sc.resizable(width = False, height = False)
    
    
    
    
    def openfilename():
        global filename 
        global img
        filename = filedialog.askopenfilename(title ='Choose the Photo')
        return filename
    
        
    def convert2gray():
        x = openfilename()
        img = Image.open(x)
        imgGray = img.convert('LA')
        img.show()
        imgGray.show()
        


    def flip_h():
        x = openfilename()
        # Open an already existing image
        imageObject = Image.open(x)
        # Do a flip of left and right
        hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
        # Show the horizontal flipped image
        hori_flippedImage.show()
        
                
    def flip_v():     
        x = openfilename()
        # Open an already existing image
        imageObject = Image.open(x)
        # Do a flip of left and right
        hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
        # Show vertically flipped image
        Vert_flippedImage = imageObject.transpose(Image.FLIP_TOP_BOTTOM)
        Vert_flippedImage.show()
        
        
    def flip_90():   
        x = openfilename()
        # Open an already existing image
        imageObject = Image.open(x)
        # Do a flip of left and right
        hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
        #show 90 degree flipped image
        degree_flippedImage = imageObject.transpose(Image.ROTATE_90)
        degree_flippedImage.show()
        
    def prop():
        x = openfilename()
        # opening the image stored in the local path.
        img = Image.open(x)
        print ("Image size: ",img.size)
        print ("Image width: ",img.width)
        print ("Iamge height: ",img.height)
        
    def blur():
        x=openfilename() 
        # opening the image stored in the local path.
        img = Image.open(x)
        # blur the image.
        filtered_img = img.filter(filter = ImageFilter.BLUR)
        filtered_img.show()
        
    def split():
        x=openfilename()
        # opening the image stored in the local path.
        img = Image.open(x)
        img.show()
        

        
        # split the rgb images into r, g, b individual images and merging again.
        r,g,b = img.split()
        #r.title("red")
        draw = ImageDraw.Draw(r)
        draw.text((100, 100),"RED SPLIT")
        
        draw = ImageDraw.Draw(g)
        draw.text((100, 100),"GREEN SPLIT")
        
        draw = ImageDraw.Draw(b)
        draw.text((100, 100),"BLUE SPLIT")
        
        r.show()
        g.show()
        b.show()
     
        u=r
        y=g
        z=b

        # merging
        draw = ImageDraw.Draw(x)
        draw.text((100, 100),"Original")
        im = Image.merge("RGB", (u, y, z))
        im.show()
        
        
    def point():
        x=openfilename()
        # creating a object 
        im = Image.open(x) 
        threshold = 191  
        im = im.point(lambda p: p > threshold and 255)
        im.show()
        
        
        
    def imgonimg():
        try:
            #Relative Path
            #Image on which we want to paste
            x = openfilename()
            img = Image.open(x)
            #Relative Path
            #Image which we want to paste
            x = openfilename()
            img2 = Image.open(x)
            img.paste(img2, (100, 100))
            #Saved in the same relative location
            #img.save("pasted_picture.jpg")
            img.show(img)
        except IOError:
            pass
        

    def outline():
        x = openfilename()
        img = Image.open(x)   
        edges = filters.sobel(img)
        io.imshow(edges)
        io.show()
        
    def cropping():
        try:
            #Relative Path
            x = openfilename()
            img = Image.open(x)
            
            width, height = img.size
            area = (0, 0, width/2, height/2)
            cimg = img.crop(area)
            img.show(img)
            cimg.show(cimg)
        except IOError:
            pass
       
    def histogram():
        try:
            #Relative Path
            x = openfilename()
            img = Image.open(x)
            #Getting histogram of image
            print(img.histogram())
        except IOError:
            pass    
        
    def rchannel():
        x = openfilename()
        img = Image.open(x)
        type(img)
        img_data = np.array(img)
        img_data.shape
        img_data[:1,:1,:]
        img_chn_red = np.zeros(img_data.shape, dtype='uint8')
        img_chn_red[:,:,0] = img_data[:,:,0]
        image_red = Image.fromarray(img_chn_red)
        img.show()
        image_red.show()
        
    def gchannel():
        x = openfilename()
        img = Image.open(x)
        type(img)
        img_data = np.array(img)
        img_data.shape
        img_data[:1,:1,:]
        img_chn_green = np.zeros(img_data.shape, dtype='uint8')
        img_chn_green[:,:,1] = img_data[:,:,1]
        image_green = Image.fromarray(img_chn_green)
        img.show()
        image_green.show()
        
    def bchannel():
        x = openfilename()
        img = Image.open(x)
        type(img)
        img_data = np.array(img)
        img_data.shape
        img_data[:1,:1,:]
        img_chn_blue = np.zeros(img_data.shape, dtype='uint8')
        img_chn_blue[:,:,2] = img_data[:,:,2]
        image_blue = Image.fromarray(img_chn_blue)
        img.show()
        image_blue.show()

    
                                
        
 #BUTTONS       
    
    l1=Label(sc,text="IMAGE ANALYSIS",font='bold',fg='red',bg='pink',justify=CENTER)
    l1.grid(row=0,column=6,columnspan=3)
    
    l2=Label(sc,text="Select an option",font='bold',fg='black',bg='light blue',justify=CENTER)
    l2.grid(row=1,column=6,columnspan=3)
    
    l3=Label(sc,text="for image processing",font='bold',fg='black',bg='light blue',justify=CENTER)
    l3.grid(row=2,column=6,columnspan=3)
    
      
    convert=Button(sc, text="convert to grey",fg='black',bg='white',command=convert2gray,height=2,width=15)
    convert.grid(row=6, column=5)
    
    hflip=Button(sc, text="horizontal flip",fg='black',bg='white',command=flip_h,height=2,width=15)
    hflip.grid(row=6, column=6)
    
    vflip=Button(sc, text="vertical flip",fg='black',bg='white',command=flip_v,height=2,width=15)
    vflip.grid(row=6, column=7)
    
    flip90=Button(sc, text="90 degree flip",fg='black',bg='white',command=flip_90,height=2,width=15)
    flip90.grid(row=6, column=8)
    
    prop=Button(sc, text="properties",fg='black',bg='white',command=prop,height=2,width=8)
    prop.grid(row=7, column=5)
    
    blur=Button(sc, text="blur",fg='black',bg='white',command=blur,height=2,width=8)
    blur.grid(row=7, column=6)
    
    split=Button(sc, text="split",fg='black',bg='white',command=split,height=2,width=8)
    split.grid(row=7, column=7)
    
    point=Button(sc, text="point",fg='black',bg='white',command=point,height=2,width=8)
    point.grid(row=7, column=8)
    
    histogram_pic=Button(sc, text='Histogram',fg='black',bg='white', command=histogram,height=2,width=8)
    histogram_pic.grid(row=7, column=9)
    
    color_split=Button(sc, text='Image on Image',fg='black',bg='white', command=imgonimg,height=2,width=15)
    color_split.grid(row=8, column=6)
    
    outline=Button(sc, text='outline of image', fg='black',bg='white', command=outline, height=2, width=15)
    outline.grid(row=6,column=9)   
    
    crop=Button(sc, text='Cropping Image', fg='black',bg='white', command=cropping, height=2, width=15)
    crop.grid(row=8,column=5)   
    
    red_channel=Button(sc, text='Red channel', fg='black',bg='white', command=rchannel, height=2, width=15)
    red_channel.grid(row=8,column=7)  
    
    green_channel=Button(sc, text='Green channel', fg='black',bg='white', command=gchannel, height=2, width=15)
    green_channel.grid(row=8,column=8)  

    blue_channel=Button(sc, text='Blue channel', fg='black',bg='white', command=bchannel, height=2, width=15)
    blue_channel.grid(row=8,column=9) 

#create original window 
root = Tk()
root.title("Image Analysis")
root.geometry("275x200")
root.configure(bg="light grey")



l4=Label(root,text="IMAGE ANALYSIS IN PYTHON ",font='bold',fg='red',bg='light grey',justify=CENTER)
l4.grid(row=1,column=6,columnspan=3)
    
l5=Label(root,text="Click on bellow given button",fg='purple',bg='light grey',justify=CENTER)
l5.grid(row=2,column=6,columnspan=3)

button =Button(root, text="click here to proceed",fg='red',bg='black',command=lambda: new_window())
button.grid(row=9,column=6,columnspan=3)

l6=Label(root,text="TPDDL-TATA POWER DELHI DISTRIBUTION LIMITED",fg='black',bg='light grey',justify=CENTER)
l6.grid(row=0,column=6)



root.mainloop()


# In[ ]:




