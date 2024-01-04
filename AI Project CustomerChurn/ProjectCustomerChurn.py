
import pandas as pd

df = pd.read_csv("customer_churn.csv")
print(df.head())
print(df.describe())
print(df.info())
#A.

total_male_customers = df[df['gender']=='Male'].shape[0]  
print("Total_male_customers:",total_male_customers)


total_dsl_customers = df[df['InternetService'] == 'DSL'].shape[0]
print("Total_dsl_customers:",total_dsl_customers)


new_customer = df[(df['gender'] == 'Female') & (df['SeniorCitizen'] == 1) & (df['PaymentMethod'] == 'Mailed check')]
print("New Cutomers:\n",new_customer)


df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
new_customer = df[(df['tenure'] < 10) | (df['TotalCharges'] < 500)]
print("New Customer:\n",new_customer)

#B.

from matplotlib import pyplot as plt

churn_counts = df['Churn'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(churn_counts,labels=churn_counts.index ,autopct='%1.1f%%')
plt.title("Churn Distribtion")
plt.show()


#
internet_service_counts = df['InternetService'].value_counts()
plt.figure(figsize=(8,6))
plt.bar(internet_service_counts.index, internet_service_counts.values)
plt.xlabel("Internet Service")
plt.ylabel("Count")
plt.title("Internet Service Distribution")
plt.show()

#C.
from keras.models import Sequential
from keras.layers import Dense , Dropout   
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import numpy as np

df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

X = df[['tenure']]
y= df[['Churn']]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#a.1st Sequential Model
print("1. Sequential Model \n")
model1 = Sequential()
model1.add(Dense(12,input_dim=1,activation='relu'))
model1.add(Dense(8,activation='relu'))
model1.add(Dense(1,activation='sigmoid'))
model1.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model1.fit(X_train,y_train,epochs=150)
y_pred1 = model1.predict(X_test)
y_pred1 =(y_pred1 > 0.5)
confusion_matrix1 = confusion_matrix(y_test,y_pred1)



#b.2nd Model Model with Dropout
print("2.nd Model with Dropout layers \n")
model2 = Sequential()
model2.add(Dense(12,input_dim=1,activation='relu'))
model2.add(Dropout(0.3))
model2.add(Dense(8,activation='relu'))
model2.add(Dropout(0.2))
model2.add(Dense(1,activation='sigmoid'))
model2.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model2.fit(X_train,y_train,epochs=150)
y_pred2 =model2.predict(X_test)
y_pred2 =(y_pred2 > 0.5)
cusfusion_matrix2 = confusion_matrix(y_test,y_pred2)


#c. 3rd Model With mutiple features
print("3.rd Model With multiple features \n")
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

X = df[['tenure','MonthlyCharges','TotalCharges']]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model3 = Sequential()
model3.add(Dense(12,input_dim=3,activation='relu'))
model3.add(Dense(8,activation='relu'))
model3.add(Dense(1,activation='sigmoid'))
model3.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model3.fit(X_train,y_train,epochs=150)
y_pred3 = model3.predict(X_test)
y_pred3 =(y_pred3 > 0.5)
confusion_matrix3 = confusion_matrix(y_test,y_pred3)

#plot 'Accuracy' VS 'Epochs'
if 'acc' in model1.history.history:
    plt.plot(np.arange(1,151),model1.history.history['acc'])
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("Accuracy Vs Epochs - Model 1")
plt.show()

#Model2 

if 'acc' in model2.history.history:
    plt.plot(np.arange(1,151),model2.history.history['acc'])
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title(" Accuracy Vs  Epochs - Model2")
plt.show()

#Model3
if 'acc' in model1.history.history:
    plt.plot(np.arange(1,151),model3.history.history['acc'])
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title(" Accuracy Vs  Epochs - Model3")
plt.show()