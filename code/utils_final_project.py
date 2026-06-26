import numpy as np
import matplotlib.pyplot as plot


def NBR(NIRband,SWIRband):
    '''Calculation of the Normalized Burned Ratio
    **input**
    1) NIRband: image in the NIR band
    2) SWIRband: image in the SWIR band
    **output**
     NBR coefficient'''
    baseline = 1e-10
    NIRband = NIRband
    SWIRband = SWIRband
    return (NIRband-SWIRband)/(NIRband+SWIRband)

def dNBR(prefire,postfire,params):
    '''Calculation of the severity level
    **input**
    1) prefire: NBR of prefire image
    2) postfire: NBR of postfire image
    **output**
      '''
    dNBR_raw = prefire - postfire
    r,c = slice(params[0][0],params[0][1]), slice(params[1][0],params[1][1])
    window = dNBR_raw[r,c]

    if window.size == 0 or np.all(np.isnan(window)):
        offset=0.0
    else:
        offset = np.nanmean(window)
    
    dNBR_thrs = ((prefire-postfire)*1000)-offset
    return dNBR_thrs

def RdNBR(dNBR, NBR_prefire):
    return dNBR/(np.abs(NBR_prefire)+0.001)**0.5

def uniformity(prefire,postfire):
    #------------------------------offset dNBR----------------------------------------------------------------------------
    #padding
    im = np.pad(prefire,1,mode='constant',constant_values =1)

    #Local Binary Patterns (offset)
    LBP = np.zeros_like(im,dtype=np.uint16)
    bits = []
    pix_uniformity = []
    counter = 0
    for i in range(1,im.shape[0]-1):
        for j in range(1,im.shape[1]-1):
            bits = []
            neighbourhood = np.array([im[i-1][j-1],im[i-1][j],im[i-1,j+1],\
           im[i][j+1],im[i+1][j+1],im[i+1][j],im[i+1][j-1],im[i][j-1]])
            for x in neighbourhood:
                if im[i][j] > x:
                    bits.append(0)
                else:
                    bits.append(1)
            #uniformity array
            counter =0
            for y in range(16):
             if bits[y] != bits[(y+1)%16]:
                    counter += 1
            if counter <= 2:
                pix_uniformity.append(1)
            else: 
                pix_uniformity.append(0)
            #transformem el valor a decimal
            value = 2**15*bits[15]+2**14*bits[14]+2**13*bits[13]+2**12*bits[12]+2**11*bits[11]+2**10*bits[10]+2**9*bits[9]+2**8*bits[8]\
                +2**7*bits[7]+2**6*bits[6]+2**5*bits[5]+2**4*bits[4]+2**3*bits[3]+2**2*bits[2]+2**1*bits[1]+2**0*bits[0]
            LBP[i][j] = value 
    
    return ((prefire-postfire)*1000)-LBP
    



def scale_image(im,param):
    '''To scale the image
    **input**
    1) im: image to scale
    2) param: ((xini,xfin),(yini,yfin))'''
    return im[param[0][0]:param[0][1],param[1][0]:param[1][1]]
