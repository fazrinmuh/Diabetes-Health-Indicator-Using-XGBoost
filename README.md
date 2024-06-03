This repository contains documentation on customer segmentation using a bank's credit card data. The data was obtained through BigQuery. Program and output listed in this repository mainly utilizes Indonesian language and may include specific or local term.

🚩 Project Name: Diabetes Health Prediction
🙋🏻‍♂️ Project Owner: Fazrin Muhammad  
🏁 Date Finished: April 2024
📞 Contact: [LinkedIn](https://www.linkedin.com/in/fazrin-muhammad-199098153/); [E-mail](mailto:fazriinmuhammad@gmail.com)

# Introduction:
Diabetes is a chronic disease with a rising global prevalence, including in the United States. According to data from the Centers for Disease Control and Prevention (CDC), approximately 34.2 million adults in the United States, or around 13% of the adult population, were diagnosed with diabetes in 2020. This condition has significant implications for individual health and healthcare costs. The Behavioral Risk Factor Surveillance System (BRFSS) is a telephone survey conducted by the CDC to collect data on health-related risk behaviors, chronic health conditions, and preventive service utilization.

# Objective:
The predictive analysis aims to build a model that can identify individuals at high risk of diabetes based on relevant factors. By using BRFSS data, I'll explore with five different classificaton models: K-Nearest Neighbor (KNN), Support Vector Machine (SVM), Decision Tree, and Random Forest and also boosting algorithm XGBClassifier. Then, compare the model with the base one to choose the best option for predicting diabetes.

# Result:
This diabetes status prediction project confirms the superiority of XGBoost after hyperparameter tuned with 80% recall score as the model of choice with a special focus on minimizing False Negatives, a crucial aspect to ensure that no cases of diabetes are missed. An in-depth analysis of model performance revealed that XGBoost, especially after tuning, outperforms other models in terms of recall, making it highly effective in identifying positive cases in both training and testing data.

---