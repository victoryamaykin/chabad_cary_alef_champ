import streamlit as st
import pandas as pd
import re

# Load the data
df = pd.read_csv('hebrew_school_data.csv')

# Create a sidebar
st.sidebar.title('Hebrew School Alef Champ Progress Tracker')

# Create a dropdown menu for the teacher
teacher_name = st.sidebar.selectbox('Select a teacher', df['teacher'].unique())

class_df = df[df['teacher'] == teacher_name]

# Create a dropdown menu for the students in that class
student_name = st.sidebar.selectbox('Select a student', class_df['student_name'].values)

# Display the student's information
st.write('**Class Information**')
st.write('Teacher Name:', teacher_name)
# st.write('Level:', df['level'][df['student_name'] == student_name].values[0])
# st.write('Stripe:', df['stripe'][df['student_name'] == student_name].values[0])

# Display the student's information
# st.write('**Student Information**')
# st.write('Name:', student_name)
# st.write('Level:', df['level'][df['student_name'] == student_name].values[0])
# st.write('Teacher:', df['teacher'][df['student_name'] == student_name].values[0])

# Display the students
st.write('**Student Levels**')
keys = class_df['student_name'].values
st.table(df[df['teacher'] == teacher_name][['student_name', 'level', 'stripe', 'homework_1']])

# Display the student's homework
st.write('**Homework for Parents**')
st.table(df[df['student_name'] == student_name][['homework_2']])
st.write('**Goal**')
st.table(df[df['student_name'] == student_name][['homework_3']])

# # Create a button that allows parents to log in
st.sidebar.button('Log in as parent')

# # If the parent clicks the button, display a form where they can enter their login credentials
if st.sidebar.button('Log in as parent'):
    st.sidebar.write('**Parent Login**')
    username = st.sidebar.text_input('Username')
    password = st.sidebar.text_input('Password')

#     # If the login credentials are correct, display the student's homework
    if username == 'parent_username' and password == 'parent_password':
        st.write('**Homework**')
        st.table(df[df['student_name'] == student_name][['homework_1', 'homework_2', 'homework_3']])

#     # If the login credentials are incorrect, display an error message
    else:
        st.sidebar.write('Invalid username or password.')
