# %%
from skimage import io
import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
from utils_final_project import NBR,dNBR, RdNBR

# %%
#---------------------------------------------------------Incendi de Paüls (imP) 03/06/2024------------------------------------------------------------------
#---------------------------------------------------------Setinel pre----------------------------------------------------------------------------------------
imP_S_B8A_pre = io.imread("/Users/blancagilabertlopez/PIVA/incendi-pauls/SETINEL/05-09-2024/2024-05-09-00_00_2024-05-09-23_59_Sentinel-2_L2A_B8A_(Raw).tiff")
imP_S_B12_pre = io.imread("/Users/blancagilabertlopez/PIVA/incendi-pauls/SETINEL/05-09-2024/2024-05-09-00_00_2024-05-09-23_59_Sentinel-2_L2A_B12_(Raw).tiff")
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
imP_S_B8A_post = io.imread("/Users/blancagilabertlopez/PIVA/incendi-pauls/SETINEL/18-6-2026/2026-06-18-00_00_2026-06-18-23_59_Sentinel-2_L2A_B8A_(Raw).tiff")
imP_S_B12_post = io.imread("/Users/blancagilabertlopez/PIVA/incendi-pauls/SETINEL/18-6-2026/2026-06-18-00_00_2026-06-18-23_59_Sentinel-2_L2A_B12_(Raw).tiff")
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
imP_L_pre = io.imread("/Users/blancagilabertlopez/PIVA/incendi-pauls/LANDSAT/Landsat8_B4_B7_Pauls_preFoc_2024-07-10.tif")
print('Image information:')
print('Pre fire')
print('tipus: ',imP_L_pre.dtype)
print('Forma: ',imP_L_pre.shape)
print('Dimensions: ',imP_L_pre.ndim)
imP_L_pre_B4, imP_L_pre_B7 = imP_L_pre[:,:,0], imP_L_pre[:,:,1]
imP_L_post = io.imread("/Users/blancagilabertlopez/PIVA/incendi-pauls/LANDSAT/Landsat8_B4_B7_Pauls_postFoc_2026-04-27.tif")
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
imP_L_pre = io.imread("/Users/blancagilabertlopez/Desktop/projecte-PIVA/incendi-pauls/LANDSAT/Landsat8_B4_B7_Pauls_preFoc_2024-07-10.tif")
imP_L_pre_B4, imP_L_pre_B7 = imP_L_pre[:,:,0], imP_L_pre[:,:,1]
imP_L_post = io.imread("/Users/blancagilabertlopez/Desktop/projecte-PIVA/incendi-pauls/LANDSAT/Landsat8_B4_B7_Pauls_postFoc_2026-04-27.tif")
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


# %%
#-------------------------------------------------------------
# Incendi Artesa de Segre (AS) 2022 15/06/2022-23/06/2022
# Imatges obtingudes pre: 14-06-2021
#                    post: 09-07-2023
#-------------------------------------------------------------
#Setinel
imAS_S_B8A_pre = io.imread("/Users/blancagilabertlopez/PIVA/database/artesa-2022/SETINEL/2021-06-14-Sentinel-2_L2A_B8A_(Raw).tiff")
imAS_S_B12_pre = io.imread("/Users/blancagilabertlopez/PIVA/database/artesa-2022/SETINEL/2021-06-14-Sentinel-2_L2A_B12_(Raw).tiff")
imAS_S_B8A_post = io.imread("/Users/blancagilabertlopez/PIVA/database/artesa-2022/SETINEL/2023-07-09-Sentinel-2_L2A_B8A_(Raw).tiff")
imAS_S_B12_post = io.imread("/Users/blancagilabertlopez/PIVA/database/artesa-2022/SETINEL/2023-07-09-Sentinel-2_L2A_B12_(Raw).tiff")

#------NBR--------------------------------------------------
NBR_AS_S_pre = NBR(imAS_S_B8A_pre,imAS_S_B12_pre)
NBR_AS_S_post = NBR(imAS_S_B8A_post,imAS_S_B12_post)

#-------dNBR-------------------------------------
dNBR_AS_S = dNBR(NBR_AS_S_pre,NBR_AS_S_post)
#-------RBR----------------------------------------
RdNBR_AS_S = RdNBR(dNBR_AS_S, NBR_AS_S_pre)

#----Resultats------------------------------------
print(f"NBR pre min: {np.min(NBR_AS_S_pre):.4f}  max: {np.max(NBR_AS_S_pre):.4f}")
print(f"NBR post min: {np.min(NBR_AS_S_post):.4f}  max: {np.max(NBR_AS_S_post):.4f}")
print(f"dNBR min: {np.min(dNBR_AS_S):.4f}  max: {np.max(dNBR_AS_S):.4f}")
print(f"RdNBR min: {np.min(RdNBR_AS_S):.4f}  max: {np.max(RdNBR_AS_S):.4f}")

np.save("/Users/blancagilabertlopez/PIVA/database/artesa-2022/dNBR_AS_Setinel.npy",dNBR_AS_S)
np.save("/Users/blancagilabertlopez/PIVA/database/artesa-2022/RdNBR_AS_Setinel.npy",RdNBR_AS_S)

#---Plot------------------------------------------------------
plot.figure(figsize=(10,10))
plot.subplot(421)
plot.imshow(imAS_S_B8A_pre,cmap='gray')
plot.axis('off')
plot.title('Setinel B8A - Prefire')
plot.subplot(422)
plot.imshow(imAS_S_B12_pre,cmap='gray')
plot.axis('off')
plot.title('Setinel B12 - Prefire')
plot.subplot(423)
plot.imshow(imAS_S_B8A_post,cmap='gray')
plot.axis('off')
plot.title('Setinel B8A - Postfire')
plot.subplot(424)
plot.imshow(imAS_S_B12_post,cmap='gray')
plot.axis('off')
plot.title('Setinel B12 - Postfire')
plot.subplot(425)
plot.imshow(NBR_AS_S_pre,cmap='gray',vmin=-1,vmax=1)
plot.axis('off')
plot.title('NBR - PreFire')
plot.subplot(426)
plot.imshow(NBR_AS_S_post,cmap='gray',vmin=-1,vmax=1)
plot.axis('off')
plot.title('NBR - PostFire')
plot.subplot(427)
plot.imshow(dNBR_AS_S,cmap='RdYlGn_r',vmin=-0.5,vmax=1.3)
plot.colorbar()
plot.axis('off')
plot.title('dNBR Artesa de Segre Wildfire (2022) ')
plot.subplot(428)
plot.imshow(RdNBR_AS_S,cmap='RdYlGn_r',vmin=-0.5,vmax=1.3)
plot.colorbar()
plot.axis('off')
plot.title('RdNBR Artesa de Segre Wildfire (2022) ')
plot.tight_layout(h_pad=2,w_pad=1)
plot.savefig("/Users/blancagilabertlopez/PIVA/database/artesa-2022/AS-Setinel.png",dpi=150,bbox_inches='tight')
plot.show()


#%%
#--------------------------------------------
# Incendi Paüls (P) 07/07/2025-15/07/2025 
# SETINEL: dades obtingudes
#          pre: 09/05/2024
#          post: 23/06/2026
#--------------------------------------------
#Setinel
imP_S_B8A_pre = io.imread("/Users/blancagilabertlopez/PIVA/database/pauls-2025/Setinel/2024-05-09-Sentinel-2_L2A_B8A_(Raw).tiff")
imP_S_B12_pre = io.imread("/Users/blancagilabertlopez/PIVA/database/pauls-2025/Setinel/2024-05-09-Sentinel-2_L2A_B12_(Raw).tiff")
imP_S_B8A_post = io.imread("/Users/blancagilabertlopez/PIVA/database/pauls-2025/Setinel/2026-06-23-Sentinel-2_L2A_B8A_(Raw).tiff")
imP_S_B12_post = io.imread("/Users/blancagilabertlopez/PIVA/database/pauls-2025/Setinel/2026-06-23-Sentinel-2_L2A_B12_(Raw).tiff")

#------NBR--------------------------------------------------
NBR_P_S_pre = NBR(imP_S_B8A_pre,imP_S_B12_pre)
NBR_P_S_post = NBR(imP_S_B8A_post,imP_S_B12_post)

#-------dNBR-------------------------------------
dNBR_P_S = dNBR(NBR_P_S_pre,NBR_P_S_post)
#-------RBR----------------------------------------
RdNBR_P_S = RdNBR(dNBR_P_S, NBR_P_S_pre)

#----Resultats------------------------------------
print(f"NBR pre min: {np.min(NBR_P_S_pre):.4f}  max: {np.max(NBR_P_S_pre):.4f}")
print(f"NBR post min: {np.min(NBR_P_S_post):.4f}  max: {np.max(NBR_P_S_post):.4f}")
print(f"dNBR min: {np.min(dNBR_P_S):.4f}  max: {np.max(dNBR_P_S):.4f}")
print(f"RdNBR min: {np.min(RdNBR_P_S):.4f}  max: {np.max(RdNBR_P_S):.4f}")

np.save("/Users/blancagilabertlopez/PIVA/database/pauls-2025/dNBR_P_Setinel.npy",dNBR_P_S)
np.save("/Users/blancagilabertlopez/PIVA/database/pauls-2025/RdNBR_P_Setinel.npy",RdNBR_P_S)


#---Plot------------------------------------------------------
plot.figure(figsize=(10,10))
plot.subplot(421)
plot.imshow(imP_S_B8A_pre,cmap='gray')
plot.axis('off')
plot.title('Setinel B8A - Prefire')
plot.subplot(422)
plot.imshow(imP_S_B12_pre,cmap='gray')
plot.axis('off')
plot.title('Setinel B12 - Prefire')
plot.subplot(423)
plot.imshow(imP_S_B8A_post,cmap='gray')
plot.axis('off')
plot.title('Setinel B8A - Postfire')
plot.subplot(424)
plot.imshow(imP_S_B12_post,cmap='gray')
plot.axis('off')
plot.title('Setinel B12 - Postfire')
plot.subplot(425)
plot.imshow(NBR_P_S_pre,cmap='gray',vmin=-1,vmax=1)
plot.axis('off')
plot.title('NBR - PreFire')
plot.subplot(426)
plot.imshow(NBR_P_S_post,cmap='gray',vmin=-1,vmax=1)
plot.axis('off')
plot.title('NBR - PostFire')
plot.subplot(427)
plot.imshow(dNBR_P_S,cmap='RdYlGn_r',vmin=-0.5,vmax=1.3)
plot.colorbar()
plot.axis('off')
plot.title('dNBR Paüls Wildfire (2025) ')
plot.subplot(428)
plot.imshow(RdNBR_P_S,cmap='RdYlGn_r',vmin=-0.5,vmax=1.3)
plot.colorbar()
plot.axis('off')
plot.title('RdNBR Paüls Wildfire (2025) ')
plot.tight_layout(h_pad=2,w_pad=1)
plot.savefig("/Users/blancagilabertlopez/PIVA/database/pauls-2025/P-Setinel.png",dpi=150,bbox_inches='tight')
plot.show()


# %%
#---------------------------------------------------
# Incendi de la Ribera d'Ebre (RE) 26/06/2019-07/07/2019
# dades obtingudes amb Setinel:
#       pre: 15/06/2018
#       post: 19/07/2020
#---------------------------------------------------

#Setinel (S)
imRE_S_B8A_pre = io.imread("/Users/blancagilabertlopez/PIVA/database/ribera-2019/SETINEL/2018-06-15-Sentinel-2_L2A_B8A_(Raw).tiff")
imRE_S_B12_pre = io.imread("/Users/blancagilabertlopez/PIVA/database/ribera-2019/SETINEL/2018-06-15-Sentinel-2_L2A_B12_(Raw).tiff")
imRE_S_B8A_post = io.imread("/Users/blancagilabertlopez/PIVA/database/ribera-2019/SETINEL/2020-07-19-Sentinel-2_L2A_B8A_(Raw).tiff")
imRE_S_B12_post = io.imread("/Users/blancagilabertlopez/PIVA/database/ribera-2019/SETINEL/2020-07-19-Sentinel-2_L2A_B12_(Raw).tiff")
print(imRE_S_B8A_pre.shape)
print(imRE_S_B8A_post.shape)

#------NBR--------------------------------------------------
NBR_RE_S_pre = NBR(imRE_S_B8A_pre,imRE_S_B12_pre)
NBR_RE_S_post = NBR(imRE_S_B8A_post,imRE_S_B12_post)

#-------dNBR-------------------------------------
dNBR_RE_S = dNBR(NBR_RE_S_pre,NBR_RE_S_post)
#-------RBR----------------------------------------
RdNBR_RE_S = RdNBR(dNBR_RE_S, NBR_RE_S_pre)

#----Resultats------------------------------------
print(f"NBR pre min: {np.min(NBR_RE_S_pre):.4f}  max: {np.max(NBR_RE_S_pre):.4f}")
print(f"NBR post min: {np.min(NBR_RE_S_post):.4f}  max: {np.max(NBR_RE_S_post):.4f}")
print(f"dNBR min: {np.min(dNBR_RE_S):.4f}  max: {np.max(dNBR_RE_S):.4f}")
print(f"RdNBR min: {np.min(RdNBR_RE_S):.4f}  max: {np.max(RdNBR_RE_S):.4f}")

np.save("/Users/blancagilabertlopez/PIVA/database/ribera-2019/dNBR_RE_Setinel.npy",dNBR_RE_S)
np.save("/Users/blancagilabertlopez/PIVA/database/ribera-2019/RdNBR_RE_Setinel.npy",RdNBR_RE_S)

#---Plot------------------------------------------------------
plot.figure(figsize=(10,10))
plot.subplot(421)
plot.imshow(imRE_S_B8A_pre,cmap='gray')
plot.axis('off')
plot.title('Setinel B8A - Prefire')
plot.subplot(422)
plot.imshow(imRE_S_B12_pre,cmap='gray')
plot.axis('off')
plot.title('Setinel B12 - Prefire')
plot.subplot(423)
plot.imshow(imRE_S_B8A_post,cmap='gray')
plot.axis('off')
plot.title('Setinel B8A - Postfire')
plot.subplot(424)
plot.imshow(imRE_S_B12_post,cmap='gray')
plot.axis('off')
plot.title('Setinel B12 - Postfire')
plot.subplot(425)
plot.imshow(NBR_RE_S_pre,cmap='gray',vmin=-1,vmax=1)
plot.axis('off')
plot.title('NBR - PreFire')
plot.subplot(426)
plot.imshow(NBR_RE_S_post,cmap='gray',vmin=-1,vmax=1)
plot.axis('off')
plot.title('NBR - PostFire')
plot.subplot(427)
plot.imshow(dNBR_RE_S,cmap='RdYlGn_r',vmin=-0.5,vmax=1.3)
plot.colorbar()
plot.axis('off')
plot.title("dNBR Ribera d'Ebre Wildfire (2019) ")
plot.subplot(428)
plot.imshow(RdNBR_RE_S,cmap='RdYlGn_r',vmin=-0.5,vmax=1.3)
plot.colorbar()
plot.axis('off')
plot.title("RdNBR Ribera d'Ebre Wildfire (2019) ")
plot.tight_layout(h_pad=2,w_pad=1)
plot.savefig("/Users/blancagilabertlopez/PIVA/database/ribera-2019/RE-Setinel.png",dpi=150,bbox_inches='tight')
plot.show()
# %%
#---Incendi Segarra (SE) 01/07/2025-----------------------
# Dades obtingudes amb Setinel
#       pre: 18/06/2024
#       post: 18/06/2026
#---------------------------------------------------------

#Setinel (S)
imSE_S_B8A_pre = io.imread("/Users/blancagilabertlopez/PIVA/database/segarra-2025/SETINEL/2024-06-18-Sentinel-2_L2A_B8A_(Raw).tiff")
imSE_S_B12_pre = io.imread("/Users/blancagilabertlopez/PIVA/database/segarra-2025/SETINEL/2024-06-18-Sentinel-2_L2A_B12_(Raw).tiff")
imSE_S_B8A_post = io.imread("/Users/blancagilabertlopez/PIVA/database/segarra-2025/SETINEL/2026-06-18-Sentinel-2_L2A_B8A_(Raw).tiff")
imSE_S_B12_post = io.imread("/Users/blancagilabertlopez/PIVA/database/segarra-2025/SETINEL/2026-06-18-Sentinel-2_L2A_B12_(Raw).tiff")
print(imSE_S_B8A_pre.shape)
print(imSE_S_B8A_post.shape)

#------NBR--------------------------------------------------
NBR_SE_S_pre = NBR(imSE_S_B8A_pre,imSE_S_B12_pre)
NBR_SE_S_post = NBR(imSE_S_B8A_post,imSE_S_B12_post)

#-------dNBR-------------------------------------
dNBR_SE_S = dNBR(NBR_SE_S_pre,NBR_SE_S_post)
#-------RBR----------------------------------------
RdNBR_SE_S = RdNBR(dNBR_SE_S, NBR_SE_S_pre)

#----Resultats------------------------------------
print(f"NBR pre min: {np.min(NBR_SE_S_pre):.4f}  max: {np.max(NBR_SE_S_pre):.4f}")
print(f"NBR post min: {np.min(NBR_SE_S_post):.4f}  max: {np.max(NBR_SE_S_post):.4f}")
print(f"dNBR min: {np.min(dNBR_SE_S):.4f}  max: {np.max(dNBR_SE_S):.4f}")
print(f"RdNBR min: {np.min(RdNBR_SE_S):.4f}  max: {np.max(RdNBR_SE_S):.4f}")

np.save("/Users/blancagilabertlopez/PIVA/database/segarra-2025/dNBR_SE_Setinel.npy",dNBR_SE_S)
np.save("/Users/blancagilabertlopez/PIVA/database/segarra-2025/RdNBR_SE_Setinel.npy",RdNBR_SE_S)


#---Plot------------------------------------------------------
plot.figure(figsize=(10,10))
plot.subplot(421)
plot.imshow(imSE_S_B8A_pre,cmap='gray')
plot.axis('off')
plot.title('Setinel B8A - Prefire')
plot.subplot(422)
plot.imshow(imSE_S_B12_pre,cmap='gray')
plot.axis('off')
plot.title('Setinel B12 - Prefire')
plot.subplot(423)
plot.imshow(imSE_S_B8A_post,cmap='gray')
plot.axis('off')
plot.title('Setinel B8A - Postfire')
plot.subplot(424)
plot.imshow(imSE_S_B12_post,cmap='gray')
plot.axis('off')
plot.title('Setinel B12 - Postfire')
plot.subplot(425)
plot.imshow(NBR_SE_S_pre,cmap='gray',vmin=-1,vmax=1)
plot.axis('off')
plot.title('NBR - PreFire')
plot.subplot(426)
plot.imshow(NBR_SE_S_post,cmap='gray',vmin=-1,vmax=1)
plot.axis('off')
plot.title('NBR - PostFire')
plot.subplot(427)
plot.imshow(dNBR_SE_S,cmap='RdYlGn_r',vmin=-0.5,vmax=1.3)
plot.colorbar()
plot.axis('off')
plot.title("dNBR Torrefeta (La Segarra) Wildfire (2025) ")
plot.subplot(428)
plot.imshow(RdNBR_SE_S,cmap='RdYlGn_r',vmin=-0.5,vmax=1.3)
plot.colorbar()
plot.axis('off')
plot.title("RdNBR Torrefeta (La Segarra) Wildfire (2025) ")
plot.tight_layout(h_pad=2,w_pad=1)
plot.savefig("/Users/blancagilabertlopez/PIVA/database/segarra-2025/SE-Setinel.png",dpi=150,bbox_inches='tight')
plot.show()
# %%
