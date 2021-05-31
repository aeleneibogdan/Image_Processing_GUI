# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:49:31 2021

@author: aelen
"""

import numpy as np
import matplotlib.pyplot as plt
import pywt
import os
import pyimage

from tkinter import *
from tkinter import filedialog
import cv2


# def imageArea():
#     plot_frame = Frame(root)
#     plot_frame.grid(row=0,column=0, sticky='nw')
    
#     fig,ax = plt.subplots(figsize=(5,4))
#     canvas=FigureCanvasTkAgg(fig, master=plot_frame)
#     canvas.get_tk_widget().pack()

cwd = os.getcwd()
imgname='bojnice.jpg'

path = os.path.join(cwd, imgname)
img = cv2.imread(path, 0)
imgResized = cv2.resize(img, (648,480))


def loadButton():
    # root.filename = filedialog.askopenfilename(initialdir="C://Users//aelen//Desktop//Facultate//DSP//DSPProject",title="Select image",filetypes=(("JPG files","*.jpg"),("PNG files","*.png"),("All files","*.*")))
    # photo = PhotoImage(root.filename)
    # myLabel = Label(e, image=photo).place(x=100,y=100)
    root.filename = filedialog.askopenfilename(initialdir="C://Users//aelen//Desktop//Facultate//DSP//DSPProject",title="Select image",filetypes=(("JPG  files","*.jpg"),("PNG files","*.png"),("All files","*.*")))
    myLabel = Label(e, text=root.filename).place(x=100,y=100)

def originalImage():
    cv2.imshow('Original Photo', imgResized)

def Filter2D():
    kernel=np.ones((3,3), np.float32)/9
    filter_2d = cv2.filter2D(imgResized, -1, kernel)
    cv2.imshow('2D filter', filter_2d)
    
def ImageBlur():
    image_blur = cv2.blur(imgResized,(3,3))
    cv2.imshow('Image Blur', image_blur)
    
def ImageGaussianBlur():
    gaussian_blur = cv2.GaussianBlur(imgResized,(3,3), 0)
    cv2.imshow('Image Gaussian Blur', gaussian_blur)
    
def ImageEdgeDetection():
    edgeDetection=cv2.Canny(imgResized,100,200)
    cv2.imshow('Edge Detection', edgeDetection)
    
def DiscreteWaveletTransform2D():
    coefficients = pywt.dwt2(imgResized, 'haar', mode='periodization')
    cA1, (cH1,cV1,cD1) = coefficients #Approximation Coeff, Horizontal Coeffs, Vertical Coeffs, Diagonal Coeffs - output arguments
    
    plt.figure(figsize=(15,15))
    
    #Plotting Approximation Coefficients
    plt.subplot(2,2,1)
    plt.imshow(cA1, 'gray')
    plt.title('Approximation Coefficients')
    
    #Plotting Horizontal detail coefficients
    plt.subplot(2,2,2)
    plt.imshow(cH1, 'gray')
    plt.title('Horizontal detail Coefficients')
    
    #Plotting Vertical detail coefficients
    plt.subplot(2,2,3)
    plt.imshow(cV1, 'gray')
    plt.title('Vertical detail Coefficients')
    
    #Plotting Diagonal detail coefficients
    plt.subplot(2,2,4)
    plt.imshow(cD1, 'gray')
    plt.title('Diagonal detail Coefficients')
    


root = Tk()
root.title('Image processing GUI')
root.geometry("300x300")
root.configure(bg="#DAF7A6")

loadButton = Button(root, text="Load Image", command=loadButton)
loadButton.place(x=7,y=30)

originalButton = Button(root, text="Original", command=originalImage)
originalButton.place(x=70,y=70)

filter2DButton = Button(root, text="Filter2D", command=Filter2D)
filter2DButton.place(x=70,y=100)

blurButton = Button(root, text="Blur", command=ImageBlur)
blurButton.place(x=70,y=130)

gaussBlurButton = Button(root, text="Gaussian Blur", command=ImageGaussianBlur)
gaussBlurButton.place(x=140,y=70)

edgeButton = Button(root, text="Edge Detection", command=ImageEdgeDetection)
edgeButton.place(x=140,y=100)

dwtButton = Button(root, text="DWT", command=DiscreteWaveletTransform2D)
dwtButton.place(x=140,y=130)

quitButton = Button(root, text="Exit", command=root.quit)
quitButton.place(x=130,y=270)

root.mainloop()