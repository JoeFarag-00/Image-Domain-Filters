import numpy as np
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

def Gaussian_Filter(size, sigma):
    x, y = np.mgrid[-size // 2 + 1:size // 2 + 1, -size // 2 + 1:size // 2 + 1]
    Generated_Smoos = np.exp(-((x ** 2 + y ** 2) / (2.0 * sigma ** 2))) / (2 * np.pi * sigma ** 2)
    # print(Generated_Smoos)
    return Generated_Smoos / Generated_Smoos.sum()

def Demina_Image(image, size, sigma):
    image = image.convert('L')
    img_array = np.array(image)
    height, width = img_array.shape
    Temp_Kernal = Gaussian_Filter(size, sigma)
    print("Filter: ",Temp_Kernal)
    
    Smoos_Image = np.zeros((height - size + 1, width - size + 1))
    
    for i in range(size // 2, height - size // 2):
        for j in range(size // 2, width - size // 2):
            # Main_Img = img_array[i - size // 4:i + size // 4 + 2, j - size // 2:j + size // 2 + 1]
            Main_Img = img_array[i - size // 2:i + size // 2 + 1, j - size // 2:j + size // 2 + 1]
            
            Smoos_Image[i - size // 2, j - size // 2] = np.sum(Main_Img * Temp_Kernal)

    denoised_image = Image.fromarray(Smoos_Image.astype('uint8'))
    return denoised_image

class GF_GUI:
    
    def __init__(self, master):
        self.master = master
        master.title("Image Denoising")
        self.browse_button = Button(master, text="Browse", command=self.Load_Image)
        self.browse_button.pack(pady=10)
        self.original_image_label = Label(master)
        self.original_image_label.pack(side=LEFT, padx=10)
        
        self.denoised_image_label = Label(master)
        self.denoised_image_label.pack(side=LEFT, padx=10)
        self.denoised_image = None

    def Load_Image(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select Image File", filetypes=(
            ("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
        if filename:
            image = Image.open(filename).convert("L")
            # original_image = Image.open(self.image_path).convert("L")
            # original_image = original_image.resize((450,450))
            original_image = ImageTk.PhotoImage(image)
            self.original_image_label.config(image=original_image)
            self.original_image_label.image = original_image

            self.denoised_image = Demina_Image(image, 5, 1)
            denoised_image = ImageTk.PhotoImage(self.denoised_image)
            self.denoised_image_label.config(image=denoised_image)
            self.denoised_image_label.image = denoised_image

root = Tk()
gui = GF_GUI(root)
root.mainloop()
