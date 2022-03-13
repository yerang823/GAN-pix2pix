from PIL import Image
import pydicom as dicom
import numpy as np
import os,glob,cv2
import matplotlib.pyplot as plt


def get_LUT_value(data, window, level):
    """Apply the RGB Look-Up Table for the given
       data and window/level value."""
    try:
        window = window[0]
    except TypeError:
        pass
    try:
        level = level[0]
    except TypeError:
        pass

    return np.piecewise(data,
                        [data <= (level - 0.5 - (window - 1) / 2),
                         data > (level - 0.5 + (window - 1) / 2)],
                        [0, 255, lambda data: ((data - (level - 0.5)) /
                         (window - 1) + 0.5) * (255 - 0)])
        
        
def dcm2bmp(path_dir, bmp_path, foldername, bool_save):
    
    # ====================
    # CT
    # ====================
    file_list1=glob.glob(path_dir+'ct/*')
    #file_list1.sort()
    
    for file in file_list1:
        if file.split('.')[-1]!='dcm':
            os.rename(file, file+'.dcm')
        
    dcm_list1=[]
    for item in file_list1:
        if item.find('.dcm') is not -1:
            dcm_list1.append(item)
   
    print('len(ct)=',len(dcm_list1))
    
    # ====================
    # MR
    # ====================
    file_list2=glob.glob(path_dir+'mr/*')
    #file_list2.sort()
    
    for file in file_list2:
        if file.split('.')[-1]!='dcm':
            os.rename(file, file+'.dcm')
        
    dcm_list2=[]
    for item in file_list2:
        if item.find('.dcm') is not -1:
            dcm_list2.append(item)
            
    
    print('len(mr)=',len(dcm_list2))
    
    
    
    idx1=[]
    bmp_ct=[]
    for j in range(len(dcm_list1)): ##############
        # ====================
        # CT
        # ====================
        
        ds=dicom.read_file(dcm_list1[j])
        img = ds.pixel_array
        img_output= ds.RescaleSlope * img + ds.RescaleIntercept
        
        img_output=img_output.astype('float32')
        img_1024=img_output
        #image1=get_LUT_value(img_1024, ds.WindowWidth, ds.WindowCenter)
        image1=get_LUT_value(img_1024, 1500, 450)
        #print(j,image1.shape)
        image1=cv2.resize(image1,(512,512))
        #print(j,image1.shape)
        bmp_ct.append(image1)
        idx1.append(float(ds.ImagePositionPatient[2]))
        
        del image1
    
    idx1 = np.array(idx1,dtype=float)
    bmp_ct = [x for _, x in sorted(zip(idx1, bmp_ct),key = lambda x : x[0])]
       
    

    idx2=[]
    bmp_mr=[]
    for j in range(len(dcm_list2)):    ##############
        # ====================
        # MR
        # ====================
        ds2=dicom.read_file(dcm_list2[j]) #########
        img2 = ds2.pixel_array
        img_output2=img2
        img_output2= ds2.RescaleSlope * img2 + ds2.RescaleIntercept
        img_output2=img_output2.astype('float32')
        img_1024_2=img_output2
        #image2=get_LUT_value(img_1024_2, ds2.WindowWidth, ds2.WindowCenter)
        image2=get_LUT_value(img_1024_2, 670,335)
        #print(j, image2.shape)
        image2=cv2.resize(image2,(512,512))
        #print(j,image2.shape)
        bmp_mr.append(image2)
        idx2.append(float(ds2.ImagePositionPatient[2]))
        
        del image2
    
    idx2 = np.array(idx2,dtype=float)
    bmp_mr = [x for _, x in sorted(zip(idx2, bmp_mr),key = lambda x : x[0])]
       
    
    min_len=min(len(dcm_list1),len(dcm_list2))
    
    for j in range(min_len):
        print(j)
        k=j
        plt.subplot(1,2,1)
        plt.imshow(bmp_ct[j],cmap='gray')
        plt.subplot(1,2,2)
        plt.imshow(bmp_mr[k],cmap='gray')
        plt.show()
        
        
        if bool_save==True:
        # j 확인하고 나서 저장할것!!
            cv2.imwrite(bmp_path+'ct/%s_{0:03d}.bmp'.format(j)%(foldername),bmp_ct[j])
            cv2.imwrite(bmp_path+'mr/%s_{0:03d}.bmp'.format(j)%(foldername),bmp_mr[k])
			
			
