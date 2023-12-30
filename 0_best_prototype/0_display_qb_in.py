import sys
import pandas as pd
from tabulate import tabulate

def display_dataframe(df):
    # Display the DataFrame using tabulate
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

qb_input_file = sys.argv[1]

print(qb_input_file)

df = pd.read_csv(qb_input_file)

df_s = df[['Street Address', 'City', 'State', 'Zip']]

display_dataframe(df_s)



