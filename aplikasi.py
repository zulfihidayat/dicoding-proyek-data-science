import streamlit as st
import joblib
import os
import pandas as pd

# Load semua model
model_paths = {
    'Logistic Regression': 'model/logistic_regression.pkl',
    'Random Forest': 'model/random_forest.pkl',
    'Support Vector Machine': 'model/support_vector_machine.pkl',
    'Gradient Boosting': 'model/gradient_boosting.pkl',
    'AdaBoost': 'model/adaboost.pkl',
    'Bagging': 'model/bagging.pkl',
    'Extra Trees': 'model/extra_trees.pkl',
    'Stacking Ensemble': 'model/stacking_ensamble.pkl'
}
models = {name: joblib.load(path) for name, path in model_paths.items()}

# Load semua encoder
encoder_dir = 'encoders'
encoders = {}
for filename in os.listdir(encoder_dir):
    if filename.endswith('_encoder.pkl'):
        feature_name = filename.replace('_encoder.pkl', '')
        encoders[feature_name] = joblib.load(os.path.join(encoder_dir, filename))

# Streamlit UI
st.title('🚀 Employee Attrition Prediction')

with st.sidebar:
    st.header("Pilih Model Machine Learning")
    selected_model_name = st.selectbox('Model:', list(models.keys()))
    selected_model = models[selected_model_name]
    st.success(f'Model: **{selected_model_name}**')

st.subheader('🔎 Input Data Karyawan')

# Fungsi untuk mendapatkan pilihan yang valid dari encoder
def get_valid_choices(feature_name):
    encoder = encoders.get(feature_name)
    if encoder:
        return encoder.classes_.tolist()  # Mengambil kelas yang dikenal oleh encoder
    return []

# Input Data Karyawan dengan urutan fitur yang sesuai
OverTime = st.selectbox('OverTime', get_valid_choices('OverTime'))
JobRole = st.selectbox('JobRole', get_valid_choices('JobRole'))
MaritalStatus = st.selectbox('MaritalStatus', get_valid_choices('MaritalStatus'))
BusinessTravel = st.selectbox('BusinessTravel', get_valid_choices('BusinessTravel'))
EducationField = st.selectbox('EducationField', get_valid_choices('EducationField'))
Department = st.selectbox('Department', get_valid_choices('Department'))

EnvironmentSatisfaction = st.selectbox('EnvironmentSatisfaction (1: Tidak Puas - 4: Sangat Puas)', [1, 2, 3, 4])
JobInvolvement = st.selectbox('JobInvolvement (1: Rendah - 4: Tinggi)', [1, 2, 3, 4])
StockOptionLevel = st.selectbox('StockOptionLevel (0-3)', [0, 1, 2, 3])
JobLevel = st.selectbox('JobLevel (1-5)', [1, 2, 3, 4, 5])

st.subheader('🏷️ Kategori Hasil Binning')

AgeCategory = st.selectbox('AgeCategory', ['Junior', 'Mid', 'Senior', 'Pre-retire'])
TotalWorkingYearsCategory = st.selectbox('TotalWorkingYearsCategory', ['Novice', 'Intermediate', 'Experienced', 'Expert'])
YearsAtCompanyCategory = st.selectbox('YearsAtCompanyCategory', ['Newcomer', 'Settled', 'Loyal', 'Master'])
MonthlyIncomeCategory = st.selectbox('MonthlyIncomeCategory', ['Low', 'Medium', 'High', 'Very High'])
DistanceFromHomeCategory = st.selectbox('DistanceFromHomeCategory', ['Near', 'Moderate', 'Far'])
YearsWithCurrManagerCategory = st.selectbox('YearsWithCurrManagerCategory', ['New', 'Intermediate', 'Experienced', 'Senior', 'Very Senior'])
YearsInCurrentRoleCategory = st.selectbox('YearsInCurrentRoleCategory', ['New', 'Intermediate', 'Experienced', 'Senior', 'Very Senior'])

# Penjelasan Binning
with st.expander("ℹ️ Penjelasan Kategori Binning"):
    st.markdown("""
    **AgeCategory**
    - Junior: < 25 tahun
    - Mid: 25 - 35 tahun
    - Senior: 36 - 50 tahun
    - Pre-retire: > 50 tahun

    **TotalWorkingYearsCategory**
    - Novice: ≤ 5 tahun
    - Intermediate: 6 - 10 tahun
    - Experienced: 11 - 20 tahun
    - Expert: > 20 tahun

    **YearsAtCompanyCategory**
    - Newcomer: ≤ 2 tahun
    - Settled: 3 - 5 tahun
    - Loyal: 6 - 10 tahun
    - Master: > 10 tahun

    **MonthlyIncomeCategory**
    - Low: < 3000
    - Medium: 3000 - 7000
    - High: 7001 - 12000
    - Very High: > 12000

    **DistanceFromHomeCategory**
    - Near: ≤ 5 km
    - Moderate: 6 - 15 km
    - Far: > 15 km

    **YearsWithCurrManagerCategory** & **YearsInCurrentRoleCategory**
    - New: ≤ 2 tahun
    - Intermediate: 3 - 5 tahun
    - Experienced: 6 - 10 tahun
    - Senior: 11 - 15 tahun
    - Very Senior: > 15 tahun
    """)

# Tombol Prediksi
if st.button('🎯 Prediksi'):
    input_data = pd.DataFrame({
        'OverTime': [OverTime],
        'JobRole': [JobRole],
        'MaritalStatus': [MaritalStatus],
        'BusinessTravel': [BusinessTravel],
        'EducationField': [EducationField],
        'EnvironmentSatisfaction': [EnvironmentSatisfaction],
        'Department': [Department],
        'JobInvolvement': [JobInvolvement],
        'StockOptionLevel': [StockOptionLevel],
        'JobLevel': [JobLevel],
        'AgeCategory': [AgeCategory],
        'TotalWorkingYearsCategory': [TotalWorkingYearsCategory],
        'YearsAtCompanyCategory': [YearsAtCompanyCategory],
        'MonthlyIncomeCategory': [MonthlyIncomeCategory],
        'DistanceFromHomeCategory': [DistanceFromHomeCategory],
        'YearsWithCurrManagerCategory': [YearsWithCurrManagerCategory],
        'YearsInCurrentRoleCategory': [YearsInCurrentRoleCategory]
    })

    # Urutkan input_data sesuai dengan urutan kolom pada model
    feature_order = selected_model.feature_names_in_  # Dapatkan urutan fitur yang digunakan saat training
    input_data = input_data[feature_order]

    # Encode fitur kategorikal
    for col in input_data.columns:
        if col in encoders:
            encoder = encoders[col]
            try:
                input_data[col] = encoder.transform(input_data[col])
            except ValueError as e:
                st.error(f"Error encoding kolom '{col}': {e}")
                st.stop()

    # Prediksi
    prediction = selected_model.predict(input_data)
    st.success(f'Prediksi: **{"Attrition" if prediction[0] == 1 else "No Attrition"}**')