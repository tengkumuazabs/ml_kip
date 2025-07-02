# app.py

import streamlit as st
from rules import evaluate_applicant  # Import logic

st.title("Evaluasi Penerimaan Bantuan Pendidikan")

st.subheader("Masukkan Data Pendaftar")

row = {}

# Nomor dan Identitas
# row['nomor'] = st.number_input("Nomor", min_value=1, step=1)
# row['Nama Lengkap'] = st.text_input("Nama Lengkap", value="Budi Santoso")
# row['No. NIK'] = st.text_input("No. NIK", value="1234567892333450")
# row['No. KK'] = st.text_input("No. KK", value="1234567123123450")

# Dokumen boolean input (True/False)
row['KTP'] = st.checkbox("KTP", value=True)
row['Akte Lahir'] = st.checkbox("Akte Lahir", value=True)
row['Kartu Keluarga'] = st.checkbox("Kartu Keluarga", value=True)
row['Foto Rumah'] = st.checkbox("Foto Rumah", value=True)
row['Rekening Listrik'] = st.checkbox("Rekening Listrik", value=True)
row['Ijazah/SKL SMA'] = st.checkbox("Ijazah/SKL SMA", value=True)
row['Pas Foto 3x4'] = st.checkbox("Pas Foto 3x4", value=True)
row['Screenshot Diterima PTN/PTS '] = st.checkbox("Screenshot Diterima PTN/PTS", value=True)
row['SKTM (Surat Keterangan Tidak Mampu)'] = st.checkbox("SKTM (Surat Keterangan Tidak Mampu)", value=True)
row['Bukti Penghasilan'] = st.checkbox("Bukti Penghasilan", value=True)

# Nilai input
row['Nilai Raport'] = st.slider("Nilai Raport", min_value=0, max_value=100, value=85)
row['Nilai UN (SHUN)'] = st.slider("Nilai UN (SHUN)", min_value=0, max_value=100, value=85)

# Bantuan sosial
row['KKS (Kartu Keluarga Sejahtera)'] = st.checkbox("KKS (Kartu Keluarga Sejahtera)", value=True)
row['PKH (Penerima Keluarga Harapan)'] = st.checkbox("PKH (Penerima Keluarga Harapan)", value=False)

# Opsional - status, prestasi, KIP
row['Surat Prestasi'] = st.checkbox("Surat Prestasi", value=False)
row['Kartu Indonesia Pintar-Pendidikan Menengah'] = st.checkbox("Kartu Indonesia Pintar - Pendidikan Menengah", value=False)

# Evaluate
if st.button("Evaluasi"):
    result = evaluate_applicant(row)
    st.subheader("Hasil Evaluasi")
    st.write(result)



# import streamlit as st
# import pandas as pd
# import pickle

# # Set Streamlit page config (must be the first Streamlit command)
# st.set_page_config(page_title="Status Prediction App", layout="centered")

# # Load the trained model
# try:
#     with open('best_model.pkl', 'rb') as f:
#         model = pickle.load(f)
#     st.success("Model loaded successfully!")
# except FileNotFoundError:
#     st.error("Error: 'best_model.pkl' not found. Please ensure the model file is in the same directory.")
#     st.stop()  # Stop the app if the model isn't found

# st.title("Student Status Prediction App")
# st.write("Enter the student's details to predict their status (0 or 1).")

# # --- Input Features ---
# st.header("Student Information")

# col1, col2 = st.columns(2)

# with col1:
#     akte_lahir = st.checkbox("Has Birth Certificate (Akte Lahir)?", value=True)
#     akte_kk = st.checkbox("Has Family Card (Akte KK)?", value=True)
#     foto_rumah = st.checkbox("Has House Photo?", value=True)
#     rekening_listrik = st.checkbox("Has Electricity Bill?", value=False) # Example of a common False
#     ijazah_sma = st.checkbox("Has High School Diploma (Ijazah SMA)?", value=True)
#     pas_foto = st.checkbox("Has Passport Photo?", value=True)
#     prestasi = st.checkbox("Has Achievements (Prestasi)?", value=False)
#     kip = st.checkbox("Has KIP (Kartu Indonesia Pintar)?", value=False)

# with col2:
#     kks = st.checkbox("Has KKS (Kartu Keluarga Sejahtera)?", value=False)
#     pkh = st.checkbox("Has PKH (Program Keluarga Harapan)?", value=True) # Example of a common True
#     bdt = st.checkbox("Has BDT (Basis Data Terpadu)?", value=False)
#     kartu_miskin = st.checkbox("Has Poor Family Card (Kartu Miskin)?", value=True)
#     sktm = st.checkbox("Has SKTM (Surat Keterangan Tidak Mampu)?", value=True)
#     penghasilan_ortu = st.checkbox("Has Parent's Income Proof?", value=True)

# # Numerical Inputs
# st.subheader("Scores")
# nilai_raport = st.slider("Report Score (Nilai Raport)", min_value=0, max_value=100, value=85)
# nilai_un = st.slider("National Exam Score (Nilai UN)", min_value=0, max_value=100, value=75)


# # --- Prediction ---
# if st.button("Predict Status"):
#     # Create a DataFrame from inputs
#     input_data = pd.DataFrame([[
#         akte_lahir, akte_kk, foto_rumah, rekening_listrik, ijazah_sma,
#         nilai_raport, pas_foto, nilai_un, prestasi, kip, kks, pkh, bdt,
#         kartu_miskin, sktm, penghasilan_ortu
#     ]], columns=[
#         'akte_lahir', 'akte_kk', 'foto_rumah', 'rekening_listrik', 'ijazah_sma',
#         'nilai_raport', 'pas_foto', 'nilai_un', 'prestasi', 'kip', 'kks',
#         'pkh', 'bdt', 'kartu_miskin', 'sktm', 'penghasilan_ortu'
#     ])

#     # Convert boolean columns to integer (0 or 1) if the model expects numerical input
#     # This is crucial for models that don't handle boolean types directly, like StandardScaler
#     for col in input_data.columns:
#         if input_data[col].dtype == 'bool':
#             input_data[col] = input_data[col].astype(int)

#     # Make prediction
#     prediction = model.predict(input_data)
#     prediction_proba = model.predict_proba(input_data) # Get probabilities

#     st.subheader("Prediction Result:")
#     if prediction[0] == 1:
#         st.success(f"The predicted status is: **1 (Eligible)**")
#     else:
#         st.warning(f"The predicted status is: **0 (Not Eligible)**")

#     st.write(f"Confidence (Probability of Status 1): **{prediction_proba[0][1]:.2f}**")
#     st.write(f"Confidence (Probability of Status 0): **{prediction_proba[0][0]:.2f}**")

# st.markdown("---")
# st.write("App created by Gemini AI.")