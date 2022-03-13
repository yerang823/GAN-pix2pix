import image_similarity_measures
from image_similarity_measures.quality_metrics import rmse, psnr,ssim
import cv2,glob
import matplotlib.pyplot as plt
import numpy as np
import scipy

def get_metrics(region_num):
    path_li=glob.glob('./result/tocalc/%d/*.png'%region_num)
    path_li.sort()

    tot_ssim=[]
    tot_psnr=[]
    tot_rmse=[]
    for i in range(int(len(path_li)/2-1)):

        print('i==================',i)
        print(path_li[2*i])
        print(path_li[2*i+1])

        img1=cv2.imread(path_li[2*i],cv2.IMREAD_GRAYSCALE)
        img2=cv2.imread(path_li[2*i+1],cv2.IMREAD_GRAYSCALE)

        img1=cv2.resize(img1,(256,256))
        img2=cv2.resize(img2,(256,256))

        plt.subplot(1,2,1)
        plt.imshow(img1,cmap='gray')
        plt.axis('off')
        plt.subplot(1,2,2)
        plt.imshow(img2,cmap='gray')
        plt.axis('off')
        plt.show()

        val_s=ssim(img1,img2)

        print('ssim=',val_s)

        img1_tmp=np.expand_dims(img1,axis=-1)
        img2_tmp=np.expand_dims(img2,axis=-1)

        val_r=rmse(img1_tmp,img2_tmp)
        val_p=psnr(img1_tmp,img2_tmp)


        print('rmse=',val_r)
        print('psnr=',val_p)

        tot_ssim.append(val_s)
        tot_psnr.append(val_p)
        tot_rmse.append(val_r)
    
    return tot_ssim,tot_psnr,tot_rmseS
	
	
tot_s=[]
tot_p=[]
tot_r=[]
for i in range(3):
    s,p,r=get_metrics(i+1)
    tot_s.append(s)
    tot_p.append(p)
    tot_r.append(r)
