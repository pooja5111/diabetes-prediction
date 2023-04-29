# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:07:49 2023

@author: ASUS
"""

import numpy as np
import pickle
import streamlit as st
import time
from sklearn.preprocessing import StandardScaler


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://media.istockphoto.com/id/1426316422/vector/deep-blue-grungy-art-abstract-header-design.jpg?s=612x612&w=0&k=20&c=Cn-VT_TCJUJXzBF_4R-CIW9Kh6bj--UHD_4SKYNqXMw=");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image:url("https://images.saymedia-content.com/.image/t_share/MTkzODU1MjgzMjUxMTkzMzI4/svg-wave-generator.gif");}
    background-attachment: fixed;
    background-size: cover
}
</style>
""",
unsafe_allow_html=True
)
add_bg_from_url() 




# loading the saved model
loaded_model = pickle.load(open('C:/diabetis prediction model/trained_model.sav' , 'rb'))

# cr4eating a function for prediction

def diabetes_prediction(input_data):
    
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
      return'the person is not diabetic'
    else:
      return'the person is diabetic'


def main():
    
    # gving a title
    st.sidebar.title('Diabetes Prediction Web App')
    

    
    # getting the input data from the user
    # Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the person')
    
    
    # code for prediction
    diagnosis = ''
    
    # cr4eating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
        
    st.success(diagnosis)
    
    
#col1, col2, col3 = st.columns([1,2,1])
    
    

                       
    
    
if __name__ == '__main__':
    main()
    
    
if "photo" not in st.session_state:
    st.session_state["photo"]="Not Done"
    
def change_photo_state():
    st.session_state["photo"]="Done"
    
uploaded_photo = st.file_uploader("Upload A Photo Of Prescribtion (Optional)", on_change=change_photo_state)
if st.session_state["photo"] == "Done":
 progress_bar = st.progress(0)
 for perc_complete in range(100):
    time.sleep(0.05)
    progress_bar.progress(perc_complete+1)

 st.success("Photo Uploaded successfully!")

with st.expander("Click to read more"):
    st.write("Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.Your body breaks down most of the food you eat into sugar (glucose) and releases it into your bloodstream. When your blood sugar goes up, it signals your pancreas to release insulin. Insulin acts like a key to let the blood sugar into your body’s cells for use as energy.")



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       