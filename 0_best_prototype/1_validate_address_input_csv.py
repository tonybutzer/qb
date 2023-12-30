#!/usr/bin/env python
# coding: utf-8

import sys
import pandas as pd
import yaml
from tabulate import tabulate

from qb_zip import qb_validate_zip, qb_validate_street, load_zip
from qb_force_edit import force_edit, edit_or_quit
#from address_match_proto import is_valid_street_simple

load_zip()

def display_dataframe(df):
    # Display the DataFrame using tabulate
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

qb_input_file = sys.argv[1]

print(qb_input_file)

df = pd.read_csv(qb_input_file)

df_s = df[['Street Address', 'City', 'State', 'Zip']]

display_dataframe(df_s)


bad_list_of_dicts = []
for i, my_df_row in df.iterrows():
    #print(type(my_df_row))
    #print(my_df_row)
    if qb_validate_zip(my_df_row):
        pass
    else:
        print('BIG PROBLEM')
        #print(my_df_row)
        print('-'*30)
        broken_dict = my_df_row.to_dict()
        better_dict = edit_or_quit(broken_dict)
        #bad_list_of_dicts.append(my_df_row.to_dict())
        continue

    if qb_validate_street(my_df_row):
        pass
    else:
        print('SMALL PROBLEM')
        print(my_df_row)
        print('-'*30)
        bad_list_of_dicts.append(my_df_row.to_dict())



