from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2
import math
import os
import random

class Enhance_Image:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1375x880")
        self.root.title("Image Filter")
        self.image_path = None
        
        title = Label(self.root, text="Image Filter", font=('Arial', 30, 'bold'), pady=2, bd=12, bg="#8A8A8A", fg="Black", relief=GROOVE)
        title.pack(fill=X)
        
        self.LoadImg_Frame = LabelFrame(self.root, text="Load Image", font=('Arial', 15, 'bold'), bd=10, fg="Black", bg="grey")
        self.LoadImg_Frame.place(x=0, y=75, width=625, height=705)
        
        self.Option_Frame = LabelFrame(self.LoadImg_Frame, text="Options", font=('Arial', 15, 'bold'), bd=10, fg="Black", bg="grey")
        self.Option_Frame.place(x=0, y=570, width=605, height=100)
        
        self.load_button = Button(self.Option_Frame, text="Load Image", command=self.Load_Image, bg="#13B10F", bd=2, fg="black", pady=15, width=12, font='arial 13 bold')
        self.load_button.pack(side=LEFT,padx=4)
        
        self.Filter_Btn = Button(self.Option_Frame, text="Apply Filter",command=self.Apply_Noise, state=NORMAL,  bg="red", bd=2, fg="black", pady=15, width=20, font='arial 13 bold')
        self.Filter_Btn.pack(side=LEFT,padx=4)
        
        self.reset = Button(self.Option_Frame, text="Reset", command=self.ResetWindow,  bg="red",fg="black", pady=15, width=12, font='arial 13 bold')
        self.reset.pack(side=RIGHT,padx=60)
        
        self.Generated_Frame = LabelFrame(self.root, text="Output", font=('Arial', 15, 'bold'), bd=10, fg="Black", bg="grey")
        self.Generated_Frame.place(x=625, y=75, width=750, height=705)
        
        self.Bit_Frame = LabelFrame(self.root, text="Parameters", font=('arial', 14, 'bold'), bd=10, bg="grey")
        self.Bit_Frame.place(x=0, y=780, relwidth=1, height=100)
        
        self.Final_Image = []

        # self.LoadVal_Btn = Button(self.Bit_Frame, text="Load Values", command=self.Load_Image,  bg="green",fg="black", pady=15, width=10, font='arial 13 bold')
        # self.LoadVal_Btn.grid(row=0,column=8,padx=10)
            
        E_Lb = Label(self.Bit_Frame, text="E=", font=('arial', 16, 'bold'), bg="grey", fg="black")
        E_Lb.grid(row=0, column=0, padx=2, pady=10, sticky='W')
        self.std = Entry(self.Bit_Frame, width=10,  font=('arial', 16, 'bold'), bd=5, relief=GROOVE)
        self.std.grid(row=0, column=1, padx=0, pady=10)
        
    def Load_Image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if self.image_path:
            self.Original_image = Image.open(self.image_path).convert("L")
            self.Original_image = self.Original_image.resize((550, 550))
            self.photo = ImageTk.PhotoImage(self.Original_image)
            self.image_display = Label(self.LoadImg_Frame)
            self.image_display.pack()
            self.image_display.config(image=self.photo)

    def Apply_Noise(self):
        self.Image_BitList = np.array(self.Original_image)
        height, width = self.Image_BitList.shape[:2]
        self.Kernel = [[0 for c in range(3)] for r in range(3)]
       
        sd = float(self.std.get())
        self.Filtered_Bitlist = self.Image_BitList
        itct = 0

        for rm in range(height):
            for cm in range(width):
                
                self.Kernel.clear()
                self.Kernel = [[0 for rk in range(3)] for ck in range(3)]
                self.Kernel[1][1] = self.Image_BitList[rm][cm]
                

                for i in range(3):
                    for j in range(3):
                        x, y = i-1, j-1
                        if (rm+x) < 0 or (rm+x) >= height or (cm+y) < 0 or (cm+y) >= width:
                            continue
                        gaussian_value = (1/(sd*math.sqrt(np.pi*2)))*(np.exp(-((x**2)+(y**2))/((sd)**2)))
                        noise = self.Image_BitList[rm+x][cm+y] + random.gauss(0, 30) * gaussian_value
                        self.Kernel[i][j] = int(noise)
                
                self.Filtered_Bitlist[rm][cm] = self.Kernel[1][1] 

        print("Output BitList: ")
        print(self.Filtered_Bitlist)
        
        Final_Image = Image.fromarray(self.Filtered_Bitlist)
        Output_Image = ImageTk.PhotoImage(Final_Image)
        Output_Lbl = tk.Label(self.Generated_Frame, image=Output_Image)
        Output_Lbl.image = Output_Image
        Output_Lbl.pack()
        
    def ResetWindow(self):
        root.destroy()
        os.startfile(r"Gaussian.py")

if __name__ == "__main__":
    root = Tk()
    app = Enhance_Image(root)
    root.mainloop()