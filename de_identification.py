import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats, random
from scipy.interpolate import interp1d
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt

#Provide the ground truth, i.e. the .csv file outputted by OpenFace processing the RADVESS' Actor video.
df_1 = pd.read_csv("Actor.csv")

x_au1 = (df_1[' AU01_r']).to_numpy()
x_au2 = (df_1[' AU02_r']).to_numpy()
x_au4 = (df_1[' AU04_r']).to_numpy()
x_au5 = (df_1[' AU05_r']).to_numpy()
x_au6 = (df_1[' AU06_r']).to_numpy()
x_au7 = (df_1[' AU07_r']).to_numpy()
x_au9 = (df_1[' AU09_r']).to_numpy()
x_au10 = (df_1[' AU10_r']).to_numpy()
x_au12 = (df_1[' AU12_r']).to_numpy()
x_au14 = (df_1[' AU14_r']).to_numpy()
x_au15 = (df_1[' AU15_r']).to_numpy()
x_au17 = (df_1[' AU17_r']).to_numpy()
x_au20 = (df_1[' AU20_r']).to_numpy()
x_au23 = (df_1[' AU23_r']).to_numpy()
x_au25 = (df_1[' AU25_r']).to_numpy()
x_au26 = (df_1[' AU26_r']).to_numpy()
x_au45 = (df_1[' AU45_r']).to_numpy()

#Provide the swapped_files, i.e. the .csv files outputted by OpenFace processing the DFaker, DeepFaceLab, Fceswap and Faceswap-GAN swapped videos.
df_2 = pd.read_csv("Actor_DF.csv")
df_3 = pd.read_csv("Actor_DFL.csv")
df_4 = pd.read_csv("Actor_FS.csv")
df_5 = pd.read_csv("Actor_FSG.csv")

df_tot=[df_2, df_3, df_4, df_5]

#De-Id comparison between Original video and Swapped videos belonging to a single RADVESS' Actor.
for df in df_tot:

    y_au1 = (df[' AU01_r']).to_numpy()
    y_au2 = (df[' AU02_r']).to_numpy()
    y_au4 = (df[' AU04_r']).to_numpy()
    y_au5 = (df[' AU05_r']).to_numpy()
    y_au6 = (df[' AU06_r']).to_numpy()
    y_au7 = (df[' AU07_r']).to_numpy()
    y_au9 = (df[' AU09_r']).to_numpy()
    y_au10 = (df[' AU10_r']).to_numpy()
    y_au12 = (df[' AU12_r']).to_numpy()
    y_au14 = (df[' AU14_r']).to_numpy()
    y_au15 = (df[' AU15_r']).to_numpy()
    y_au17 = (df[' AU17_r']).to_numpy()
    y_au20 = (df[' AU20_r']).to_numpy()
    y_au23 = (df[' AU23_r']).to_numpy()
    y_au25 = (df[' AU25_r']).to_numpy()
    y_au26 = (df[' AU26_r']).to_numpy()
    y_au45 = (df[' AU45_r']).to_numpy()

    matrix_1=np.matrix([x_au1,x_au2,x_au4,x_au5,x_au6,x_au7,x_au9,x_au10,x_au12,x_au14,x_au15,x_au17,x_au20,x_au23,x_au25,x_au26,x_au45])
    plt.figure()
    y_axis_labels = ["AU_1","AU_2","AU_4","AU_5","AU_6","AU_7","AU_9","AU_10","AU_12","AU_14","AU_15","AU_17","AU_20","AU_23","AU_25","AU_26","AU_45"]
    sns.heatmap(matrix_1, yticklabels=y_axis_labels)

    matrix_2=np.matrix([y_au1,y_au2,y_au4,y_au5,y_au6,y_au7,y_au9,y_au10,y_au12,y_au14,y_au15,y_au17,y_au20,y_au23,y_au25,y_au26,y_au45])
    plt.figure()
    sns.heatmap(matrix_2, yticklabels=y_axis_labels)

    plt.figure()
    corcoeff_tot=np.array([])
    rmse_tot=np.array([])

    #PCC and RMSE between each AU from Original video and Swapped videos.
    for index, (row_1, row_2) in enumerate(zip(matrix_1, matrix_2), start=1):
        row_1=np.squeeze(np.asarray(row_1))
        row_2=np.squeeze(np.asarray(row_2))
        corcoeff_tot=np.append(corcoeff_tot, np.corrcoef(row_1,row_2)[0,1])
        rmse_tot=np.append(rmse_tot, sqrt(mean_squared_error(row_1, row_2)))
        print(np.around(np.corrcoef(row_1,row_2)[0,1], decimals=3), np.around(sqrt(mean_squared_error(row_1, row_2)), decimals=3))

        plt.subplot(5, 4, index)
        plt.plot(row_1)
        plt.plot(row_2)

    print 'CorCoef: ', np.around(np.mean(corcoeff_tot), decimals=3), 'StdDev: ', np.around(np.std(corcoeff_tot), decimals=3)
    print 'Rmse: ', np.around(np.mean(rmse_tot), decimals=3), 'StdDev: ', np.around(np.std(rmse_tot), decimals=3)

plt.show()