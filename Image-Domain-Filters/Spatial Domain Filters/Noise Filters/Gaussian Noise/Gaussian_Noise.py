from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2
import math
import os
import random

class Gauss:

    Final_Image = []
    
    def Load_Image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if self.image_path:
            self.Original_image = Image.open(self.image_path).convert("L")
            self.Original_image = self.Original_image.resize((550, 550))
            self.photo = ImageTk.PhotoImage(self.Original_image)
            self.image_display = Label(self.LoadImg_Frame)
            self.image_display.pack()
            self.image_display.config(image=self.photo)

    def Apply_Noise(self,Original_image,sd):
        
        self.Image_BitList = np.array(Original_image)
        height, width = self.Image_BitList.shape[:2]
        self.Kernel = [[0 for c in range(3)] for r in range(3)]
       
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
                        noise = self.Image_BitList[rm+x][cm+y] + random.Gauss(0, 30) * gaussian_value
                        self.Kernel[i][j] = int(noise)
                
                self.Filtered_Bitlist[rm][cm] = self.Kernel[1][1] 

        # print("Output BitList: ")
        # print(self.Filtered_Bitlist)
        return self.Filtered_Bitlist
        
        Final_Image = Image.fromarray(self.Filtered_Bitlist)
        Output_Image = ImageTk.PhotoImage(Final_Image)
        Output_Lbl = tk.Label(self.Generated_Frame, image=Output_Image)
        Output_Lbl.image = Output_Image
        Output_Lbl.pack()
        