import time, os
import streamlit as st
import pandas as pd
import re
from pw import pw
from datetime import date

file_name = "hebrew_school_data.csv"
progress_file = "student_progress_report.csv" 

# Load the data
df = pd.read_csv(file_name)
progress_df = pd.read_csv(progress_file)

# Create a sidebar
st.sidebar.title('Hebrew School Alef Champ Progress Tracker')

# Create a dropdown menu for the teacher
teacher_name = st.sidebar.selectbox('Select a teacher', df['teacher'].unique())

class_df = df[df['teacher'] == teacher_name]

# Create a dropdown menu for the students in that class
student_name = st.sidebar.selectbox('Select a student', class_df['student_name'].values)

password = st.sidebar.text_input(f'Enter password to update')
# debug mode
password = 'matzah613'

# lists
levels = ["White", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Brown", "Grey", "Black"]
stripes = [1,2,3]
        
# If the password is corect, show the update form
if password == pw:

    # Create a form
    with st.sidebar.form('update_df'):

        st.write(f"Update progress for {student_name}")
        
        if not isinstance(progress_df[progress_df['student_name'] == student_name], type(None)):
                st.table(progress_df[progress_df['student_name'] == student_name][['date', 'level', 'stripe']])
        else:
                st.write("no past progress records yet")
                
        # Today's date
        date = st.date_input("Select Date", value=date.today())
        
        # Get the level 
        level = st.radio('Level', options = levels, \
                         index = levels.index(df.loc[df['student_name'] == student_name, 'level'].values.item()))
        
        # Get the stripe
        stripe = st.radio('Stripe', options = stripes, \
                          index = stripes.index(df.loc[df['student_name'] == student_name, 'stripe'].values.item()))

        # student homework
        homework = st.text_input(f"Enter homework for {student_name}")

        submitted = st.form_submit_button("Submit")

        # Update the dataframe
        if submitted:
            # Save to current roster
            df.loc[df['student_name'] == student_name, 'level'] = level
            df.loc[df['student_name'] == student_name, 'stripe'] = stripe
            df.loc[df['student_name'] == student_name, 'homework'] = homework
            df.to_csv(file_name, sep=',')
        
            # Save progess to progress report
            progress_df = progress_df.append({'date': date, 'student_name': student_name, 'level': level, 'stripe': stripe}, ignore_index=True)
            progress_df.to_csv(progress_file, sep=',')

# Display the student's information
st.write('<<< Open the sidebar to select classroom and update student progress.')
st.write('***********')
st.write('**Chabad of Cary: Alef Champ**')
st.write('***********')
st.write(f'**Teacher Name:** {teacher_name}')
st.write('***********')

# Display the students
st.table(df[df['teacher'] == teacher_name][['student_name', 'level', 'stripe', \
                                            'homework']].sort_values(by=['level', 'stripe']))
