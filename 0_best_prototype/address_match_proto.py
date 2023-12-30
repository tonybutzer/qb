#!/usr/bin/env python
# coding: utf-8

database_file = '/efs/data/addressdb_geo.sqlite'


myaddr='4301,S Mountain Ash Dr,Sioux Falls,SD,57103'


import sqlite3
import pandas as pd

def ret_df_from_address_db(zip_code, database_file):
  
    connection = sqlite3.connect(database_file)
    
    # Specify the table name (replace 'albums' with your actual table name)
    table_name = 'addresses'
    
    # Query to select all rows from the specified table
    query = f"SELECT * FROM {table_name} where zipcode = {zip_code};"
    
    # Use Pandas to read the SQL query result into a DataFrame
    df = pd.read_sql_query(query, connection)
    
    # Close the connection
    connection.close()
    

    return df


def is_valid_street_simple(qb_street_address, qb_city, qb_state, qb_zip):

    qb_number = qb_street_address.split(' ')[0]
    qb_street = ' '.join(qb_street_address.split(' ')[1:])
    match = False
    df = ret_df_from_address_db(qb_zip, database_file)
    dfn = df[df['number'].str.startswith(qb_number, na=False)]
    dfa = dfn[dfn['street'].str.contains(qb_street, case=False, na=False)]
    if dfa.shape[0] == 1:
        match = True
    return match


def ret_options(qb_street_address, qb_city, qb_state, qb_zip):

    qb_number = qb_street_address.split(' ')[0]
    qb_street = ' '.join(qb_street_address.split(' ')[1:])
    match = False
    df = ret_df_from_address_db(qb_zip, database_file)
    dfn = df[df['number'].str.startswith(qb_number, na=False)]
    #dfc = dfn[dfn['city'].str.contains(qb_city, case=False, na=False)]
    #dfa = dfn[dfn['street'].str.contains(qb_street, case=False, na=False)]

    return dfn



def qb_evaluate_address(df_row):
    '''
    return suggested_address_dict
    return stats = score, confidence, method
    '''
    # check zip errors
    # check db match
    # check smarty match
    # 
    pass
