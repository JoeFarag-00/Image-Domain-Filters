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

def CalculateMedian(Kernel):
    FlattenedKernel = Kernel.flatten()
    SortedFlattenedKernel = sorted(FlattenedKernel)
    N=len(SortedFlattenedKernel)
    if N % 2 == 0:
        return (SortedFlattenedKernel[N//2 - 1] + SortedFlattenedKernel[N//2]) / 2
    else:
         return SortedFlattenedKernel[N//2]

def ApplyMedianFilter(PaddedImage):
    FilteredImage = PaddedImage.copy()
    for r in range(1, PaddedImage.shape[0] - 1):
        for c in range(1, PaddedImage.shape[1] - 1):
            Kernel = PaddedImage[r - 1:r + 2, c - 1:c + 2]
            Median = CalculateMedian(Kernel)
            FilteredImage[r, c] = Median
    return FilteredImage

def ApplyUnsharpMaskingAndHighboostFilteringMedian(OriginalImage, K):
    PaddedImage = PadImageWithZeros(OriginalImage)
    FilteredImage = ApplyMedianFilter(PaddedImage)
    FilteredImage = Int32ToUint8(FilteredImage)
    Mask = PaddedImage - FilteredImage
    SharpenedImage = PaddedImage + K * Mask
    return SharpenedImage

# Path = GetImagePath()

# OriginalImage = ReadImage(Path)

# K=int(input('Enter Weight Of The Mask:'))

# if  K>=0:
#     SharpenedImage = ApplyUnsharpMaskingAndHighboostFilteringMedian(OriginalImage,K)
# else:
#     SharpenedImage = PadImageWithZeros(OriginalImage)

# SaveImage(r'Output Images\Unsharp Masking and Highboost Filtering Using Median Filter.png',SharpenedImage)