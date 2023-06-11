from PIL import Image, ImageOps
import os, glob

# Function to crop images
def cropImage(a,b):
    datas = Image.open(a)
    datas = datas.crop(b)
    datas.save('cropped/'+a)
    print('Cropped '+a)

# Function to remove solid color background
def removeBackground(a):
    img = Image.open(a)#image path and name
    img = img.convert('RGBA')
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 0))#black:255,255,255,0
        else:
            newData.append(item)
    img.putdata(newData)
    img.save('transp/'+a, 'PNG')#converted image name
    print('Removed Background of '+a)

## Call on the above functions to edit images
# Specify image path
path='/Users/dingchao/Downloads'

os.chdir(path)
images=glob.glob('*.png')
for image in images:
    # Crop image
    if not os.path.isdir(path+'/cropped'):
        os.mkdir(path+'/cropped')  
    cropImage(image,(200,200,1000,1000))
    '''
    # Remove black background for image
    if not os.path.isdir(path+'/transp'):
        os.mkdir(path+'/transp')       
    removeBackground(image)
    '''

## Mirror images
os.chdir(path+'/cropped')
images=glob.glob('*.png')
for image in images:
    img = Image.open(image)
    img_mirror = ImageOps.mirror(img)
    img_mirror.save(image.replace('a','b'))
    print('Created mirror image of '+image)
