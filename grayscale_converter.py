# -*- coding: utf-8 -*-

from PIL import Image
import os

image_directory = '/Users/vdtang/Documents/test'
grayscale_directory = '/Users/vdtang/Documents/test_grayscale'

if not os.path.isdir(grayscale_directory):
 	os.makedirs(grayscale_directory)

counter = 0
for file in os.listdir(image_directory):
    if file.lower().endswith(".jpeg"):
        img = Image.open(image_directory + os.sep + file).convert('LA').convert('RGB')
        img.save(grayscale_directory + os.sep + file)
        print(counter)
        counter+=1
        
