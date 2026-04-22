# Predictive-Modeling-of-Salary-Determinants-Using-Regularized-Regression
This project develops a machine learning model to predict salary based on key factors such as job role, education, experience, company size, and location. The goal is to identify the most influential drivers of salary and build a robust predictive system.

📊 Dataset
~250,000 observations
Features include:
Job Title
Education Level
Experience
Company Size
Location
Skills Count

🔍 Exploratory Data Analysis

Key findings:
Salary distribution is slightly right-skewed
Experience shows a weak positive relationship
Education shows a stronger structured relationship
Location and company size show noticeable variation
Skills count has minimal predictive power

⚙️ Methodology
Data split into training and test sets (80/20)
Pipeline used to ensure consistent preprocessing
One-Hot-Encoding applied to categorical variables
Ridge Regression is used to:
reduce overfitting
handle multicollinearity

| Metric       | Value  |
| ------------ | ------ |
| Baseline MAE | 29,807 |
| Training MAE | 5,470  |
| Test MAE     | 5,436  |
| R² Score     | 0.96   |


👉 Indicates strong predictive performance and good generalization.

💡 Key Insights
Location is the most influential factor in salary determination,
Certain job roles significantly increase earning potential,
Larger companies tend to offer higher salaries,
Higher education levels are associated with higher pay,
The number of skills alone is not a strong predictor

⚠️ Limitations
Encoded categorical features reduce interpretability,
The dataset may be highly structured, influencing model performance,
Real-world salary variation may include unobserved factors

🧰 Tools & Technologies
Python, 
Pandas, NumPy, 
Scikit-learn, 
Matplotlib / Seaborn

🚀 Conclusion
The model demonstrates strong predictive capability and highlights key drivers of salary. While results are robust, further work could improve interpretability and incorporate additional real-world variables.

🚀 Future Improvements
Restore original categorical labels for better interpretability, 
Experiment with other models (e.g., Lasso, Random Forest), 
Incorporate additional real-world features, 
Deploy as a simple web application


🚀 Deployment

This project was deployed as an interactive web application using Streamlit, enabling users to input job-related features and receive real-time salary predictions. The trained machine learning pipeline, including preprocessing steps and the Ridge regression model, was serialized using joblib and integrated into the application to ensure consistency between training and inference. Additional input validation was implemented within the prediction function to enforce data integrity and prevent invalid entries, enhancing the robustness and reliability of the application.

The application was further deployed online via Streamlit Community Cloud, allowing seamless public access through a web browser without requiring local setup. This deployment demonstrates the end-to-end lifecycle of a machine learning project, from data preprocessing and model development to production-ready deployment. By making the model accessible through an intuitive user interface, the project highlights practical considerations in real-world ML systems, including reproducibility, usability, and scalability.
