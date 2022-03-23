
import psycopg2
import numpy as np
import pandas as pd
import streamlit as st
from psycopg2 import Error
from pycaret.classification import load_model, predict_model



# Initialize connection.
# Uses st.cache to only run once.
# @st.cache (allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

records = run_query("SELECT prospect_id, \
                 question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, \
                 question13, question14, question15, question16, question17, question18, question19, question20, question21, question22, question23, question24, \
                 question25, question26, question27, question28, question29, question30 \
                 FROM academy_service.prospect_psychometric_results")

records = pd.DataFrame(records)


# Rename the columns of the input
records.columns = records.columns.rename = ('prospectid', 'question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'question7', 'question8', 'question9', 
                                            'question10', 'question11', 'question12','question13', 'question14', 'question15', 'question16', 'question17', 'question18', 
                                            'question19', 'question20', 'question21', 'question22', 'question23','question24', 'question25', 'question26', 'question27', 'question28', 
                                            'question29', 'question30')

# Load the model into the app
pipeline = load_model('loan_default')


@st.cache

# Define the prediction function
def prediction(feature):

    predictions = predict_model(pipeline, data = feature)
    
    predictions = "%.2f" % predictions['Score'][0]
    
    return predictions

# The main fucntion to run the application
def main():
    
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">MAX Loan Default Model</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    
    # Create a form to read the result of each prospect
    form = st.form(key='my_form')
    prospectid = form.text_input(label='Enter the Prospect ID')
    submit_button = form.form_submit_button(label='Submit')
    
    # Initialize the structure of the columns
    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)
    col9, col10, col11, col12 = st.columns(4)
    col13, col14, col15, col16 = st.columns(4)
    col17, col18, col19, col20 = st.columns(4)
    col21, col22, col23, col24 = st.columns(4)
    col25, col26, col27, col28 = st.columns(4)
    col29, col30 = st.columns(2)

    # When the submit button is pressed
    if submit_button: 
        
        # Checks if a correct prospectid was inputed
        if prospectid not in list(records['prospectid']):
            st.warning('The Prospect ID is not valid')
            st.stop()
        else:
            for i in records.index: 
                if (records['prospectid'][i] == prospectid):
                    question1 = col1.text_input("Question 1", records['question1'][i])
                    question2 = col2.text_input("Question 2", records['question2'][i])
                    question3 = col3.text_input("Question 3", records['question3'][i])
                    question4 = col4.text_input("Question 4", records['question4'][i])
                    question5 = col5.text_input("Question 5", records['question5'][i])
                    question6 = col6.text_input("Question 6", records['question6'][i])
                    question7 = col7.text_input("Question 7", records['question7'][i])
                    question8 = col8.text_input("Question 8", records['question8'][i])
                    question9 = col9.text_input("Question 9", records['question9'][i])
                    question10 = col10.text_input("Question 10", records['question10'][i])
                    question11 = col11.text_input("Question 11", records['question11'][i])
                    question12 = col12.text_input("Question 12", records['question12'][i])
                    question13 = col13.text_input("Question 13", records['question13'][i])
                    question14 = col14.text_input("Question 14", records['question14'][i])
                    question15 = col15.text_input("Question 15", records['question15'][i])
                    question16 = col16.text_input("Question 16", records['question16'][i])
                    question17 = col17.text_input("Question 17", records['question17'][i])
                    question18 = col18.text_input("Question 18", records['question18'][i])
                    question19 = col19.text_input("Question 19", records['question19'][i])
                    question20 = col20.text_input("Question 20", records['question20'][i])
                    question21 = col21.text_input("Question 21", records['question21'][i])
                    question22 = col22.text_input("Question 22", records['question22'][i])
                    question23 = col23.text_input("Question 23", records['question23'][i])
                    question24 = col24.text_input("Question 24", records['question24'][i])
                    question25 = col25.text_input("Question 25", records['question25'][i])
                    question26 = col26.text_input("Question 26", records['question26'][i])
                    question27 = col27.text_input("Question 27", records['question27'][i])
                    question28 = col28.text_input("Question 28", records['question28'][i])
                    question29 = col29.text_input("Question 29", records['question29'][i])
                    question30 = col30.text_input("Question 30", records['question30'][i])

                    # Write the results back into a DataFrame
                    feature = pd.DataFrame([{'question1':question1, 'question2':question2, 'question3':question3, 'question4':question4,
                                'question5':question5, 'question6':question6, 'question7':question7, 'question8':question8,'question9':question9,
                                'question10':question10,'question11':question11,'question12':question12,'question13':question13,'question14':question14,
                                'question15':question15,'question16':question16,'question17':question17,'question18':question18,'question19':question19,
                                'question20':question20,'question21':question21,'question22':question22,'question23':question23,'question24':question24,
                                'question25':question25,'question26':question26,'question27':question27,'question28':question28,'question29':question29,
                                'question30':question30}])

                    # Make prediction based on the results in the DataFrame
                    st.success('Loan Default Score = **{}**'.format(prediction(feature)))

        # To initiate another re-run of the application session
        st.button("Make Another Prediction")
                    
                    
# Run the application
if __name__=='__main__': 
    main()    
