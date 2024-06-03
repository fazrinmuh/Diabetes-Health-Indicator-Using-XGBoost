# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define data
df_eda = pd.read_csv('diabetes_binary_health_indicators_BRFSS2021.csv')

# Create Plot Functions
def plot1():
    # Histogram and Pie Chart of Comparison of Diabetes Status

    # Diabetes status
    diabetes_status = df_eda['Diabetes_binary'].value_counts()

    # Figure and axis
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    # Histogram
    axs[0].hist(df_eda['Diabetes_binary'], bins=5, color='skyblue', edgecolor='black')
    axs[0].set_title('Histogram of Comparison Diabetes Status')
    axs[0].set_xlabel('Status')
    axs[0].set_ylabel('Number of Diabetes Status')
    axs[0].set_xticks([0.1, 0.9])
    axs[0].set_xticklabels(['No', 'Yes'])
    axs[0].grid(axis='y', linestyle='--', alpha=0.7)

    # Pie Chart
    axs[1].pie(diabetes_status, labels=['No', 'Yes'], autopct='%1.1f%%', startangle=140, colors=['lightgreen', 'red'])
    axs[1].set_title('Pie Chart of Comparison Diabetes Status')
    axs[1].axis('equal')
    
    # Showing the Plot
    plt.tight_layout()
    
    # Show the plot
    st.pyplot()

def plot2():
    # Data subsets for diabetes and non-diabetes
    diabetes_data = df_eda[df_eda['Diabetes_binary'] == 1]
    non_diabetes_data = df_eda[df_eda['Diabetes_binary'] == 0]
    
    # Columns to be analyzed
    columns_to_analyze = ['BMI', 'Age']
    
    plt.figure(figsize=(20, 7))
    
    # Histogram plot for each column
    for column in columns_to_analyze:
        plt.subplot(1, 2, columns_to_analyze.index(column)+1)
        sns.histplot(diabetes_data[column], color='blue', kde=True, label='Diabetes')
        sns.histplot(non_diabetes_data[column], color='orange', kde=True, label='Non-Diabetes')
        plt.title(f'Distribution of {column} by Diabetes Status')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.legend()
    
    plt.tight_layout()
    
    # Show the plot
    st.pyplot()

def plot3():
    # Selecting the variables to be used for segmentation
    healthrisk_var = ['HighBP', 'HighChol', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'Fruits', 'Veggies', 'HvyAlcoholConsump']
    
    # Create subplots for each segmentation variable
    plt.figure(figsize=(15, 10))
    for i, var in enumerate(healthrisk_var):
        plt.subplot(4, 2, i+1)
        sns.countplot(x=var, hue='Diabetes_binary', data=df_eda)
        plt.title(f'Diabetes Status by {var}')
        plt.xlabel(var)
        plt.ylabel('Count')
        plt.legend(title='Diabetes Status', loc='upper right', labels=['No', 'Yes'])
    plt.tight_layout()

    # Show the plot
    st.pyplot()

def plot4():
    # Memilih variabel yang akan digunakan untuk segmentasi
    segment_vars = ['Education', 'Sex']

    # Membuat subplots untuk setiap variabel segmentasi
    plt.figure(figsize=(20, 7))
    for i, var in enumerate(segment_vars):
        plt.subplot(1, 2, i+1)
        sns.countplot(x=var, hue='Diabetes_binary', data=df_eda)
        plt.title(f'Diabetes Status by {var}')
        plt.xlabel(var)
        plt.ylabel('Count')
        plt.legend(title='Diabetes Status', loc='upper right', labels=['No', 'Yes'])
    plt.tight_layout()

    # Show the plot
    st.pyplot()