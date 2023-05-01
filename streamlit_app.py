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

# Create a form
with st.form('update_df'):

    # Get the level 
    level = st.radio('Level', options = ["White", "Red", "Orange", "Yellow", "Green", "Blue"])
    
    # Get the stripe
    stripe = st.radio('Stripe', options = [1,2,3])
    
    # student homework
    homework_1 = st.text_input("Enter homework for student")
    
    # parent homework
#     homework_2 =  st.text_input("Enter homework for parent")
    
    submitted = st.form_submit_button("Submit")
    
    # Update the dataframe
    if submitted:
        df.loc[df['student_name'] == student_name, 'level'] = level
        df.loc[df['student_name'] == student_name, 'stripe'] = stripe
        df.loc[df['student_name'] == student_name, 'homework_1'] = homework_1
        df.loc[df['student_name'] == student_name, 'homework_2'] = homework_2

# Display the student's information
st.write('**Class Information**')
st.write('Teacher Name:', teacher_name)

# Display the students
st.write('**Student Levels**')
keys = class_df['student_name'].values
st.table(df[df['teacher'] == teacher_name][['student_name', 'level', 'stripe', 'homework_1']])

# Display the parent's homework
# st.write('**Homework for Parents**')
# st.table(df[df['student_name'] == student_name][['homework_2']])
