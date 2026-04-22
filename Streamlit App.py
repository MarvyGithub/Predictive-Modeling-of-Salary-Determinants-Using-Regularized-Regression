
# Loading of trained pipeline
 model = joblib.load("model.pkl") # saved model

 def make_prediction(job_title, years_of_experience, education_level, skills_count, industry, company_size, location, certifications, remote_work):
     
     # Validation
     valid_remote = ["Remote", "Hybrid", "Onsite"]
     if remote_work not in valid_remote:
         raise ValueError(f"remote_work must be one of {valid_remote}")
 
     if years_of_experience < 0:
         raise ValueError("years_of_experience cannot be negative")
 
     input_data = {
         'job_title': job_title,
         'experience_years': years_of_experience,
         'education_level': education_level,
         'skills_count': skills_count,
         'industry': industry,
         'company_size': company_size,
         'location': location,
         'remote_work': remote_work,
         'certifications': certifications
     }
 
     df = pd.DataFrame(input_data, index=[0])
     prediction = model.predict(df).round(2)[0]
 
     return prediction
 
  st.title("💰 Salary Prediction App")
 
 st.write("Enter details below to predict salary")
 
 # Inputs
 job_title = st.text_input("Job Title", "AI Engineer")
 experience = st.number_input("Years of Experience", min_value=0, value=5)
 education = st.selectbox("Education Level", ["High School", "Bachelor", "Master", "PhD"])
 skills = st.number_input("Number of Skills", min_value=0, value=3)
 industry = st.text_input("Industry", "Tech")
 company_size = st.selectbox("Company Size", ["Small", "Medium", "Large"])
 location = st.text_input("Location", "USA")
 remote_work = st.selectbox("Work Type", ["Remote", "Hybrid", "Onsite"])
 certifications = st.number_input("Certifications", min_value=0, value=1)
 
 # Prediction button
 if st.button("Predict Salary"):
     
     input_data = {
         'job_title': job_title,
         'experience_years': experience,
         'education_level': education,
         'skills_count': skills,
         'industry': industry,
         'company_size': company_size,
         'location': location,
         'certifications': certifications,
         'remote_work': remote_work
        }

    df = pd.DataFrame(input_data, index=[0])

    try:
        prediction = make_prediction(
            job_title,
            experience,
            education,
            skills,
            industry,
            company_size,
            location,
            certifications,
            remote_work
        )
        
        st.success(f"Predicted Salary: ${prediction}")

    except Exception as e:
