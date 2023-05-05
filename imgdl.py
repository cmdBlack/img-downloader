#!/usr/bin/env python
# coding: utf-8

# In[13]:


import requests
import os

parent_dir = input("Working Directory? ")
path1 = os.path.join(parent_dir, "500hPa")
path2 = os.path.join(parent_dir, "700hPa")
path3 = os.path.join(parent_dir, "850hPa")
path4 = os.path.join(parent_dir, "MSLP")
path5 = os.path.join(parent_dir, "3hrly-RR")
path6 = os.path.join(parent_dir, "SW")
path7 = os.path.join(parent_dir, "NL")
path8 = os.path.join(parent_dir, "12km-WRF")

os.mkdir(path1)
os.mkdir(path2)
os.mkdir(path3)
os.mkdir(path4)
os.mkdir(path5)
os.mkdir(path6)
os.mkdir(path7)
os.mkdir(path8)


pointer = 3 
pointer_nl = 100


image_url500 = []
image_url700 = []
image_url850 = []
image_urlSW = []
image_urlMSLP = []
image_urlRR = []
image_urlNL = []
image_urlWRF = []

for i in range(1, 16):
    if pointer < 10:
        image_url1 = 'https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/500winds/GSM_Phl_500hPa_Wind_00' + str(pointer) + 'h.png'
        image_url2 = 'https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/700winds/GSM_Phl_700hPa_Wind_00' + str(pointer) + 'h.png'
        image_url3 = 'https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/850winds/GSM_Phl_850hPa_Wind_00' + str(pointer) + 'h.png'
        image_url4 = 'https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/winds/GSM_Phl_Sfc_Wind_00' + str(pointer) + 'h.png'
        image_url5 = 'https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/pressure/GSM_Phl_Sfc_MSLP_00' + str(pointer) + 'h.png'
        image_url6 = 'https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/24hr/GSM_Phl_Sfc_RR_3hrly_00' + str(pointer) + 'h.png'
    
    else:
        image_url1 = 'https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/500winds/GSM_Phl_500hPa_Wind_0' + str(pointer) + 'h.png'
        image_url2 = 'https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/700winds/GSM_Phl_700hPa_Wind_0' + str(pointer) + 'h.png'
        image_url3 = 'https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/850winds/GSM_Phl_850hPa_Wind_0' + str(pointer) + 'h.png'
        image_url4 = 'https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/winds/GSM_Phl_Sfc_Wind_0'+ str(pointer) + 'h.png'
        image_url5 = 'https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/pressure/GSM_Phl_Sfc_MSLP_0'+ str(pointer) + 'h.png'
        image_url6 = 'https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/24hr/GSM_Phl_Sfc_RR_3hrly_0' + str(pointer) + 'h.png'
    
    image_url500.append(image_url1)
    image_url700.append(image_url2)
    image_url850.append(image_url3)
    image_urlSW.append(image_url4)
    image_urlMSLP.append(image_url5)
    image_urlRR.append(image_url6)
    pointer += 3

for j in range(1, 49):
    if pointer_nl < 1000:
        image_url7 = 'https://pubfiles.pagasa.dost.gov.ph/nms/wrf/prsd/nl/d02/pcp_cc_1hr/nl_pcp_cc_1hr_d02_f00'+ str(pointer_nl) + '.png'
    else:
        image_url7 = 'https://pubfiles.pagasa.dost.gov.ph/nms/wrf/prsd/nl/d02/pcp_cc_1hr/nl_pcp_cc_1hr_d02_f0'+ str(pointer_nl) + '.png'
    
    image_urlNL.append(image_url7)
    pointer_nl += 100
    
pointer_nl = 100
for k in range(1, 145):
    if pointer_nl < 1000:
        image_url8 = 'https://pubfiles.pagasa.dost.gov.ph/nms/wrf/d01/pcp_1hr/pcp_1hr_d01_f00'+ str(pointer_nl) + '.png'
    elif pointer_nl < 10000:
        image_url8 = 'https://pubfiles.pagasa.dost.gov.ph/nms/wrf/d01/pcp_1hr/pcp_1hr_d01_f0' + str(pointer_nl) + '.png'
    else:
        image_url8 = 'https://pubfiles.pagasa.dost.gov.ph/nms/wrf/d01/pcp_1hr/pcp_1hr_d01_f' + str(pointer_nl) + '.png'
    
    image_urlWRF.append(image_url8)
    pointer_nl += 100
    


folder500 = parent_dir + '/500hPa/'
folder700 = parent_dir + '/700hPa/'
folder850 = parent_dir + '/850hPa/'
folderSW = parent_dir + '/SW/'
folderMSLP = parent_dir + '/MSLP/'
folderNL = parent_dir + '/NL/'
folderWRF = parent_dir + '/12km-WRF/'
folderRR = parent_dir + '/3hrly-RR/'

for url in image_url500:
    print(url)
    img_data = requests.get(url).content
    with open(folder500 + url.lstrip("https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/500winds/"), 'wb') as handler:
        handler.write(img_data)
        
for url in image_url700:
    print(url)
    img_data = requests.get(url).content
    with open(folder700 + url.lstrip("https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/700winds/"), 'wb') as handler:
        handler.write(img_data)
        
for url in image_url850:
    print(url)
    img_data = requests.get(url).content
    with open(folder850 + url.lstrip("https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/850winds/"), 'wb') as handler:
        handler.write(img_data)
        
for url in image_urlSW:
    print(url)
    img_data = requests.get(url).content
    with open(folderSW + url.lstrip("https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/winds/"), 'wb') as handler:
        handler.write(img_data)

for url in image_urlMSLP:
    print(url)
    img_data = requests.get(url).content
    with open(folderMSLP + url.lstrip("https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/pressure/"), 'wb') as handler:
        handler.write(img_data)

for url in image_urlRR:
    print(url)
    img_data = requests.get(url).content
    with open(folderRR + url.lstrip("https://pubfiles.pagasa.dost.gov.ph/tamss/nwp/gsm/24hr/"), 'wb') as handler:
        handler.write(img_data)

q = 100  
prefix1 = 'pcp_1hr_d01_f00'
prefix2 = 'pcp_1hr_d01_f0'
for url in image_urlNL:
    print(url)
    img_data = requests.get(url).content
    if q < 1000: 
        with open(folderNL + prefix1 + str(q) + '.png', 'wb') as handler:
            handler.write(img_data)
    else:
        with open(folderNL + prefix2 + str(q) + '.png', 'wb') as handler:
            handler.write(img_data)        
    q += 100
    
w = 100  
prefix3 = 'nl_pcp_cc_1hr_d02_f00'
prefix4 = 'nl_pcp_cc_1hr_d02_f0'
prefix5 = 'nl_pcp_cc_1hr_d02_f'
for url in image_urlWRF:
    print(url)
    img_data = requests.get(url).content
    if w < 1000: 
        with open(folderWRF + prefix3 + str(w) + '.png', 'wb') as handler:
            handler.write(img_data)
    elif w < 10000: 
        with open(folderWRF + prefix4 + str(w) + '.png', 'wb') as handler:
            handler.write(img_data)
    else:
        with open(folderWRF + prefix5 + str(w) + '.png', 'wb') as handler:
            handler.write(img_data)        
    w += 100
        
print("done")   
        


# In[ ]:




