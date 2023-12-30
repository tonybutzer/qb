import pandas as pd

from address_match_proto import is_valid_street_simple

global ZIP_DF

def load_zip():
    global ZIP_DF
    file_path = 'ZIP_Locale_Detail.xls'

    # Read the Excel file into a Pandas DataFrame
    ZIP_DF = pd.read_excel(file_path, dtype=str)



class ZIP:

    def is_valid(self, zip_code):
        global ZIP_DF
        filtered_rows = ZIP_DF[ZIP_DF['DELIVERY ZIPCODE'] == zip_code]
        if filtered_rows.empty:
            return False
        else:
            return True
    
    def is_equal(self, zip_code, city):
        global ZIP_DF
        filtered_rows = ZIP_DF[ZIP_DF['DELIVERY ZIPCODE'] == zip_code]
        #print(filtered_rows['LOCALE NAME'].values[0])
        locale_name = filtered_rows['LOCALE NAME'].values[0]
        physical_city = filtered_rows['PHYSICAL CITY'].values[0]
        # print(locale_name, physical_city)
        if city.upper() == locale_name:
            return True

        if city.upper() == physical_city:
            return True
        else:
            return False
   
    def is_5_digits(self, zip_code):
        if len(zip_code) == 5:
            return True
        else:
            return False


def qb_validate_zip(df_row):
    #print(df_row.Zip, df_row.City)
    # Example usage:
    zip_instance = ZIP()
     # Test is_equal method
    qb_zip = str(df_row.Zip)
    qb_city = df_row.City

    zip_valid = zip_instance.is_valid(qb_zip)
    if not zip_valid:
        print(f"zip_valid result: {zip_valid}")
        return False
    # Test is_5_digits method
    digits_result = zip_instance.is_5_digits(qb_zip)
    #print(f"is_5_digits result: {digits_result}")

    if not digits_result:
        print(f"is_5_digits result: {digits_result}")
        return False

    
    zip_result = zip_instance.is_equal(qb_zip, qb_city)
    #print(f"is_equal result: {zip_result}")

    if not zip_result:
        print(f"City and ZIP is_equal result: {zip_result}")
        return False

    return True


def qb_validate_street(df_row):
    qb_zip = str(df_row.Zip)
    qb_street_address = df_row['Street Address']
    qb_state = df_row.State
    qb_city = df_row.City

    print(qb_street_address, qb_city, qb_state, qb_zip)
    a_status = is_valid_street_simple(qb_street_address, qb_city, qb_state, qb_zip)
    print(a_status)
    return a_status
