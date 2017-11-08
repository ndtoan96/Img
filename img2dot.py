import numpy as np
from PIL import Image
import sys
import os

dirpath= os.path.dirname(sys.argv[0])
if len(sys.argv)==1:
    path='img.png'
else:
    path=sys.argv[1]
image=Image.open(path)
image=image.convert('1')
data=np.asarray(image)
size=data.shape
rows=size[0]//3*3
columns=size[1]//2*2
data=data[0:rows,0:columns]
data=data==False
a=np.array([[1,0],[0,0],[0,0]])
b=np.array([[0,0],[1,0],[0,0]])
c=np.array([[0,0],[0,0],[1,0]])
d=np.array([[0,1],[0,0],[0,0]])
e=np.array([[0,0],[0,1],[0,0]])
f=np.array([[0,0],[0,0],[0,1]])
def conv(s):
    return eval(s.replace('','+')[1:-1])
sample=open(dirpath+'/sample.txt','r').read()
sample=sample.split('\n')[:-1]
braille=open(dirpath+'/braille.txt','r').read()
braille=braille.split('\n')[:-1]
braille=[conv(i) for i in braille]
braille.append(a-a)

def exchange(element):
    for i, j in enumerate(braille):
        if (j==element).all():
            index=i
    return sample[index]

img_text=''
for y in range(0,data.shape[0],3):
    for x in range(0,data.shape[1],2):
        block=data[y:y+3,x:x+2].astype(int)
        img_text += exchange(block)
    img_text += '\n'
print(img_text)    
#open('img_text.txt','w').write(img_text)
