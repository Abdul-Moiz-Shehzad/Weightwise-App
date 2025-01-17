import streamlit as st
import pickle
import numpy as np
RF_model=pickle.load(open("RandomForestModel.pkl","rb"))
LabelEncoder=pickle.load(open("LabelEncoder.pkl","rb"))

st.header("WeightWise APP")
Age=st.number_input("Age")
Weight=st.number_input("Weight in Kgs")
family_history=st.selectbox("Has a family member suffered or suffers from overweight?", ['yes','no'])
family_history_yes=1 if family_history=='yes' else 0
family_history_no=1 if family_history=='no' else 0

food_between_meals=st.selectbox("Do you eat any food between meals?",["frequently","sometimes"])
food_between_meals_frequently=1 if food_between_meals=="frequently" else 0
food_between_meals_sometimes=1 if food_between_meals=="sometimes" else 0

predict=st.button("Predict")
if predict:
    features = np.array([Age, Weight, family_history_yes, family_history_no,food_between_meals_frequently, food_between_meals_sometimes])
    features_reshaped = features.reshape(1, -1) 
    output = RF_model.predict(features_reshaped)
    output=LabelEncoder.inverse_transform(output.reshape(-1,1))
    st.subheader("Prediction:")
    st.code(output[0])
    st.markdown("""
**Disclaimer:** Although the model's accuracy is 84%, it may not produce accurate results because it is trained on a smaller dataset and may not generalize well to unseen or random values. If very random values are inputted, the model might crash or produce irregular results.
""")