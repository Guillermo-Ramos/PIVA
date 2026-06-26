# %%
from skimage import io
import matplotlib.pyplot as plot
import numpy as np
from utils_final_project import NBR,dNBR, RdNBR

# %%
#---------------------------------------------------------Incendi de Paüls (imP) 03/06/2024------------------------------------------------------------------
#---------------------------------------------------------Setinel pre----------------------------------------------------------------------------------------
imP_S_B8A_pre = io.imread("../incendi-pauls/SETINEL/05-09-2024/2024-05-09-00_00_2024-05-09-23_59_Sentinel-2_L2A_B8A_(Raw).tiff")
imP_S_B12_pre = io.imread("../incendi-pauls/SETINEL/05-09-2024/2024-05-09-00_00_2024-05-09-23_59_Sentinel-2_L2A_B12_(Raw).tiff")
#informació sobre les imatges
print("Images information")
print("L2A B8A:")
print("type: ", imP_S_B8A_pre.dtype)
print("shape: ", imP_S_B8A_pre.shape)
print("dim: ", imP_S_B8A_pre.ndim)
print("L2A B12:")
print("type: ", imP_S_B12_pre.dtype)
print("shape: ", imP_S_B12_pre.shape)
print("dim: ", imP_S_B12_pre.ndim)


#%%
#---------------------------Setinel post------------------------------------
imP_S_B8A_post = io.imread("../incendi-pauls/SETINEL/18-6-2026/2026-06-18-00_00_2026-06-18-23_59_Sentinel-2_L2A_B8A_(Raw).tiff")
imP_S_B12_post = io.imread("../incendi-pauls/SETINEL/18-6-2026/2026-06-18-00_00_2026-06-18-23_59_Sentinel-2_L2A_B12_(Raw).tiff")
#informació sobre les imatges
print("Images information")
print("L2A B04:")
print("type: ", imP_S_B8A_post.dtype)
print("shape: ", imP_S_B8A_post.shape)
print("dim: ", imP_S_B8A_post.ndim)
print("L2A B07:")
print("type: ", imP_S_B12_post.dtype)
print("shape: ", imP_S_B12_post.shape)
print("dim: ", imP_S_B12_post.ndim)

#%%
#------------------LANDSAT pre and post fire-----------------------------------------
imP_L_pre = io.imread("../incendi-pauls/LANDSAT/Landsat8_B4_B7_Pauls_preFoc_2024-07-10.tif")
print('Image information:')
print('Pre fire')
print('tipus: ',imP_L_pre.dtype)
print('Forma: ',imP_L_pre.shape)
print('Dimensions: ',imP_L_pre.ndim)
imP_L_pre_B4, imP_L_pre_B7 = imP_L_pre[:,:,0], imP_L_pre[:,:,1]
imP_L_post = io.imread("../incendi-pauls/LANDSAT/Landsat8_B4_B7_Pauls_postFoc_2026-04-27.tif")
print('Post fire')
print('tipus: ',imP_L_post.dtype)
print('Forma: ',imP_L_post.shape)
print('Dimensions: ',imP_L_post.ndim)
imP_L_post_B4, imP_L_post_B7 = imP_L_post[:,:,0], imP_L_post[:,:,1]

# %%
#------------------------------------------------------------------------------------
print("Raw values for B8A pre (NIR): ", imP_S_B8A_pre.min(),imP_S_B8A_pre.max())
print("Raw values for B12 pre (SWIR): ", imP_S_B12_pre.min(),imP_S_B12_pre.max())
print("Raw values for B8A post (NIR): ", imP_S_B8A_post.min(),imP_S_B8A_post.max())
print("Raw values for B12 post (SWIR): ", imP_S_B12_post.min(),imP_S_B12_post.max())

# %%
#NBR and dNBR
imP_S_pre_NBR = NBR(imP_S_B8A_pre,imP_S_B12_pre)
print('Pre fire:', imP_S_pre_NBR)
imP_S_post_NBR = NBR(imP_S_B8A_post,imP_S_B12_post)
print('Post fire:', imP_S_post_NBR)
dNBR_P_S = dNBR(imP_S_pre_NBR,imP_S_post_NBR)
print('Burn severity: ',dNBR_P_S.min(),dNBR_P_S.max())
RdNBR_P_S = RdNBR(dNBR_P_S,imP_S_pre_NBR)
print("RdNBR: ", RdNBR_P_S.min(), RdNBR_P_S.max())


# %%
#representem per veure-les
plot.figure(figsize=(10,10))
plot.subplot(321)
plot.imshow(imP_S_B8A_pre,cmap='gray')
plot.axis('off')
plot.title('L2A B8a. Pre-fire')
plot.subplot(322)
plot.imshow(imP_S_B12_pre,cmap='gray')
plot.axis('off')
plot.title('L2A B12. Pre-fire')
plot.subplot(323)
plot.imshow(imP_S_B8A_post,cmap='gray')
plot.axis('off')
plot.title('L2A B8A. Post-fire')
plot.subplot(324)
plot.imshow(imP_S_B12_post,cmap='gray')
plot.axis('off')
plot.title('L2A B12. Post-fire')
plot.subplot(325)
plot.imshow(imP_S_pre_NBR,cmap='gray',vmin=0,vmax=1)
plot.colorbar()
plot.axis('off')
plot.title('NBR. Pre-fire')
plot.subplot(326)
plot.imshow(imP_S_post_NBR,cmap='gray',vmin=0,vmax=1)
plot.colorbar()
plot.axis('off')
plot.title('NBR. Post-fire')
plot.tight_layout(h_pad=2,w_pad=2)
plot.show()

plot.figure(figsize=(10,10))
plot.subplot(121)
plot.imshow(dNBR_P_S,cmap='gray',vmin=0,vmax=1)
plot.colorbar()
plot.axis('off')
plot.title('dNBR wildfire Paüls 2025 (Setinel database)')
plot.subplot(122)
plot.imshow(RdNBR_P_S,cmap='gray',vmin=0,vmax=1)
plot.colorbar()
plot.axis('off')
plot.title('RdNBR wildfire Paüls 2025 (Setinel database)')
plot.tight_layout()
plot.show()


# %%
#---------------------Landsat-----------------------------------------------
imP_L_pre = io.imread("../incendi-pauls/LANDSAT/Landsat8_B4_B7_Pauls_preFoc_2024-07-10.tif")
imP_L_pre_B4, imP_L_pre_B7 = imP_L_pre[:,:,0], imP_L_pre[:,:,1]
imP_L_post = io.imread("../incendi-pauls/LANDSAT/Landsat8_B4_B7_Pauls_postFoc_2026-04-27.tif")
imP_L_post_B4, imP_L_post_B7 = imP_L_post[:,:,0], imP_L_post[:,:,1]
print('Informació')
print('Pre B4')
print('tipus: ', imP_L_pre_B4.dtype)
print('forma: ',imP_L_pre_B4.shape)
print('dimensions: ',imP_L_pre_B4.ndim)
print('Pre B7')
print('tipus: ', imP_L_pre_B7.dtype)
print('forma: ',imP_L_pre_B7.shape)
print('dimensions: ',imP_L_pre_B7.ndim)
print('Post B4')
print('tipus: ', imP_L_post_B4.dtype)
print('forma: ',imP_L_post_B4.shape)
print('dimensions: ',imP_L_post_B4.ndim)
print('dimensions: ',imP_L_pre_B7.ndim)
print('Post B7')
print('tipus: ', imP_L_post_B7.dtype)
print('forma: ',imP_L_post_B7.shape)
print('dimensions: ',imP_L_post_B7.ndim)


# %%
#NBR and dNBR
imP_L_pre_NBR = NBR(imP_L_pre_B4,imP_L_pre_B7)
print('Pre fire:', imP_L_pre_NBR)
imP_L_post_NBR = NBR(imP_L_post_B4,imP_L_post_B7)
print('Post fire:', imP_L_post_NBR)
dNBR_P_L = dNBR(imP_L_pre_NBR,imP_L_post_NBR)
print('Burn severity: ',dNBR_P_L.min(),dNBR_P_L.max())
RdNBR_P_L = RdNBR(dNBR_P_L,imP_L_pre_NBR)
print("RdNBR: ", RdNBR_P_L.min(), RdNBR_P_L.max())


# %%
#representem per veure-les
plot.figure(figsize=(10,10))
plot.subplot(321)
plot.imshow(imP_L_pre_B4,cmap='gray')
plot.axis('off')
plot.title('Landsat B4. Pre-fire')
plot.subplot(322)
plot.imshow(imP_L_pre_B7,cmap='gray')
plot.axis('off')
plot.title('Landsat B7. Pre-fire')
plot.subplot(323)
plot.imshow(imP_L_post_B4,cmap='gray')
plot.axis('off')
plot.title('Landsat B4. Post-fire')
plot.subplot(324)
plot.imshow(imP_L_post_B7,cmap='gray')
plot.axis('off')
plot.title('Landsat B7. Post-fire')
plot.subplot(325)
plot.imshow(imP_L_pre_NBR,cmap='gray')
plot.colorbar()
plot.axis('off')
plot.title('NBR. Pre-fire')
plot.subplot(326)
plot.imshow(imP_L_post_NBR,cmap='gray')
plot.colorbar()
plot.axis('off')
plot.title('NBR. Post-fire')
plot.tight_layout(h_pad=2,w_pad=2)
plot.show()

plot.figure(figsize=(10,10))
plot.subplot(121)
plot.imshow(dNBR_P_L,cmap='gray')
plot.colorbar()
plot.axis('off')
plot.title('dNBR wildfire Paüls 2025 (Landsat database)')
plot.subplot(122)
plot.imshow(RdNBR_P_L,cmap='gray')
plot.colorbar()
plot.axis('off')
plot.title('RdNBR wildfire Paüls 2025 (Landsat database)')
plot.tight_layout()
plot.show()
