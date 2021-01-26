####### CORE IMPORTS ###############
import cv2
from cv2 import dnn_superres
from PIL import Image,ImageEnhance
import time
import numpy as np
import os
import sys
import random
import string
from datetime import datetime
import math

class ML():
    """" This class is for realizing ml models """
    
    def bgr2rgb(self, img):
        im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return im_rgb

    # define a function for peak signal-to-noise ratio (PSNR)
    def psnr(self, target, ref):
            
        # assume RGB image
        target_data = target.astype(float)
        ref_data = ref.astype(float)

        diff = ref_data - target_data
        diff = diff.flatten('C')

        rmse = math.sqrt(np.mean(diff ** 2.))

        return 20 * math.log10(255. / rmse)

    # define function for mean squared error (MSE)
    def mse(self, target, ref):
        # the MSE between the two images is the sum of the squared difference between the two images
        err = np.sum((target.astype('float') - ref.astype('float')) ** 2)
        err /= float(target.shape[0] * target.shape[1])
        
        return err

    # define function that combines all three image quality metrics
    def compare_images(self, target, ref):
        scores = []
        scores.append(psnr(target, ref))
        scores.append(mse(target, ref))
        #scores.append(ssim(target, ref, multichannel =True))
        
        return scores

    def loadim(self, img_file):
        file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        return img

    def upScaleEDSR(self, image):
        # Create an SR object
        sr = dnn_superres.DnnSuperResImpl_create()
        path = os.path.join(os.path.dirname(__file__),"weights//EDSR_x3.pb")
        sr.readModel(path)
        # Set the desired model and scale to get correct pre- and post-processing
        sr.setModel("edsr", 3)
        result = sr.upsample(image)
        return result

    def crop(img,x,y):
        y1,x1 = x
        y2,x2 = y
        crop_img = img[y1:y2,x1:x2]
        return crop_img

    def upScaleFSRCNN(self, image):
        # Create an SR object
        sr = dnn_superres.DnnSuperResImpl_create()

        path = os.path.join(os.path.dirname(__file__),"weights/FSRCNN_x3.pb")
        sr.readModel(path)
        # Set the desired model and scale to get correct pre- and post-processing
        sr.setModel("fsrcnn", 3)
        result = sr.upsample(image)
        return result
    
        
        
    def resize(img,shape):

        img_resized = cv2.resize(img, shape,interpolation = cv2.INTER_CUBIC) 
        return img_resized


        
    def BilinearUpscaling(img,factor = 2):
        
        img_resized = cv2.resize(img,(0,0), fx=factor, fy=factor, interpolation=cv2.INTER_LINEAR)
        return img_resized
        
    def rotate(image,x):
        (h1, w1) = image.shape[:2]
        center = (w1 / 2, h1 / 2)
        Matrix = cv2.getRotationMatrix2D(center, -90 * x, 1.0)
        rotated_image = cv2.warpAffine(image, Matrix, (w1, h1))
        return rotated_image

    def denoise(img):

        # denoising of image saving it into dst image 
        dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
        return dst
        
    def randomString(stringLength=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def save(self, typ,img):
        now = datetime.now()
        time_stamp = now.strftime("%m_%d_%H_%M_%S") 
        fn =os.path.join(os.path.dirname(__file__),'Saved_Images\\'+typ+time_stamp+'.png') # Couldnt find a way to get the correct system dir path so dont change the name of the file this is a mess. I repeat This is a mess .
        cv2.imwrite(fn,img)