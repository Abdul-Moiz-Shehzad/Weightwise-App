# Weightwise App

## Overview

The **Weightwise App** is a predictive application designed to predict obesity based on various health-related features. It is built using machine learning models, with a focus on Random Forest, which provided the best performance with an accuracy of 84%. The app uses a dataset from [Kaggle's Obesity Prediction Dataset](https://www.kaggle.com/datasets/ruchikakumbhar/obesity-prediction) to train and make predictions.

## Dataset

The dataset used for training the model is sourced from Kaggle, which can be found [here](https://www.kaggle.com/datasets/ruchikakumbhar/obesity-prediction). It includes various health-related features such as Age, Weight, and Family History, among others, with the target variable being "Obesity".

### Data Preprocessing

1. **Categorical Columns to Numeric**:  
   The categorical columns were converted into numeric values using **One-Hot Encoding** via `pd.get_dummies` to ensure the data is in a format suitable for model training.

2. **Label Encoding**:  
   The target variable, "Obesity", was encoded using **Label Encoding** from `sklearn.preprocessing.LabelEncoder` to transform the target into a numerical form (0 for non-obese, 1 for obese).

3. **Correlation Analysis**:  
   We performed a correlation analysis and found that obesity was mainly dependent on the following features:
   - Age
   - Weight
   - family_history_yes
   - family_history_no
   - CAEC_Frequently
   - CAEC_Sometimes

## Model Training

Several models were trained on the dataset, including **Decision Trees**, **Logistic Regression**, and **Random Forest**. After evaluating the performance of these models, **Random Forest** proved to be the best with an accuracy of **84%**.

The model was then serialized using **Pickle** to save the trained model and the label encoder for later use in the web app.

## Web Application (Streamlit)

A **Streamlit** app was developed to allow users to input the necessary features and predict the likelihood of obesity based on their inputs.

### Features:
- Users can input:
  - Age
  - Weight
  - Family history (Yes/No)
  - Frequency of food between meals (Frequently/Sometimes)
- The app loads the pre-trained model and label encoder to make predictions on the user's data.

The model and encoder are loaded using **Pickle**, ensuring efficient predictions on new data.

## Dockerization

The app is containerized using **Docker**, making it easy to deploy and run in any environment.

### Docker Setup:
- **Dockerfile**: The Dockerfile was set up to:
  - Install the required dependencies from `requirements.txt`.
  - Build and run the Streamlit app.

## CI/CD Pipeline

A GitHub Actions workflow was configured for CI/CD to automatically deploy the app to Render every time changes are pushed to the main branch.

### GitHub Actions Workflow:

- Checkout: Check out the latest code from the GitHub repository.
- Build Docker Image: Build the Docker image for the app.
- Deploy to Render: Trigger the deployment using Render's API.

## How to Use

To run locally

1. Clone the repository to your local machine:
```
git clone https://github.com/Abdul-Moiz-Shehzad/Weightwise-App
cd Weightwise-App
```
2. Install required dependencies
```
pip install -r requirements.txt
```
3. Run the streamlit app locally
``` 
streamlit run app.py
```
