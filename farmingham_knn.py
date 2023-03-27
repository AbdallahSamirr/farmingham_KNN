# -*- coding: utf-8 -*-
"""farmingham_KNN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DKBXjLrcr3Uk5q_Dmu4kPlSh8Ypufxqz
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import plotly.express as px

df = pd.read_csv('/content/framingham.csv')

df.head()

df.info()

df.describe().T

sns.countplot(x='male',data=df)
plt.show()

df['age'].value_counts().sort_values()

sns.countplot(x='currentSmoker',data=df)
plt.show()

df['currentSmoker'].value_counts()

df.columns

display(px.pie(df['BPMeds'].value_counts().reset_index().rename(columns={'index':'Type'}), values='BPMeds', names='Type', title='Blood Pressure Medications'))

df['BPMeds'].value_counts()

df['prevalentStroke'].value_counts().plot.pie(autopct='%.1f%%')
plt.show()

df['prevalentHyp'].value_counts().plot.pie(autopct='%.1f%%')
plt.show()

sns.countplot(x='diabetes',data=df)
plt.show()

df['diabetes'].value_counts()

sns.displot(data=df,x='totChol',kind='kde')
plt.show()

sns.displot(data=df, x="totChol", kde=True)
plt.show()

cholMean=df['totChol'].mean()
cholMedian=df['totChol'].median()
print(cholMean,cholMedian)

df.columns

sns.displot(data=df,x='sysBP',kind='kde')
plt.show()

df['sysBP'].mean()

df.columns

sns.displot(data=df,x='diaBP',kind='kde')
plt.show()

df['diaBP'].mean()

df['diaBP'].median()

sns.displot(data=df,x='heartRate',kind='kde')
plt.show()

sns.displot(data=df,x='glucose',kde=True)
plt.show()

df['TenYearCHD'].value_counts().plot.pie(autopct='%.1f%%')
plt.show()

df.isna().sum()

df['education']

plt.figure(figsize=(12,8))
sns.heatmap(df.corr(),annot=True,fmt='.2f')
plt.show()

df.corrwith(df['TenYearCHD']).sort_values()

df.duplicated().sum()

df.isna().sum()

education_mean = df['education'].mean()

df['education'].fillna(education_mean,inplace=True)

cigs_median=df['cigsPerDay'].median()

df['cigsPerDay'].fillna(cigs_median,inplace=True)

bp_mean=df['BPMeds'].mean()

df['BPMeds'].fillna(bp_mean,inplace=True)

chol_mean=df['totChol'].mean()

df['totChol'].fillna(chol_mean,inplace=True)

bmi_mean =df['BMI'].mean()

df['BMI'].fillna(bmi_mean,inplace=True)

HR_mean=df['heartRate'].mean()
df['heartRate'].fillna(HR_mean,inplace=True)

glucose_mean = df['glucose'].mean()

df['glucose'].fillna(glucose_mean,inplace=True)

df.isna().sum()

df.hist(bins = 50 , figsize = (15,12))
plt.show()

df2 = df.drop(['male','education','diabetes','prevalentHyp','prevalentStroke','BPMeds'],axis=1)

df2.info()

x=df2.iloc[:,0:9]
x

y = df.iloc[:, -1].values
y

from imblearn.over_sampling import SMOTE

sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(x, y)

X_res

df_resampled=X_res

df_resampled['output_resampled'] = y_res

sns.countplot(x='output_resampled',data=df_resampled)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X_res, y_res, test_size = 0.33, random_state = 0)

from sklearn.preprocessing import StandardScaler

Sc=StandardScaler()

X_train_Scaled=Sc.fit_transform(x_train)

X_test_Scaled=Sc.fit_transform(x_test)

from sklearn.neighbors import KNeighborsClassifier

KNN_classifier=KNeighborsClassifier(n_neighbors=10)

KNN_classifier.fit(X_train_Scaled,y_train)

y_pred_knn=KNN_classifier.predict(X_test_Scaled)

y_pred_knn

print("Training set score: {:.3f}".format(KNN_classifier.score(X_train_Scaled, y_train)))
print("Test set score: {:.3f}".format(KNN_classifier.score(X_test_Scaled, y_test)))

from sklearn.metrics import confusion_matrix

cm=confusion_matrix(y_pred_knn,y_test)
cm

