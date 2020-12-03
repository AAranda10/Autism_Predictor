#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

##################### Acquire Mall Customers #######################

def prep_asd_data():
    df = pd.read_csv('Toddler Autism dataset July 2018.csv')
    df.columns = df.columns.str.replace('/','')
    df.columns = df.columns.str.replace(' ','')
    df = df.rename(columns = {'ClassASDTraits': 'is_asd', 'Who completed the test': 'completed_test', 'qchat-10-score': 'score'})
    df.columns = df.columns.str.lower()
    
    df = pd.get_dummies(df, columns = ['sex', 'jaundice', 'family_mem_with_asd', 'is_asd'], drop_first = True)
    
    df = df.rename(columns = {'is_asd_Yes': 'has_asd', 'family_mem_with_asd_yes':'has_fam_history',
                              'jaundice_yes': 'has_jaundice', 'sex_m': 'is_male', 'qchat-10-score':'survey_score'})
    df['is_white'] = df.ethnicity == 'White European'
    df['is_hispanic'] = (df.ethnicity == 'Hispanic') | (df.ethnicity == 'Latino')
    df['is_black'] = df.ethnicity == 'black'
    df['is_asian'] = (df.ethnicity == 'asian') | (df.ethnicity == 'south asian')
    df['is_middle_eastern'] = df.ethnicity == 'middle eastern'
    df['is_other'] = (df.ethnicity == 'Native Indian') | (df.ethnicity == 'Others') | (df.ethnicity == 'mixed') | (df.ethnicity == 'Pacifica')

    df = pd.get_dummies(df, columns = ['is_white', 'is_hispanic','is_black','is_asian', 'is_middle_eastern',
                                       'is_other'],drop_first = True)
    df = df.rename(columns = {'is_white_True': 'is_white', 'is_hispanic_True':'is_hispanic',
                              'is_asian_True': 'is_asian', 'is_middle_eastern_True': 'is_middle_eastern',
                              'is_black_True':'is_black', 'is_other_True': 'is_other'})
    return df
