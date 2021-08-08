#!/usr/bin/env python3
__author__ ="Raktim Kumar Mondol"

####################################################################################################
###################################### Import Required Lirary ######################################
####################################################################################################
seed=42
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import glob
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from patchify import patchify
import tifffile as tiff


SIZE=224
CHANNEL=3
patched_image ='C:/D_DRIVE/UNSW/Dataset/grand_challenge_data/patched_image/'

#################################   Read Train Image  ####################################
for directory_path in glob.glob("C:/D_DRIVE/UNSW/Experiment/Normalized_H&E/tcga-gc/*"):
    #print(directory_path)
    #path = directory_path.split("\\")[1]
    #print(label)

    
    for img_path in glob.glob(os.path.join(directory_path, "*.png")):
        #print(img_path)
        img_name = img_path.split("\\")[1]
        img_name = img_name.split(".")[0]
        print(img_name)
        full_path = os.path.join(patched_image, img_name)
        #to create blank folder
        #os.mkdir(full_path)
        #print(full_path)
        large_image_stack = cv2.imread(img_path, cv2.IMREAD_COLOR)       
        #img = cv2.resize(img, (SIZE, SIZE))
        large_image_stack = cv2.cvtColor(large_image_stack, cv2.COLOR_BGR2RGB)
        #print(img_path)
        patches_img = patchify(large_image_stack, (SIZE, SIZE, CHANNEL), step=SIZE)  #Step=256 for 256 patches means no overlap
        
        for i in range(patches_img.shape[0]):
            for j in range(patches_img.shape[1]):
                single_patch_img = patches_img[i,j,:,:]
                tiff.imwrite(full_path + '/image_' + str(img_name) + '_' + str(i)+str(j)+ '.png', single_patch_img)














