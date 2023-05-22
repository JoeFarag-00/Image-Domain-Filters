import customtkinter
from customtkinter import CTkImage
import os
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
from PIL import Image, ImageTk
import string
import re
from tkinter import Tk, Label, Text, Button, Menu
import tkinter
import sys
import cv2

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

class MainGUI():
    
    @staticmethod
    def Load_Dynamic_Operations():
        global Original_image
        global image_path
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if image_path:
            Original_image = Image.open(image_path).convert("L")
            Original_image = Original_image.resize((550, 550))
            photo = ImageTk.PhotoImage(Original_image)
            image_display = customtkinter.CTkLabel(LoadImg_Frame,image=photo, text=" ")
            image_display.pack()
            Load_Image_Btn.destroy()
                
            if IsNoise:  
                if Selected == 1:
                    
                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Filter",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Threshold_Lbl = customtkinter.CTkLabel(Main, text="Threshold:", font=("System", 20, "bold"))
                    Threshold_Lbl.place(x=Main.winfo_screenwidth()/2 - 900,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    global Threshold
                    Threshold = customtkinter.CTkEntry(Main, placeholder_text="Thres < 1")
                    Threshold.place(x=Main.winfo_screenwidth()/2 - 780,y=Main.winfo_screenheight()/2 + 180, anchor="center")

                elif Selected == 2:
                    
                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Filter",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Threshold_Lbl = customtkinter.CTkLabel(Main, text="Enter SD: ", font=("System", 20, "bold"))
                    Threshold_Lbl.place(x=Main.winfo_screenwidth()/2 - 900,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    global Sd_Value 
                    Sd_Value = customtkinter.CTkEntry(Main, placeholder_text="Enter SD")
                    Sd_Value.place(x=Main.winfo_screenwidth()/2 - 770,y=Main.winfo_screenheight()/2 + 180, anchor="center")

                elif Selected == 3:
                    
                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Filter",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Threshold_Lbl = customtkinter.CTkLabel(Main, text="Range Min:", font=("System", 20, "bold"))
                    Threshold_Lbl.place(x=Main.winfo_screenwidth()/2 - 900,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    RangeB_Lbl = customtkinter.CTkLabel(Main, text="Range Max:", font=("System", 20, "bold"))
                    RangeB_Lbl.place(x=Main.winfo_screenwidth()/2 - 660,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    global ErangeA ,ErangeB 
                    ErangeA = customtkinter.CTkEntry(Main, placeholder_text="Min")
                    ErangeA.place(x=Main.winfo_screenwidth()/2 - 780,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    ErangeB = customtkinter.CTkEntry(Main, placeholder_text="Max")
                    ErangeB.place(x=Main.winfo_screenwidth()/2 - 540,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
            elif IsSharpen:  
                if Selected == 1:

                    global IWhichKernel
                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Filter",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Kernel_Lbl = customtkinter.CTkLabel(Main, text="Kernel: ", font=("System", 20, "bold"))
                    Kernel_Lbl.place(x=Main.winfo_screenwidth()/2 - 900,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    IWhichKernel = customtkinter.CTkEntry(Main, placeholder_text="1 - 4")
                    IWhichKernel.place(x=Main.winfo_screenwidth()/2 - 780,y=Main.winfo_screenheight()/2 + 180, anchor="center")

                elif Selected == 2:
                    
                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Filter",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    umhf_Lbl = customtkinter.CTkLabel(Main, text="K: ", font=("System", 20, "bold"))
                    umhf_Lbl.place(x=Main.winfo_screenwidth()/2 - 900,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    global K_val 
                    K_val = customtkinter.CTkEntry(Main, placeholder_text="K >= 0 ")
                    K_val.place(x=Main.winfo_screenwidth()/2 - 800,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                
                elif Selected == 3:

                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Filter",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                elif Selected == 4:
                    
                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Filter",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Sd_Lbl = customtkinter.CTkLabel(Main, text="SD: ", font=("System", 20, "bold"))
                    Sd_Lbl.place(x=Main.winfo_screenwidth()/2 - 900,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    global StandG
                    StandG = customtkinter.CTkEntry(Main, placeholder_text="SD")
                    StandG.place(x=Main.winfo_screenwidth()/2 - 780,y=Main.winfo_screenheight()/2 + 180, anchor="center")
    
            elif IsSmoos:  
                
                if Selected == 2:

                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Filter",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                elif Selected == 3:

                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Filter",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")
        
                elif Selected == 1:

                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Filter",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Median_Lbl = customtkinter.CTkLabel(Main, text="Median Filter ", font=("System", 20, "bold"))
                    Median_Lbl.place(x=Main.winfo_screenwidth()/2 - 900,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                
                elif Selected == 4:

                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Filter",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")
            
            elif IsTrans:
                if Trans == 1:
                    
                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Filter",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")

                elif Trans == 2:
                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Filter",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")

                elif Trans == 3:
                    # MainGUI.Draw_Special_Room()
                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Filter",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")

                elif Trans == 4:
                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Interpolation",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Kfactorlb = customtkinter.CTkLabel(Main, text="Scale: ", font=("System", 20, "bold"))
                    Kfactorlb.place(x=Main.winfo_screenwidth()/2 - 900,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    global Kfactor
                    Kfactor = customtkinter.CTkEntry(Main, placeholder_text="K Factor")
                    Kfactor.place(x=Main.winfo_screenwidth()/2 - 780,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                
                elif Trans == 5:

                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Interpolation",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Kfactorlb = customtkinter.CTkLabel(Main, text="Scale: ", font=("System", 20, "bold"))
                    Kfactorlb.place(x=Main.winfo_screenwidth()/2 - 900,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    global BiLinearscale
                    BiLinearscale = customtkinter.CTkEntry(Main, placeholder_text="Scale: ")
                    BiLinearscale.place(x=Main.winfo_screenwidth()/2 - 780,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                elif Trans == 6:
                    Apply_Filter_Button = customtkinter.CTkButton(Main, text="Apply Interpolation",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Operate_Filter())    
                    Apply_Filter_Button.place(x=Main.winfo_screenwidth()/2 - 40 ,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Reset_Btn = customtkinter.CTkButton(Main, text="RESET",width=100, height=62, font=("System", 30, "bold"), fg_color="darkred", command=lambda:MainGUI.ResetWindow())
                    Reset_Btn.place(x=Main.winfo_screenwidth()/2 + 150,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    Kfactorlb = customtkinter.CTkLabel(Main, text="Scale: ", font=("System", 20, "bold"))
                    Kfactorlb.place(x=Main.winfo_screenwidth()/2 - 900,y=Main.winfo_screenheight()/2 + 180, anchor="center")
                    
                    global BiCubicscale
                    BiCubicscale = customtkinter.CTkEntry(Main, placeholder_text="Scale: ")
                    BiCubicscale.place(x=Main.winfo_screenwidth()/2 - 780,y=Main.winfo_screenheight()/2 + 180, anchor="center")

    def Operate_Filter():
        global Output_Image_Lbl
        global Special_Fourier_Lbl
        
        if IsTrans:
            if Trans == 1:
                sys.path.append('Image-Domain-Filters/Transform & Frequency Domain Filters/Histogram Equalization')
                from Histogram_Equalization import Histo_Equa
                Do_Histo_Equa = Histo_Equa()
                # Input_Image = np.array(Original_image)
                Do_Histo_Equa.Histogram_Equalization(image_path)
                Output_image = Do_Histo_Equa.Histogram_Equalization(image_path)
                print("\nHistogram_Equalization:\n",Output_image)
                
                Final_Image = Image.fromarray(Output_image)
                Final_Image = Final_Image.resize((550, 550))
                Output_Image = ImageTk.PhotoImage(Final_Image)
                Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()
                
            elif Trans == 2:
                sys.path.append('Image-Domain-Filters/Transform & Frequency Domain Filters/Histogram Matching')
                from Histogram_Matching import Histo_Match
                Do_Histo_Spec = Histo_Match()   
                # Input_Image = np.array(Original_image)
                # Do_Histo_Match.histogram_specification()
                Do_Histo_Spec.histogram_specification(image_path)
                Output_image = Do_Histo_Spec.histogram_specification(image_path)
                print("\nHistogram_Equalization:\n",Output_image)
                
                Final_Image = Image.fromarray(Output_image)
                Final_Image = Final_Image.resize((550, 550))
                Output_Image = ImageTk.PhotoImage(Final_Image)
                Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()
            
            elif Trans == 3:
                sys.path.append('Image-Domain-Filters/Transform & Frequency Domain Filters/Fourier Transformation')
                from Fourier_Transform import Fourier
                Do_Fourier = Fourier()
                
                Fourier_Img = Do_Fourier.Shift(image_path)
                print("\nFourier Image:\n",Fourier_Img)
                Fourier_Img = np.array(Fourier_Img)
                Final_Image = Image.fromarray(Fourier_Img)
                # Final_Image = Final_Image.resize((550, 550))
                Output_Image = ImageTk.PhotoImage(Final_Image)
                Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()
                
                Inverse_Img = Do_Fourier.Inverse_Fourier(image_path)
                print("\nInverse Image:\n",Inverse_Img)
                
                Final_Image_Inverse = Image.fromarray(Inverse_Img)
                # Final_Image_Inverse = Final_Image.resize((550, 550))
                Output_Image = ImageTk.PhotoImage(Final_Image_Inverse)
                Output_Image_Lbl = customtkinter.CTkLabel(Inverse_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()
                Do_Fourier.Show_Image()
                
            elif Trans == 4:
                sys.path.append('Image-Domain-Filters/Transform & Frequency Domain Filters/Interpolation')
                from Interpolation import Interpolate
                Do_Interpolate = Interpolate()
                Input_Image = np.array(Original_image)
                scalefactor = float(Kfactor.get())
                Scaled_Image = Do_Interpolate.nearest_neighbor_interpolation(scalefactor,Input_Image)
                print("\nLinear Interpolation:\n",Scaled_Image)

                Final_Image = Image.fromarray(Scaled_Image)
                # Final_Image = Final_Image.resize((550, 550))
                Final_Image = np.array(Final_Image)
                cv2.imshow( "Linear Interpolation", Final_Image)
                Output_Image = ImageTk.PhotoImage(Final_Image)
                Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()
            
            elif Trans == 5:
                sys.path.append('Image-Domain-Filters/Transform & Frequency Domain Filters/Interpolation')
                from Interpolation import Interpolate
                Do_Interpolate = Interpolate()
                Input_Image = np.array(Original_image)
                scalefactor = float(BiLinearscale.get())
                Scaled_Image = Do_Interpolate.bilinear_interpolation(scalefactor,Input_Image)
                print("\Bilinear Interpolation:\n",Scaled_Image)
                
                Final_Image = Image.fromarray(Scaled_Image)
                Final_Image = np.array(Final_Image)
                cv2.imshow( "Bilinear Interpolation", Final_Image)
                # Final_Image = Final_Image.resize((250, 250))
                Output_Image = ImageTk.PhotoImage(Final_Image)
                Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()
            
            elif Trans == 6:
                sys.path.append('Image-Domain-Filters/Transform & Frequency Domain Filters/Interpolation')
                from Interpolation import Interpolate
                Do_Interpolate = Interpolate()
                Input_Image = np.array(Original_image)
                scalefactor = float(BiCubicscale.get())
                Scaled_Image = Do_Interpolate.bicubic_interpolation(scalefactor,Input_Image)
                # Input_Image = np.array(Original_image)
                # Do_Histo_Match.histogram_specification()
                print("\BiCubic Interpolation:\n",Scaled_Image)
                
                Final_Image = Image.fromarray(Scaled_Image)
                Final_Image = np.array(Final_Image)
                cv2.imshow( "BiCubic Interpolation", Final_Image)
                # Final_Image = Final_Image.resize((250, 250))
                
                Output_Image = ImageTk.PhotoImage(Final_Image)
                Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()

        if IsSmoos:
            if Selected == 1:

                sys.path.append('Image-Domain-Filters/Spatial Domain Filters/Smoothing Filter/Median Filter')
                from Median_Filter import PadImageWithZeros,ApplyMedianFilter
                
                Input_Image = np.array(Original_image)
                Do_Median_Smoos = PadImageWithZeros(Input_Image)
                Ouput_Image = ApplyMedianFilter(Do_Median_Smoos)
                print("\nMedian Filter\n",Ouput_Image)
                
                Final_Image = Image.fromarray(Ouput_Image)
                Final_Image = Final_Image.resize((550, 550))
                Output_Image = ImageTk.PhotoImage(Final_Image)
                Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()
                
            elif Selected == 2:
                    
                sys.path.append('Image-Domain-Filters/Spatial Domain Filters/Smoothing Filter/Adaptive Median Filter/')
                from Adaptive_Median_Filter import PadImageWithZeros,ApplyAdaptiveMedianFilter
                
                Input_Image = np.array(Original_image)
                Do_Adpt_Smoos = PadImageWithZeros(Input_Image)
                Ouput_Image = ApplyAdaptiveMedianFilter(Do_Adpt_Smoos, 7)
                print("\nAdaptive Filter:\n",Ouput_Image)
                
                Final_Image = Image.fromarray(Ouput_Image)
                Final_Image = Final_Image.resize((550, 550))
                Output_Image = ImageTk.PhotoImage(Final_Image)
                Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()     
                
            elif Selected == 3:
                    
                sys.path.append('Image-Domain-Filters/Spatial Domain Filters/Smoothing Filter/Averaging Filter')
                from Averaging_Filter import PadImageWithZeros,ApplyAveragingFilter
                
                Input_Image = np.array(Original_image)
                Do_Avg_Smoos = PadImageWithZeros(Input_Image)
                Ouput_Image = ApplyAveragingFilter(Do_Avg_Smoos)
                print("\nAveraging Filter:\n",Ouput_Image)
                
                Final_Image = Image.fromarray(Ouput_Image)
                Final_Image = Final_Image.resize((550, 550))
                Output_Image = ImageTk.PhotoImage(Final_Image)
                Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()
            
            elif Selected == 4:
                
                sys.path.append('Image-Domain-Filters/Spatial Domain Filters/Smoothing Filter/Gaussian Filter (Ahmed)')
                from Gaussian_Filter import ApplyGaussianFilter

                Input_Image = np.array(Original_image)
                Ouput_Image = ApplyGaussianFilter(Input_Image)
                print("\nGaussian Filter\n",Ouput_Image)
                
                Final_Image = Image.fromarray(Ouput_Image)
                Final_Image = Final_Image.resize((550, 550))
                Output_Image = ImageTk.PhotoImage(Final_Image)
                Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()
      
        if IsNoise:
            if Selected == 1:
                Thres = Threshold.get()
                Thres = float(Thres)
                sys.path.append('Image-Domain-Filters/Spatial Domain Filters/Noise Filters/impulse_noise (salt and pepper)/')
                from Impulse_Noise import Impulse
                Do_Impulse_Noise = Impulse()
                Input_Image = np.array(Original_image)
                Ouput_Image = Do_Impulse_Noise.generate_salt_and_pepper_noise(Input_Image,Thres)
                print("\nImpulse Noise:\n",Ouput_Image)
                
                Final_Image = Image.fromarray(Ouput_Image)
                Final_Image = Final_Image.resize((550, 550))
                Output_Image = ImageTk.PhotoImage(Final_Image)
                Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()
                
            elif Selected == 2:
                sd = Sd_Value.get()
                sd = float(sd)
                sys.path.append('Image-Domain-Filters/Spatial Domain Filters/Noise Filters/Gaussian Noise/')
                from Gaussian_Noise import Gauss
                Do_Gaussian_Noise = Gauss()
                Ouput_Image = Do_Gaussian_Noise.Apply_Noise(Original_image,sd)
                print("\nGaussian Noise:\n ",Ouput_Image)
                
                Final_Image = Image.fromarray(Ouput_Image)
                Final_Image = Final_Image.resize((550, 550))
                Output_Image = ImageTk.PhotoImage(Final_Image)
                Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()
                
            elif Selected == 3:
                RangeA = ErangeA.get()
                RangeB = ErangeB.get()
                
                RangeA = float(RangeA)
                RangeB = float(RangeB)
                
                sys.path.append('Image-Domain-Filters/Spatial Domain Filters/Noise Filters/Uniform Noise')
                from Uniform_Noise import Uniform
                Do_Uniform_Noise = Uniform()
                Ouput_Image = Do_Uniform_Noise.Apply_Noise(Original_image,RangeA,RangeB)
                print("\nUniform Noise:\n",Ouput_Image)
                
                Final_Image = Image.fromarray(Ouput_Image)
                Final_Image = Final_Image.resize((550, 550))
                Output_Image = ImageTk.PhotoImage(Final_Image)
                Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()
        
        elif IsSharpen:
            if Selected == 1:
                kernelct = int(IWhichKernel.get())
                if kernelct <= 4:
                # kernelct = int(IWhichKernel)
                    sys.path.append('Image-Domain-Filters/Spatial Domain Filters/Sharpening Spatial Filters/Laplacian Operator Filter/')
                    from Laplacian_Operator_Filter import PadImageWithZeros, ApplyLaplacianOperatorFilter
                    Input_Image = np.array(Original_image)
                    Padded_Image = PadImageWithZeros(Input_Image)
                    Output_Image = ApplyLaplacianOperatorFilter(Padded_Image,kernelct)
                    print("\nLaplacian Filter: \n",Output_Image)
                    
                    Final_Image = Image.fromarray(Output_Image)
                    Final_Image = Final_Image.resize((550, 550))
                    Output_Image = ImageTk.PhotoImage(Final_Image)
                    Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                    Output_Image_Lbl.pack()
                    
                else:
                    
                    print("\nERROR: KERNEL VALUE INCORRECT...[1-4]")
            
            elif Selected == 2:
               
                if umhf == 1:
                    K = int(K_val.get())
                    if  K>=0:
                        sys.path.append('Image-Domain-Filters/Spatial Domain Filters/Sharpening Spatial Filters/UMHF Gaussian Filter/')
                        from Umhf_Gaussian_Filter import ApplyUnsharpMaskingAndHighboostFilteringGauss
                        Input_Image = np.array(Original_image)
                        Do_umhf_Gauss = ApplyUnsharpMaskingAndHighboostFilteringGauss(Input_Image, K)
                        Ouput_Image = Do_umhf_Gauss
                        print("\nUmhf_Gaussian_Filter: \n ",Ouput_Image)
                        
                        Final_Image = Image.fromarray(Ouput_Image)
                        Final_Image = Final_Image.resize((550, 550))
                        Output_Image = ImageTk.PhotoImage(Final_Image)
                        Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                        Output_Image_Lbl.pack()
                    else:
                        Final_Image = Image.fromarray(Ouput_Image)
                        Final_Image = Final_Image.resize((550, 550))
                        Output_Image = ImageTk.PhotoImage(Final_Image)
                        Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                        Output_Image_Lbl.pack()
                        
                elif umhf == 2:
                    
                    K = int(K_val.get())
                    if  K>=0:
                        sys.path.append('Image-Domain-Filters/Spatial Domain Filters/Sharpening Spatial Filters/UMHF Median Filter/')
                        from Umhf_Median_Filter import ApplyUnsharpMaskingAndHighboostFilteringMedian
                        Input_Image = np.array(Original_image)
                        Do_umhf_Gauss = ApplyUnsharpMaskingAndHighboostFilteringMedian(Input_Image, K)
                        Ouput_Image = Do_umhf_Gauss
                        print("\nUmhf_Median_Filter: \n ",Ouput_Image)
                    
                        Final_Image = Image.fromarray(Ouput_Image)
                        Final_Image = Final_Image.resize((550, 550))
                        Output_Image = ImageTk.PhotoImage(Final_Image)
                        Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                        Output_Image_Lbl.pack()
                    else:
                        Final_Image = Image.fromarray(Ouput_Image)
                        Final_Image = Final_Image.resize((550, 550))
                        Output_Image = ImageTk.PhotoImage(Final_Image)
                        Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                        Output_Image_Lbl.pack()

            elif Selected == 3:
                # robertget = robertb.get()
                # robertget = int(robertget)
                sys.path.append('Image-Domain-Filters/Spatial Domain Filters/Sharpening Spatial Filters/Roberts Cross Gradient Operators Filter/')
                from Roberts_Cross_Gradient_Operators_Filter import ApplyRobertsCrossGradientOperatorsFilter
                Input_Image = np.array(Original_image)
                Do_Roberts_Filter = ApplyRobertsCrossGradientOperatorsFilter(Input_Image)
                print("\nUniform Noise:\n",Do_Roberts_Filter)
                
                Final_Image = Image.fromarray(Do_Roberts_Filter)
                Final_Image = Final_Image.resize((550, 550))
                Output_Image = ImageTk.PhotoImage(Final_Image)
                Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()
            
            elif Selected == 4:
                SDg = float(StandG.get())
                sys.path.append('Image-Domain-Filters/Spatial Domain Filters/Sharpening Spatial Filters/Sobel Operators')
                from Sobel import SobelME
                Do_Sobel_Filter = SobelME()
                Input_Image = np.array(Original_image)
                Output_Image = Do_Sobel_Filter.Apply_Noise(Input_Image, SDg)
                print("\nUniform Noise:\n",Output_Image)
                
                Final_Image = Image.fromarray(Output_Image)
                Final_Image = Final_Image.resize((550, 550))
                Output_Image = ImageTk.PhotoImage(Final_Image)
                Output_Image_Lbl = customtkinter.CTkLabel(Final_Image_Frame,image=Output_Image, text=" ")
                Output_Image_Lbl.pack()
                

    def Draw_Operation_Room():
        global Back_Button
        global LoadImg_Frame
        global Load_Image_Btn
        global Final_Image_Frame
        global Inverse_Image_Frame
        if Choosen != "Fourier Transform":
            MainGUI.DestroyAll()
            Main.geometry("1200x775".format(ScreenWidth, ScreenHeight))
            Filter_Page_Label = customtkinter.CTkLabel(Main, text=Choosen, font=("System", 40, "bold"))
            Filter_Page_Label.place(x=ScreenWidth/2-350, y=ScreenHeight/2 - 500, anchor="center")

            Back_Button = customtkinter.CTkButton(Main, text="<- Back",width=80, height=32, font=("System", 20, "bold"), fg_color="DarkRed", command=lambda:MainGUI.GoBack_ChooseSameType())        
            Back_Button.place(x=Main.winfo_screenwidth()/2 - 880,y=Main.winfo_screenheight()/2 - 490, anchor="center")

            LoadImg_Frame = customtkinter.CTkFrame(Main, width=550, height=550)
            LoadImg_Frame.place(x=20, y=90)

            Final_Image_Frame = customtkinter.CTkFrame(Main, width=550, height=550)
            Final_Image_Frame.place(x=630, y=90)

            Load_Image_Btn = customtkinter.CTkButton(Main, text="Load Image",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Load_Dynamic_Operations())        
            Load_Image_Btn.place(x=Main.winfo_screenwidth()/2 - 675,y=Main.winfo_screenheight()/2 + 180, anchor="center")
        else:
            MainGUI.DestroyAll()
            Main.geometry("1750x775".format(ScreenWidth, ScreenHeight))
            Filter_Page_Label = customtkinter.CTkLabel(Main, text=Choosen, font=("System", 40, "bold"))
            Filter_Page_Label.place(x=ScreenWidth/2 - 70, y=ScreenHeight/2 - 500, anchor="center")
            
            Back_Button = customtkinter.CTkButton(Main, text="<- Back",width=80, height=32, font=("System", 20, "bold"), fg_color="DarkRed", command=lambda:MainGUI.GoBack_ChooseSameType())        
            Back_Button.place(x=Main.winfo_screenwidth()/2 - 880,y=Main.winfo_screenheight()/2 - 490, anchor="center")

            LoadImg_Frame = customtkinter.CTkFrame(Main, width=550, height=550)
            LoadImg_Frame.place(x=20, y=90)

            Final_Image_Frame = customtkinter.CTkFrame(Main, width=550, height=550)
            Final_Image_Frame.place(x=600, y=90)

            Inverse_Image_Frame = customtkinter.CTkFrame(Main, width=550, height=550)
            Inverse_Image_Frame.place(x=1180, y=90)

            Load_Image_Btn = customtkinter.CTkButton(Main, text="Load Image",width=200, height=62, font=("System", 30, "bold"), fg_color="darkgreen", command=lambda:MainGUI.Load_Dynamic_Operations())        
            Load_Image_Btn.place(x=Main.winfo_screenwidth()/2 - 675,y=Main.winfo_screenheight()/2 + 180, anchor="center")

            
   
    def DestroyAll():
        widgets = Main.winfo_children()
        # print(widgets)
        for widget in widgets:
            # if hasattr(widget, 'delete'):
            #     widget.delete(0, 'end')
            # elif hasattr(widget, 'destroy'):
            widget.destroy()
                
    def Start_Page_Continue():
        MainGUI.DestroyAll()
        MainGUI.Choose_Domain()
    
    def ResetWindow():
        MainGUI.DestroyAll()
        MainGUI.Draw_Operation_Room()
    
    def GoBack_ChooseSameType():
        MainGUI.DestroyAll()
        ScreenWidth = Main.winfo_screenwidth()
        ScreenHeight = Main.winfo_screenheight()
        Main.geometry("1000x580".format(ScreenWidth, ScreenHeight))
        
        if IsNoise:
            MainGUI.Noise_Filters_Page()
        elif IsSharpen:
            MainGUI.Sharpening_Filters_Page()
        elif IsSmoos:
            MainGUI.Smoothing_Filters_Page()
        elif IsTrans:
            MainGUI.TransFreq_Domain_Page()
            
        # Main.destroy()
        # os.startfile(r"MainGUI.py")
    
    def GoBack_ChooseDifferentFilter():
        MainGUI.DestroyAll()
        
        ScreenWidth = Main.winfo_screenwidth()
        ScreenHeight = Main.winfo_screenheight()
        Main.geometry("1000x580".format(ScreenWidth, ScreenHeight))
        
        if IsSpacial:
            MainGUI.Spatial_Domain_Page()
        elif IsTrans:
            MainGUI.TransFreq_Domain_Page()
        # Main.destroy()
        # os.startfile(r"MainGUI.py")
        
    def TransFreq_Confirmation():
        global Choosen
        global Trans
        global Selected
        global IsNoise
        global IsSharpen
        global IsSmoos
        global IsTrans
        global BTrans

        IsTrans = True
        IsNoise = False
        IsSharpen = False
        IsSmoos = False
        
        Selected = 0
        Choosen = TransFreq_Filters_ComboBox.get()

        if TransFreq_Filters_ComboBox.get():
            TransFreq_Type = TransFreq_Filters_ComboBox.get()

            if TransFreq_Type == "Histogram Equalization":
                Trans = 1
                IsTrans = True
                Choosen = TransFreq_Type
                MainGUI.Draw_Operation_Room()

            elif TransFreq_Type == "Histogram Specification":
                Trans = 2
                IsTrans = True
                Choosen = TransFreq_Type
                MainGUI.Draw_Operation_Room()
                
            elif TransFreq_Type == "Fourier Transform":
                Trans = 3
                IsTrans = True
                Choosen = TransFreq_Type
                MainGUI.Draw_Operation_Room()
                
            elif TransFreq_Type == "Linear Interpolation":
                Trans = 4
                IsTrans = True
                Choosen = TransFreq_Type
                MainGUI.Draw_Operation_Room()

            elif TransFreq_Type == "Bicubic Interpolation":
                Trans = 6
                IsTrans = True
                Choosen = TransFreq_Type
                MainGUI.Draw_Operation_Room()
                
            elif TransFreq_Type == "Bilinear Interpolation":
                Trans = 5
                IsTrans = True
                Choosen = TransFreq_Type
                MainGUI.Draw_Operation_Room()
           
            # MainGUI.Draw_Operation_Room()

    def Spatial_Confirmation():
        global Selected
        global Choosen
        global umhf
        global Trans
        global IsSpacial
        global IsTrans
        IsTrans = False
        IsSpacial = True
        Trans = 0
        
        if IsSmoos:
            if Spatial_Smoothing_Filter_ComboBox.get():
                Smoothing_Type = Spatial_Smoothing_Filter_ComboBox.get()
                
                if Smoothing_Type == "Median Filter":
                    Selected = 1
                    Choosen = Smoothing_Type
                    MainGUI.Draw_Operation_Room()

                elif Smoothing_Type == "Adaptive Filter":
                    Selected = 2
                    Choosen = Smoothing_Type
                    MainGUI.Draw_Operation_Room()
                    
                elif Smoothing_Type == "Averaging Filter":
                    Selected = 3
                    Choosen = Smoothing_Type
                    MainGUI.Draw_Operation_Room()
                    
                elif Smoothing_Type == "Gaussian Filter":
                    Selected = 4
                    Choosen = Smoothing_Type
                    MainGUI.Draw_Operation_Room()
        
        if IsSharpen:        
            if Spatial_Sharpening_Filter_ComboBox.get():
                Sharpen_Type = Spatial_Sharpening_Filter_ComboBox.get()
                
                if Sharpen_Type == "Laplacian Operator":
                    Selected = 1
                    Choosen = Sharpen_Type
                    MainGUI.Draw_Operation_Room()
                    
                elif Sharpen_Type == "Unsharp Masking & Highboost Gaussian":
                    Selected = 2
                    Choosen = Sharpen_Type
                    umhf = 1
                    MainGUI.Draw_Operation_Room()
                
                elif Sharpen_Type == "Unsharp Masking & Highboost Median":
                    Selected = 2
                    Choosen = Sharpen_Type
                    umhf = 2
                    MainGUI.Draw_Operation_Room()
                    
                elif Sharpen_Type == "Roberts Cross-Gradient":
                    Selected = 3
                    Choosen = Sharpen_Type
                    MainGUI.Draw_Operation_Room()
                    
                elif Sharpen_Type == "Sobel Operators":
                    Selected = 4
                    Choosen = Sharpen_Type
                    MainGUI.Draw_Operation_Room()
        
        if IsNoise:     
            if Spatial_Noise_Filter_ComboBox.get():
                Noise_Type = Spatial_Noise_Filter_ComboBox.get()
                
                if Noise_Type == "Impulse Noise":
                    Selected = 1
                    Choosen = Noise_Type
                    MainGUI.Draw_Operation_Room()
                    
                elif Noise_Type == "Gaussian Noise":
                    Selected = 2
                    Choosen = Noise_Type
                    MainGUI.Draw_Operation_Room()
        
                elif Noise_Type == "Uniform Noise":
                    Selected = 3
                    Choosen = Noise_Type
                    MainGUI.Draw_Operation_Room()
                
    def Smoothing_Filters_Page():
        MainGUI.DestroyAll()
        global IsSmoos
        global IsSharpen
        global IsNoise
        IsSmoos = True
        IsSharpen = False
        IsNoise = False
        
        global IsSpacial
        IsSpacial = True
        
        Smoothing_Types = ["...", "Median Filter", "Adaptive Filter", "Averaging Filter", "Gaussian Filter"]
        
        ChooseButtonLabel = customtkinter.CTkLabel(Main, text="Choose A Smoothing Filter", font=("System", 40, "bold"))
        global Spatial_Smoothing_Filter_ComboBox
        
        Spatial_Smoothing_Filter_ComboBox = customtkinter.CTkComboBox(Main, values=Smoothing_Types, width=400, height=55, font=("System", 30, "bold"))
        
        Back_Button = customtkinter.CTkButton(Main, text="<- Back",width=80, height=32, font=("System", 20, "bold"), fg_color="DarkRed", command=lambda:MainGUI.GoBack_ChooseDifferentFilter())        
        Back_Button.place(x=Main.winfo_screenwidth()/2 - 880,y=Main.winfo_screenheight()/2 - 490, anchor="center")

        ConfirmButton = customtkinter.CTkButton(Main, text="Confirm", command=lambda: MainGUI.Spatial_Confirmation(), width=100, height=50, font=("System", 30, "bold"), fg_color="darkgreen")
        QuitButton = customtkinter.CTkButton(Main, text="Quit", command=quit, width=100, height=50, font=("System", 30, "bold"), fg_color="darkgreen")
        
        ChooseButtonLabel.place(x=Main.winfo_screenwidth()/2 - 450,y=Main.winfo_screenheight()/2 - 400, anchor="center")
        Spatial_Smoothing_Filter_ComboBox.place(x=Main.winfo_screenwidth()/2 - 520, y=Main.winfo_screenheight()/2 - 250, anchor="center")
        ConfirmButton.place(x=Main.winfo_screenwidth()/2 - 220, y=Main.winfo_screenheight() /2 - 250, anchor="center")
        QuitButton.place(x=Main.winfo_screenwidth()/2 - 120,y=Main.winfo_screenheight() / 2 - 50, anchor="center")
    
    def Sharpening_Filters_Page():
        MainGUI.DestroyAll()
        global IsSmoos
        global IsSharpen
        global IsNoise
        IsSmoos = False
        IsSharpen = True
        IsNoise = False
        
        Sharpening_Types = ["...", "Laplacian Operator", "Unsharp Masking & Highboost Gaussian","Unsharp Masking & Highboost Median", "Roberts Cross-Gradient", "Sobel Operators"]
        ChooseButtonLabel = customtkinter.CTkLabel(Main, text="Choose A Sharpening Filter", font=("System", 40, "bold"))
        global Spatial_Sharpening_Filter_ComboBox
        Spatial_Sharpening_Filter_ComboBox = customtkinter.CTkComboBox(Main, values=Sharpening_Types, width=400, height=55, font=("System", 30, "bold"))
        
        global IsSpacial
        IsSpacial = True
        Back_Button = customtkinter.CTkButton(Main, text="<- Back",width=80, height=32, font=("System", 20, "bold"), fg_color="DarkRed", command=lambda:MainGUI.GoBack_ChooseDifferentFilter())        
        Back_Button.place(x=Main.winfo_screenwidth()/2 - 880,y=Main.winfo_screenheight()/2 - 490, anchor="center")

        ConfirmButton = customtkinter.CTkButton(Main, text="Confirm", command=lambda: MainGUI.Spatial_Confirmation(), width=100, height=50, font=("System", 30, "bold"), fg_color="darkgreen")
        QuitButton = customtkinter.CTkButton(Main, text="Quit", command=quit, width=100, height=50, font=("System", 30, "bold"), fg_color="darkgreen")
        
        ChooseButtonLabel.place(x=Main.winfo_screenwidth()/2 - 450,y=Main.winfo_screenheight()/2 - 400, anchor="center")
        Spatial_Sharpening_Filter_ComboBox.place(x=Main.winfo_screenwidth()/2 - 520, y=Main.winfo_screenheight()/2 - 250, anchor="center")
        ConfirmButton.place(x=Main.winfo_screenwidth()/2 - 220, y=Main.winfo_screenheight() /2 - 250, anchor="center")
        QuitButton.place(x=Main.winfo_screenwidth()/2 - 120,y=Main.winfo_screenheight() / 2 - 50, anchor="center")
        
    def Noise_Filters_Page():
        MainGUI.DestroyAll()
        global IsNoise
        global IsSmoos
        global IsSharpen
        IsNoise = True
        IsSmoos = False
        IsSharpen = False
        
        Noise_Types = ["...", "Impulse Noise", "Gaussian Noise", "Uniform Noise"]
        ChooseButtonLabel = customtkinter.CTkLabel(Main, text="Choose A Noise Addition Filter", font=("System", 40, "bold"))
        global Spatial_Noise_Filter_ComboBox
        Spatial_Noise_Filter_ComboBox = customtkinter.CTkComboBox(Main, values=Noise_Types, width=400, height=55, font=("System", 30, "bold"))
           
        global IsSpacial
        IsSpacial = True
        Back_Button = customtkinter.CTkButton(Main, text="<- Back",width=80, height=32, font=("System", 20, "bold"), fg_color="DarkRed", command=lambda:MainGUI.GoBack_ChooseDifferentFilter())        
        Back_Button.place(x=Main.winfo_screenwidth()/2 - 880,y=Main.winfo_screenheight()/2 - 490, anchor="center")

        ConfirmButton = customtkinter.CTkButton(Main, text="Confirm", command=lambda: MainGUI.Spatial_Confirmation(), width=100, height=50, font=("System", 30, "bold"), fg_color="darkgreen")
        QuitButton = customtkinter.CTkButton(Main, text="Quit", command=quit, width=100, height=50, font=("System", 30, "bold"), fg_color="darkgreen")
        ChooseButtonLabel.place(x=Main.winfo_screenwidth()/2 - 450,y=Main.winfo_screenheight()/2 - 400, anchor="center")
        Spatial_Noise_Filter_ComboBox.place(x=Main.winfo_screenwidth()/2 - 520, y=Main.winfo_screenheight()/2 - 250, anchor="center")
        ConfirmButton.place(x=Main.winfo_screenwidth()/2 - 220, y=Main.winfo_screenheight() /2 - 250, anchor="center")
        QuitButton.place(x=Main.winfo_screenwidth()/2 - 120,y=Main.winfo_screenheight() / 2 - 50, anchor="center")
        
    def Spatial_Domain_Page():
        MainGUI.DestroyAll()
        
        ChooseButtonLabel = customtkinter.CTkLabel(Main, text="Choose A Filter Category", font=("System", 40, "bold"))
        Smoothing_Btn = customtkinter.CTkButton(Main, text="Smoothing Filters", width=500, height=125, font=("System", 40, "bold"), fg_color="darkgreen", command=lambda: MainGUI.Smoothing_Filters_Page())
        Sharpening_Btn = customtkinter.CTkButton(Main, text="Sharpening Filters", width=500, height=125, font=("System", 40, "bold"), fg_color="darkgreen", command=lambda: MainGUI.Sharpening_Filters_Page())
        Noise_Btn = customtkinter.CTkButton(Main, text="Noise Filters", width=500, height=125, font=("System", 40, "bold"), fg_color="darkgreen", command=lambda: MainGUI.Noise_Filters_Page())
       
        ChooseButtonLabel.place(x=Main.winfo_screenwidth()/2 - 450, y=Main.winfo_screenheight()/2 - 480, anchor="center")
        Smoothing_Btn.place(x=Main.winfo_screenwidth()/2 - 450,y=Main.winfo_screenheight() / 2 - 370, anchor="center")
        Sharpening_Btn.place(x=Main.winfo_screenwidth()/2 -450 ,y=Main.winfo_screenheight() / 2 - 220, anchor="center")
        Noise_Btn.place(x=Main.winfo_screenwidth()/2 -450 ,y=Main.winfo_screenheight() / 2 - 70, anchor="center")

    def TransFreq_Domain_Page():
        MainGUI.DestroyAll()
        TransFreq_Types = ["...", "Histogram Equalization", "Histogram Specification", "Fourier Transform", "Linear Interpolation", "Bilinear Interpolation", "Bicubic Interpolation"]
        ChooseClassLbl = customtkinter.CTkLabel(Main, text="Choose A Transform / Frequency Filter", font=("System", 40, "bold"))

        Back_Button = customtkinter.CTkButton(Main, text="<- Back",width=80, height=32, font=("System", 20, "bold"), fg_color="DarkRed", command=lambda:MainGUI.Choose_Domain())        
        Back_Button.place(x=Main.winfo_screenwidth()/2 - 880,y=Main.winfo_screenheight()/2 - 490, anchor="center")

        global TransFreq_Filters_ComboBox
        TransFreq_Filters_ComboBox = customtkinter.CTkComboBox(Main, values=TransFreq_Types, width=400, height=55, font=("System", 30, "bold"))
        ConfirmButton = customtkinter.CTkButton(Main, text="Confirm", command=lambda: MainGUI.TransFreq_Confirmation(), width=100, height=50, font=("System", 30, "bold"), fg_color="darkgreen")
        QuitButton = customtkinter.CTkButton(Main, text="Quit", command=quit, width=100, height=50, font=("System", 30, "bold"), fg_color="darkgreen")
        global IsTransFreq
        
        ChooseClassLbl.place(x=Main.winfo_screenwidth()/2 - 450,y=Main.winfo_screenheight()/2 - 400, anchor="center")
        TransFreq_Filters_ComboBox.place(x=Main.winfo_screenwidth()/2 - 520, y=Main.winfo_screenheight()/2 - 250, anchor="center")
        ConfirmButton.place(x=Main.winfo_screenwidth()/2 - 220, y=Main.winfo_screenheight() /2 - 250, anchor="center")
        QuitButton.place(x=Main.winfo_screenwidth()/2 - 120,y=Main.winfo_screenheight() / 2 - 50, anchor="center")
        IsTransFreq = True

    def Choose_Domain():
        MainGUI.DestroyAll()
        ChooseButtonLabel = customtkinter.CTkLabel(Main, text="Choose A Domain Filters", font=("System", 40, "bold"))
        Spatial_Btn = customtkinter.CTkButton(Main, text="Spatial", width=500, height=125, font=("System", 40, "bold"), fg_color="darkgreen", command=lambda: MainGUI.Spatial_Domain_Page())
        TransFreq_Btn = customtkinter.CTkButton(Main, text="Transform & Frequency", width=500, height=125, font=("System", 40, "bold"), fg_color="darkgreen", command=lambda: MainGUI.TransFreq_Domain_Page())
        
        ChooseButtonLabel.place(x=Main.winfo_screenwidth()/2 - 450, y=Main.winfo_screenheight()/2 - 400, anchor="center")
        Spatial_Btn.place(x=Main.winfo_screenwidth()/2 - 450,y=Main.winfo_screenheight() / 2 - 250, anchor="center")
        TransFreq_Btn.place(x=Main.winfo_screenwidth()/2 -450 ,y=Main.winfo_screenheight() / 2 - 100, anchor="center")


Main = customtkinter.CTk()
Main.title("Domain Filters")
Main.attributes("-topmost", True)

ScreenWidth = Main.winfo_screenwidth()
ScreenHeight = Main.winfo_screenheight()
Main.geometry("1000x580".format(ScreenWidth, ScreenHeight))

WelcomeLabel = customtkinter.CTkLabel(Main, text="Welcome To The\nBest Image Project", font=("System", 40, "bold"))
ContinueButton = customtkinter.CTkButton(Main, text="Continue", command=lambda: MainGUI.Start_Page_Continue(),  width=500, height=125, font=("System", 40, "bold"), fg_color="darkgreen")
QuitButton = customtkinter.CTkButton(Main, text="Quit", command=quit, width=500, height=125, font=("System", 40, "bold"), fg_color="darkgreen")
# ResetButton = customtkinter.CTkButton(Main, text="Quit", command=MainGUI.ResetWindow(), width=500, height=125, font=("System", 40, "bold"), fg_color="darkgreen")

WelcomeLabel.place(x=ScreenWidth/2-450, y=ScreenHeight/2 - 450, anchor="center")
ContinueButton.place(x=ScreenWidth/2 - 450, y=ScreenHeight/2 - 250, anchor="center")
QuitButton.place(x=ScreenWidth/2 - 450, y=ScreenHeight/2 - 100, anchor="center")
# ResetButton.place(x=ScreenWidth/2 - 450, y=ScreenHeight/2 - 100, anchor="center")

Main.mainloop()
