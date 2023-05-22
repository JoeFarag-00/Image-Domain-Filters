from tkinter.filedialog import askopenfilename
import cv2
import numpy

def GetImagePath():
    return askopenfilename(title = 'Select The Image',filetypes = (('png files', '*.png'), ('bmp files', '*.bmp'), ('jpeg files', '*.jpeg'),('jpg files','*.jpg')))

def ReadImage(Path):
    return cv2.imread(Path,0)

def SaveImage(Path,Image):
    cv2.imwrite(Path,Image)

def ShowImage(WindowTitle,Image):
    cv2.imshow(f'{WindowTitle}',Image)
    cv2.waitKey(0)
    
def PadImageWithZeros(Image):
    r,c = Image.shape[0],Image.shape[1]
    PaddedImage=numpy.zeros((r + 2, c + 2), dtype=Image.dtype)
    PaddedImage[1:-1,1:-1]=Image
    return PaddedImage

def Int32ToUint8(List):     
    return List.astype(numpy.uint8)

def CalculateMin(Kernel):
    FlattenedKernel = Kernel.flatten()
    Min = numpy.min(Kernel)
    return Min

def ApplyMinFilter(PaddedImage):
    FilteredImage=PaddedImage.copy()
    for r in range(1,PaddedImage.shape[0]-1):
        for c in range(1,PaddedImage.shape[1]-1):
            Kernel = PaddedImage[r - 1:r + 2, c - 1:c + 2]
            Min = CalculateMin(Kernel)
            FilteredImage[r, c] = Min
    return FilteredImage

Path = GetImagePath()

OriginalImage = ReadImage(Path)

PaddedImage = PadImageWithZeros(OriginalImage)

FilteredImage = ApplyMinFilter(PaddedImage)

FilteredImage = Int32ToUint8(FilteredImage)

SaveImage('Output Images\Min Filter.png',FilteredImage)