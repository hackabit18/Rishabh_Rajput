import numpy as np
import pandas as pd
import glob
import os
import skimage.io as io
from skimage.transform import rescale, resize
import skimage.color as co

data = []
i = 0

landmark_list = ['Dataset/Train/Unlabelled', 'Dataset/Train/Charminar','Dataset/Train/GatewayofIndia', 'Dataset/Train/GoldenTemple', 'Dataset/Train/GolGumbaz', 'Dataset/Train/HawaMahal', 'Dataset/Train/HumayunsTomb', 'Dataset/Train/IndiaGate', 'Dataset/Train/LotusTemple', 'Dataset/Train/QutubMinar', 'Dataset/Train/RashtrapatiBhavan', 'Dataset/Train/RedFort','Dataset/Train/SanchiStupa','Dataset/Train/SeCathedral','Dataset/Train/TajMahal']
#landmark_list = ['Dataset/Train/GoldenTemple', 'Dataset/Train/GolGumbaz', 'Dataset/Train/HawaMahal', 'Dataset/Train/HumayunsTomb', 'Dataset/Train/IndiaGate', 'Dataset/Train/LotusTemple']

for imgnm in landmark_list:
	print(imgnm)
	imgnmlist = glob.glob(os.path.join(imgnm,'*.jpeg'))
	empty_list = []
	a = np.ones(len(imgnmlist))
	for item in imgnmlist :
		img = io.imread(item)
		img1 = co.rgb2hsv(resize(img, (32,32,3),anti_aliasing=False))
		rgb_img = np.reshape(img1,(32*32*3))
		empty_list.append(rgb_img)
	empty_list=np.array(empty_list)
	new_list=np.zeros(shape=(len(empty_list),32*32*3+1))
	new_list[:,0]= a*i
	new_list[:, 1:] = empty_list
	data.append(np.array(new_list))
	a=list(a)
	a.clear()
	empty_list=list(empty_list)
	empty_list.clear()
	new_list=list(new_list)
	new_list.clear()
	print(i)
	i+=1

arra = np.concatenate(data, axis=0)
print(arra.shape)
df = pd.DataFrame(arra)

df.to_csv("train_data1.csv", index=False, header=None)
