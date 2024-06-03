# Import Libraries
import prediction 
import streamlit as st
import pandas as pd
import joblib
import eda

# Set Option
st.set_option('deprecation.showPyplotGlobalUse', False)

# Header
st.header('Predicting Diabetes Status')
st.write("""
Created by Fazrin Muhammad

This project aims to use machine learning classification methods on the diabetes status to predict whether a patient have non diabetes or diabetes.
""")

@st.cache_data
def fetch_data():
    df = pd.read_csv('diabetes_binary_health_indicators_BRFSS2021.csv')
    return df

df = fetch_data()
st.write("""Diabetes Status""")
st.write(df)

def main():
    st.title("Predicting Diabetes Status App")

def user_input():
    HighBP = st.selectbox("Do you have high blood pressure?", options=[0.0, 1.0], index=1)
    HighChol = st.selectbox("Do you have high cholesterol?", options=[0.0, 1.0], index=1)
    CholCheck = st.selectbox("Have you ever had your cholesterol checked?", options=[0.0, 1.0], index=1)
    BMI = st.number_input("Enter BMI", min_value=1, max_value=100, value=50, step=1)
    Smoker = st.selectbox("Are you a smoker?", options=[0.0, 1.0], index=1)
    Stroke = st.selectbox("Have you ever had a stroke?", options=[0.0, 1.0], index=1)
    HeartDiseaseorAttack = st.selectbox("Have you ever had heart disease or a heart attack?", options=[0.0, 1.0], index=1)
    PhysActivity = st.selectbox("Do you engage in physical activity?", options=[0.0, 1.0], index=1)
    Fruits = st.selectbox("Do you eat fruits?", options=[0.0, 1.0], index=1)
    Veggies = st.selectbox("Do you eat vegetables?", options=[0.0, 1.0], index=1)
    HvyAlcoholConsump = st.selectbox("Do you consume alcohol heavily?", options=[0.0, 1.0], index=1)
    AnyHealthcare = st.selectbox("Do you have any form of healthcare?", options=[0.0, 1.0], index=1)
    NoDocbcCost = st.selectbox("Is there a time you did not see a doctor because of cost?", options=[0.0, 1.0], index=1)
    GenHlth = st.number_input("Enter GenHlth", min_value=1, max_value=5, value=5, step=1)
    MentHlth = st.number_input("Enter MentHlth", min_value=0, max_value=30, value=20, step=1)
    PhysHlth = st.number_input("Enter PhysHlth", min_value=0, max_value=30, value=10, step=1)
    DiffWalk = st.selectbox("Do you have difficulty walking?", options=[0.0, 1.0], index=1)
    Sex = st.selectbox("Select your sex (0.0 for female, 1.0 for male)", options=[0.0, 1.0], index=1)
    Age = st.number_input("Enter Age", min_value=1, max_value=13, value=10, step=1)
    Education = st.number_input("Enter Education", min_value=1, max_value=6, value=6, step=1)
    Income = st.number_input("Enter Income", min_value=1, max_value=8, value=5, step=1)
    
    data={
        'HighBP': HighBP,
        'HighChol': HighChol,
        'CholCheck': CholCheck,
        'BMI': BMI,
        'Smoker': Smoker,
        'Stroke': Stroke,
        'HeartDiseaseorAttack': HeartDiseaseorAttack,
        'PhysActivity': PhysActivity,
        'Fruits': Fruits,
        'Veggies': Veggies,
        'HvyAlcoholConsump': HvyAlcoholConsump,
        'AnyHealthcare': AnyHealthcare,
        'NoDocbcCost': NoDocbcCost,
        'GenHlth': GenHlth,
        'MentHlth': MentHlth,
        'PhysHlth': PhysHlth,
        'DiffWalk': DiffWalk,
        'Sex': Sex,
        'Age': Age,
        'Education': Education,
        'Income': Income,
    }
    features = pd.DataFrame(data, index=[0])
    return features


input = user_input()

st.subheader('User Input')
st.write(input)

if st.button("Predict"):
    # Make prediction and display the result
    predicted = prediction.predict_default(input)
    if predicted == 1:
        st.write("The patient is Diabetes.")
    else:
        st.write("The patient is non Diabetes.")


st.title('Exploratory Data Analysis')

eda.plot1()
st.write("""
From the overall comparison diabetes status of dataset, we have 50.3% that negative diabetes and 49.7% that positive diabetes.
""")

eda.plot2()
st.write("""
From above distribution we have some information as like:
- BMI distribution for both of diabetes status have a roughly normal distribution, but the distribution for individuals with diabetes is shifted to the right. This indicates, on average of diabetes have higher BMI than those without diabetes.
- The age distribution for diabetes is generally skewed to the right, showing that older age groups have higher frequencies of diabetes. Then, for non diabetes the age distribution seems relatively uniform, but with a slight increase in frequency in the middle age ranges. Anyway, the diabetes is more prevalent in older population.
""")

eda.plot3()
st.write("""
We can see the status of diabetes based on health risk factors, here is the information that can be obtained:
- A larger number of individuals with high blood pressure also have diabetes compared to those who don't have high blood pressure. This suggest, a strong association between high blood pressure and diabetes.
- Similar to high blood pressure, high cholesterol levels are also more common in individuals with diabetes than in those without. This could indicate that high cholesterol is another condition that is commonly associated with diabetes.
- The difference between smokers and non-smokers in terms of diabetes prevalence is less pronounced than in the cases of high blood pressure or cholesterol. Smoking does not appear to show a clear pattern of association with diabetes in this data.
- Individuals that have history of stroke also tend to have higher rates of diabetes. There appears to be an association between the incidence of stroke and diabetes.
- There are more individuals with diabetes who have had a heart disease or attack than those without diabetes. This suggests that there is significant assocation between diabetes and heart-related health issues.
- There is difference in the consumption of fruits between diabetes and non-diabetes individuals, with non-diabetics more likely to consume fruits. This suggests that a potential assocation between fruits consumption and diabetes rates
- Like with fruits, a greater proportion of non-diabetics consume vegetables. This also suggests a potential assocation between vegetable consumption and lower diabetes rates
- The heavy alcohol consumption have fewer individuals with diabetes compared to those without. Then, Iindividuals who do not consume alcohol heavily, there are more individuals with diabetes than without.
""")

eda.plot4()
st.write("""
From visualization above, we have information as like:
- Education is ordinal categorical, for both diabetes status have majority of population a higher level education. However, the education level might indicate have relationship with diabetes status, possibly due to factors like better health awareness and lifestyle choices associated with higher education levels.
- The bar chart compares the count of individuals with and without diabetes between two sex categories, typically '0' represent females and '1' represent males. Males has a slightly higher count of individuals with diabetes compared to females.
""")
