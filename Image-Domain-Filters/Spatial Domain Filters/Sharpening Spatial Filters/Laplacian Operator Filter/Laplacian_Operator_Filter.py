from tkinter.filedialog import askopenfilename
import cv2
import numpy

def GetImagePath():
    return askopenfilename(title='Select The Image', filetypes=(('png files', '*.png'), ('bmp files', '*.bmp'), ('jpeg files', '*.jpeg'), ('jpg files', '*.jpg')))

def ReadImage(Path):
    return cv2.imread(Path, 0)

def SaveImage(Path, Image):
    cv2.imwrite(Path, Image)

def ShowImage(WindowTitle, Image):
    cv2.imshow(f'{WindowTitle}', Image)

def WaitKey():
    cv2.waitKey(0)

def PadImageWithZeros(Image):
    r, c = Image.shape[0], Image.shape[1]
    PaddedImage = numpy.zeros((r + 2, c + 2), dtype=Image.dtype)
    PaddedImage[1:-1, 1:-1] = Image
    return PaddedImage

def Int32ToUint8(List):
    return List.astype(numpy.uint8)

def CreateLaplacianOperatorKernel(IWhichKernel):
    print('Choose The Kernel')
    print('1:')
    print('------------')
    print(numpy.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]))
    print('2:')
    print('------------')
    print(numpy.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]]))
    print('3:')
    print('------------')
    print(numpy.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]]))
    print('4:')
    print('------------')
    print(numpy.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]))
    # IWhichKernel=int(input('Enter:'))
    if IWhichKernel == 1:
        return numpy.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    if IWhichKernel == 2:
        return numpy.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    if IWhichKernel == 3:
        return numpy.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    if IWhichKernel == 4:
        return numpy.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    if IWhichKernel != 1 or IWhichKernel !=2 or IWhichKernel !=3 or IWhichKernel!=4:
        return CreateLaplacianOperatorKernel()
    
def ApplyLaplacianOperatorFilter(PaddedImage,IWhichKernel):
    FilteredImage = PaddedImage.copy()
    Kernel = CreateLaplacianOperatorKernel(IWhichKernel)
    for r in range(1, PaddedImage.shape[0] - 1):
        for c in range(1, PaddedImage.shape[1] - 1):
            LaplacianOperator = numpy.sum(PaddedImage[r - 1:r + 2, c - 1:c + 2] * Kernel)
            FilteredImage[r, c] = numpy.clip(LaplacianOperator, 0, 255)
    return FilteredImage

# Path = GetImagePath()

# OriginalImage = ReadImage(Path)

# PaddedImage = PadImageWithZeros(OriginalImage)

# FilteredImage = ApplyLaplacianOperatorFilter(PaddedImage)

# FilteredImage = Int32ToUint8(FilteredImage)

# SaveImage('Output Images/Laplacian Operator Filter.png', FilteredImage)