import numpy as np
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans
from sklearn.utils import shuffle

def NBR(NIRband,SWIRband):
    '''Calculation of the Normalized Burned Ratio
    **input**
    1) NIRband: image in the NIR band
    2) SWIRband: image in the SWIR band
    **output**
     NBR coefficient'''
    NIRband = NIRband.astype(np.float32)
    SWIRband = SWIRband.astype(np.float32)
    return (NIRband-SWIRband)/(NIRband+SWIRband+1e-10)

def dNBR(prefire,postfire):
    '''Calculation of the severity level
    **input**
    1) prefire: NBR of prefire image
    2) postfire: NBR of postfire image
    **output**
      '''
    return prefire-postfire


def RdNBR(dNBR, NBR_prefire):
    return dNBR/(np.abs(NBR_prefire)+0.001)**0.5

def Kmeans_segmentation(im,low_lim,upper_lim):
    #primer acotem la regió i filtrem a la zona cremada
    mask = (im>low_lim)&(im<upper_lim)
    filt_im = im[mask].reshape(-1,1)
    #entrenem els píxels cremats
    #data_P_S = np.reshape(filtered_RdNBR, (-1,1))
    mostra = shuffle(filt_im, random_state=0)[:1000] #mostra per accelerar entrenament
    kmn = KMeans(n_clusters=3, init='k-means++',random_state=0).fit(mostra) #entrenament
    labels = kmn.predict(filt_im) #etiquetar
    centroids = kmn.cluster_centers_
    #reconstrucció de la imatge
    im_Kmeans = np.zeros(im.shape,dtype=int)
    im_Kmeans[mask] = labels + 1
    return im_Kmeans


