# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 10:01:03 2018

@author: haoyu
"""

import numpy as np
from PIL import Image

if __name__=='__main__':
    image_file='girl.png'
    height=100
    
    img=Image.open(image_file)
    img_width,img_height=img.size
    width=2*height*img_width// img_height
    img=img.resize((width,height),Image.ANTIALIAS)
    pixels=np.array(img.convert('L'))
    print(pixels.shape)
    print(pixels)
    chars='MNHQ$OC?7>!:-;. '
    N=len(chars)
    step=256//N
    print(N)
    result=''
    for i in range(height):
        for j in range(width):
            result+=chars[pixels[i][j]//step]
        result+='\n'
        with open('girl.txt',mode='w') as f:
            f.write(result)