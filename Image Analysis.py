#!/usr/bin/env python

import numpy as np
from skimage import filters, io
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageFilter, ImageDraw


def new_window():
    if __name__=="__main__":
        sc = Toplevel(root)
        sc.configure(bg="#eef4ff")
        sc.title("Image Analysis")  
        sc.geometry("700x430")
        sc.resizable(width = False, height = False)
    
    
    
    
    def openfilename():
        filename = filedialog.askopenfilename(
            title="Choose the Photo",
            filetypes=[
                ("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff"),
                ("All files", "*.*"),
            ],
        )
        return filename
    
        
    def convert2gray():
        x = openfilename()
        if not x:
            return
        img = Image.open(x)
        imgGray = img.convert('LA')
        img.show()
        imgGray.show()
        


    def flip_h():
        x = openfilename()
        if not x:
            return
        # Open an already existing image
        imageObject = Image.open(x)
        # Do a flip of left and right
        hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
        # Show the horizontal flipped image
        hori_flippedImage.show()
        
                
    def flip_v():     
        x = openfilename()
        if not x:
            return
        # Open an already existing image
        imageObject = Image.open(x)
        # Show vertically flipped image
        Vert_flippedImage = imageObject.transpose(Image.FLIP_TOP_BOTTOM)
        Vert_flippedImage.show()
        
        
    def flip_90():   
        x = openfilename()
        if not x:
            return
        # Open an already existing image
        imageObject = Image.open(x)
        #show 90 degree flipped image
        degree_flippedImage = imageObject.transpose(Image.ROTATE_90)
        degree_flippedImage.show()
        
    def prop():
        x = openfilename()
        if not x:
            return
        # opening the image stored in the local path.
        img = Image.open(x)
        print ("Image size: ",img.size)
        print ("Image width: ",img.width)
        print ("Iamge height: ",img.height)
        
    def blur():
        x=openfilename() 
        if not x:
            return
        # opening the image stored in the local path.
        img = Image.open(x)
        # blur the image.
        filtered_img = img.filter(filter = ImageFilter.BLUR)
        filtered_img.show()
        
    def split():
        x=openfilename()
        if not x:
            return
        # opening the image stored in the local path.
        img = Image.open(x).convert("RGB")
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
        merged = Image.merge("RGB", (u, y, z))
        draw = ImageDraw.Draw(merged)
        draw.text((100, 100),"Original")
        merged.show()
        
        
    def point():
        x=openfilename()
        if not x:
            return
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
            if not x:
                return
            img = Image.open(x)
            #Relative Path
            #Image which we want to paste
            x = openfilename()
            if not x:
                return
            img2 = Image.open(x)
            img.paste(img2, (100, 100))
            #Saved in the same relative location
            #img.save("pasted_picture.jpg")
            img.show()
        except IOError:
            pass
        

    def outline():
        x = openfilename()
        if not x:
            return
        img = Image.open(x).convert("L")
        edges = filters.sobel(np.array(img))
        io.imshow(edges)
        io.show()
        
    def cropping():
        try:
            #Relative Path
            x = openfilename()
            if not x:
                return
            img = Image.open(x)
            
            width, height = img.size
            area = (0, 0, width // 2, height // 2)
            cimg = img.crop(area)
            img.show()
            cimg.show()
        except IOError:
            pass
       
    def histogram():
        try:
            #Relative Path
            x = openfilename()
            if not x:
                return
            img = Image.open(x)
            #Getting histogram of image
            print(img.histogram())
        except IOError:
            pass    
        
    def rchannel():
        x = openfilename()
        if not x:
            return
        img = Image.open(x).convert("RGB")
        r, g, b = img.split()
        blank = Image.new("L", img.size, 0)
        image_red = Image.merge("RGB", (r, blank, blank))
        img.show()
        r.show(title="Red Channel Intensity")
        image_red.show()
        
    def gchannel():
        x = openfilename()
        if not x:
            return
        img = Image.open(x).convert("RGB")
        r, g, b = img.split()
        blank = Image.new("L", img.size, 0)
        image_green = Image.merge("RGB", (blank, g, blank))
        img.show()
        g.show(title="Green Channel Intensity")
        image_green.show()
        
    def bchannel():
        x = openfilename()
        if not x:
            return
        img = Image.open(x).convert("RGB")
        r, g, b = img.split()
        blank = Image.new("L", img.size, 0)
        image_blue = Image.merge("RGB", (blank, blank, b))
        img.show()
        b.show(title="Blue Channel Intensity")
        image_blue.show()

    
                                
        
 #BUTTONS       
    
    l1=Label(
        sc,
        text="IMAGE ANALYSIS STUDIO",
        font=("Georgia", 18, "bold"),
        fg="#173b70",
        bg="#dce9ff",
        padx=18,
        pady=10,
        justify=CENTER,
    )
    l1.grid(row=0,column=5,columnspan=5,pady=(18, 8))
    
    l2=Label(
        sc,
        text="Choose an effect or analysis tool",
        font=("Segoe UI", 12, "bold"),
        fg="#243b53",
        bg="#eef4ff",
        justify=CENTER,
    )
    l2.grid(row=1,column=5,columnspan=5)
    
    l3=Label(
        sc,
        text="then pick an image to preview the result",
        font=("Segoe UI", 10),
        fg="#486581",
        bg="#eef4ff",
        justify=CENTER,
    )
    l3.grid(row=2,column=5,columnspan=5,pady=(4, 0))

    helper = Label(
        sc,
        text="Choose a tool below, then pick an image file.",
        font=("Segoe UI", 10),
        fg="#243b53",
        bg="#eef4ff",
        justify=CENTER,
    )
    helper.grid(row=3, column=5, columnspan=5, pady=(10, 20))
    
      
    button_style = {
        "fg": "white",
        "bg": "#2f6fed",
        "activebackground": "#1f4fb1",
        "activeforeground": "white",
        "font": ("Segoe UI", 10, "bold"),
        "relief": FLAT,
        "bd": 0,
        "height": 2,
        "width": 16,
        "cursor": "hand2",
    }

    convert=Button(sc, text="Convert to Grey",command=convert2gray,**button_style)
    convert.grid(row=6, column=5)
    
    hflip=Button(sc, text="Horizontal Flip",command=flip_h,**button_style)
    hflip.grid(row=6, column=6)
    
    vflip=Button(sc, text="Vertical Flip",command=flip_v,**button_style)
    vflip.grid(row=6, column=7)
    
    flip90=Button(sc, text="Rotate 90°",command=flip_90,**button_style)
    flip90.grid(row=6, column=8)
    
    prop=Button(sc, text="Properties",command=prop,**button_style)
    prop.grid(row=7, column=5)
    
    blur=Button(sc, text="Blur",command=blur,**button_style)
    blur.grid(row=7, column=6)
    
    split=Button(sc, text="Split RGB",command=split,**button_style)
    split.grid(row=7, column=7)
    
    point=Button(sc, text="Threshold",command=point,**button_style)
    point.grid(row=7, column=8)
    
    histogram_pic=Button(sc, text='Histogram', command=histogram,**button_style)
    histogram_pic.grid(row=7, column=9)
    
    color_split=Button(sc, text='Image on Image', command=imgonimg,**button_style)
    color_split.grid(row=8, column=6)
    
    outline=Button(sc, text='Outline Image', command=outline,**button_style)
    outline.grid(row=6,column=9)   
    
    crop=Button(sc, text='Crop Image', command=cropping,**button_style)
    crop.grid(row=8,column=5)   
    
    red_channel=Button(sc, text='Red Channel', command=rchannel,**button_style)
    red_channel.grid(row=8,column=7)  
    
    green_channel=Button(sc, text='Green Channel', command=gchannel,**button_style)
    green_channel.grid(row=8,column=8)  

    blue_channel=Button(sc, text='Blue Channel', command=bchannel,**button_style)
    blue_channel.grid(row=8,column=9) 

#create original window 
root = Tk()
root.title("Image Analysis")
root.geometry("380x240")
root.configure(bg="#f5f7fb")



l4=Label(
    root,
    text="Image Analysis",
    font=("Georgia", 20, "bold"),
    fg="#173b70",
    bg="#f5f7fb",
    justify=CENTER,
)
l4.grid(row=1,column=6,columnspan=3,pady=(24, 6))
    
l5=Label(
    root,
    text="Explore simple image effects and analysis tools",
    font=("Segoe UI", 10),
    fg="#486581",
    bg="#f5f7fb",
    justify=CENTER,
)
l5.grid(row=2,column=6,columnspan=3,pady=(0, 18))

button =Button(
    root,
    text="Open Studio",
    fg='white',
    bg='#2f6fed',
    activebackground="#1f4fb1",
    activeforeground="white",
    font=("Segoe UI", 11, "bold"),
    relief=FLAT,
    bd=0,
    padx=20,
    pady=10,
    cursor="hand2",
    command=lambda: new_window(),
)
button.grid(row=9,column=6,columnspan=3)

l6=Label(
    root,
    text="Pick a tool, choose an image, and preview the result",
    font=("Segoe UI", 9),
    fg="#627d98",
    bg="#f5f7fb",
    justify=CENTER,
)
l6.grid(row=10,column=6,columnspan=3,pady=(16, 0))



root.mainloop()
