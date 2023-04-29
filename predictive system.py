# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:53:29 2023

@author: ASUS
"""

import numpy as np 
import pickle
from sklearn.preprocessing import StandardScaler


# loading the saved model
loaded_model = pickle.load(open('C:/diabetis prediction model/trained_model.sav' , 'rb'))

input_data = (4,110,92,0,0,37.6,0.191,30)
#changing the input data into the numpy arrray
input_data_as_numpy_array = np.asarray(input_data)
# reshape the array as we predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
## standardize the input data
scaler = StandardScaler()
scaler.fit(input_data_reshaped)
standardized_data = scaler.transform(input_data_reshaped)
std_data = scaler.transform(standardized_data)
print(std_data)
prediction = loaded_model.predict(std_data)
print(prediction)


if (prediction[0] == 0):
  print('the person is not diabetic')
else:
  print('the person is diabetic')