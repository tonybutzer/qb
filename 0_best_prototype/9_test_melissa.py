#!/usr/bin/env python
# coding: utf-8

import sys
import pandas as pd
import yaml
from tabulate import tabulate


def display_dataframe(df):
    # Display the DataFrame using tabulate
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

qb_input_file = sys.argv[1]

print(qb_input_file)

df = pd.read_csv(qb_input_file)

df_s = df[['Street Address', 'City', 'State', 'Zip']]

display_dataframe(df_s)


bad_list_of_dicts = []

df_prune = df.head(2)
for i, my_df_row in df_prune.iterrows():
    print(my_df_row)



