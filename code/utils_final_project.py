import numpy as np
import matplotlib.pyplot as plot


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



