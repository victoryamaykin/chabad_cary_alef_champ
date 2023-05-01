import time, os
import streamlit as st
import pandas as pd
import re
from pw import pw

# Load the data
df = pd.read_csv('hebrew_school_data.csv')

# Create a sidebar
st.sidebar.title('Hebrew School Alef Champ Progress Tracker')

# Create a dropdown menu for the teacher
teacher_name = st.sidebar.selectbox('Select a teacher', df['teacher'].unique())

class_df = df[df['teacher'] == teacher_name]

# Create a dropdown menu for the students in that class
student_name = st.sidebar.selectbox('Select a student', class_df['student_name'].values)

password = st.sidebar.text_input(f'Enter password to update for {student_name}')
# debug mode
password = 'matzah613'

# If the password is corect, show the update form
if password == pw:

    # Create a form
    with st.sidebar.form('update_df'):

        st.write(f"Update progress for {student_name}")

        levels = ["White", "Red", "Orange", "Yellow", "Green", "Blue"]
        
        # Get the level 
        level = st.radio('Level', options = levels, \
                         index = levels.index(df.loc[df['student_name'] == student_name, 'level'].values.item()))
        
        stripes = [1,2,3]
        
        # Get the stripe
        stripe = st.radio('Stripe', options = stripes, \
                          index = stripes.index(df.loc[df['student_name'] == student_name, 'stripe'].values.item()))

        # student homework
        homework_1 = st.text_input(f"Enter homework for {student_name}")

        submitted = st.form_submit_button("Submit")

        # Update the dataframe
        if submitted:
            df.loc[df['student_name'] == student_name, 'level'] = level
            df.loc[df['student_name'] == student_name, 'stripe'] = stripe
            df.loc[df['student_name'] == student_name, 'homework_1'] = homework_1
        
        st.write("***************")
        st.write("Add new student")
        
        name = st.text_input('Student name')

        # Update the dataframe
        if submitted:
            new_student = pd.DataFrame({'student_name': name, 'teacher': teacher_name, 'level': level, 'stripe': stripe, 'homework_1': ''})
            df = df.append(new_student, ignore_index=True)

# Display the student's information
st.write('**Class Information**')
st.write('Teacher Name:', teacher_name)

# Display the students
st.write('**Student Levels**')
st.table(df[df['teacher'] == teacher_name][['student_name', 'level', 'stripe', 'homework_1']])
