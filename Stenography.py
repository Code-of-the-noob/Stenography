#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 17:19:50 2017

@author: n0_ob
"""


import sys
from PIL import Image

def txt_encode(imp,text):
    Im=Image.open(imp)
    
    pixel=Im.load()
    pixel[0,0]=(len(text)%256,(len(text)//256)%256,(len(text)//65536))
    
    for i in range(1,len(text)+1):
        k=list(pixel[0,i])
        k[0]=int(k[0]/10)*10+ord(text[i-1])//100
        k[1]=int(k[1]/10)*10+((ord(text[i-1])//10)%10)
        k[2]=int(k[2]/10)*10+ord(text[i-1])%10
        #print(pixel[0,i],k,ord(text[i-1]))
        pixel[0,i]=tuple(k)
    Im.save("r.png")
    
def txt_decode(imp):
    Im=Image.open(imp)
    #Im=Im.convert('RGB')
    pixels=Im.load()
    size=(pixels[0,0][0])+(pixels[0,0][1])*256+(pixels[0,0][2])*65536
    print (size)
    t=[]
    for i in range(1,size+1):
        #print(pixels[0,i])
        t.append(chr((pixels[0,i][0]%10)*100+(pixels[0,i][1]%10)*10+(pixels[0,i][2]%10)))
    te="".join(t)
    print(te)
    
def img_encode(imp,cmp,s=4):
    im=Image.open(imp)
    cm=Image.open(cmp)
    ip=im.load()
    cp=cm.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            p=ip[i,j]
            q=cp[i,j]
            red   = p[0] - (p[0] % s) + (s * q[0] / 255)
            green = p[1] - (p[1] % s) + (s * q[1] / 255)
            blue  = p[2] - (p[2] % s) + (s * q[2] / 255)
            ip[i,j]=(int(red),int(green),int(blue))

    im.save("r.png")
    
    
def img_decode(imp,s=4):
    im=Image.open(imp)
    ip=im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            p=ip[i,j]
            red   = (p[0] % s) * 255 / s
            green = (p[1] % s) * 255 / s
            blue  = (p[2] % s) * 255 / s
            ip[i,j]=(int(red),int(green),int(blue))

    im.show()
    

#Main()
if __name__=="__main__":
    if sys.argv[1]=="text" and sys.argv[2]=="encode":
        txt_encode(sys.argv[3],sys.argv[4])


    elif sys.argv[1]=="text" and sys.argv[2]=="decode":
        txt_decode(sys.argv[3])
    

    elif sys.argv[1]=="image" and sys.argv[2]=="encode":
        img_encode(sys.argv[3],sys.argv[4])

    elif sys.argv[1]=="image" and sys.argv[2]=="decode":
        img_decode(sys.argv[3])

