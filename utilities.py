import pandas as pd
import numpy as np

import classes



def import_files():
    # Import the necessary files
    global amsurg_rev
    global asu_service
    global payer_class
    global detail

    amsurg_rev = pd.read_csv('C:\\Users\Michael\Documents\Work\Monte\Revenue\Amsurg\\amsurg_csv data\Amb Surg Finance 2019.csv')
    asu_service = pd.read_csv('C:\\Users\Michael\Documents\Work\Monte\Revenue\Amsurg\\amsurg_csv data\MMC Amb Surg 2017 ASU.csv')
    payer_class = pd.read_csv('C:\\Users\Michael\Documents\Work\Monte\Revenue\Amsurg\\amsurg_csv data\MMC Amb Surg 2017 Payors.csv')
    detail = pd.read_csv('C:\\Users\Michael\Documents\Work\Monte\Revenue\Amsurg\\amsurg_csv data\MMC Amb Surg 2017 detail.csv')



def reconfigure_dataframes(raw_file):
    raw_file.drop(columns='Unnamed: 26', inplace=True)

    # create a new datetime column and recast 'Month' to datetime format in the new column
    raw_file['Month_Year'] = pd.to_datetime(raw_file['Month'], format='%Y%m')
    raw_file[['Month', 'Account', 'MRN', 'Plan Cd']] = raw_file[['Month', 'Account', 'MRN', 'Plan Cd']].astype(str)

    raw_file["Service month"] = raw_file['Month_Year'].dt.month.apply(lambda month: convert_month.get(month))

    # populate a new facility column based on the convert_facility dict
    raw_file["Facility"] = raw_file['Hospital'].apply(lambda Facility: convert_facility.get(Facility))

    # use list comprehensions to creat lists for plan name and 2017 payor groups in the payer_class worksheet
    department = [department for department in asu_service['Department']]
    service = [asu for asu in asu_service['ASU SERVICE']]

    # zip the plan and payor classes into a dictionary to map the two
    convert_asu = dict(zip(department, service))

    # apply a lambda function and dict.get() method to populate a new column in ed_rev file with the 2017 Payor Groups
    raw_file["ASU SERVICE"] = raw_file['Department'].apply(lambda department: convert_asu.get(department))

    return raw_file

def create_dicts():

    global convert_month
    global convert_facility

    convert_facility = {'CHILDRENS HOSPITAL AT MONTEFIORE': 'MOSES', 'COMPREHENSIVE HEALTH CARE CENTER': 'MOSES',
                        'EASTCHESTER PRACTICE AT 1695': 'MOSES', 'MEDICAL PARK AT 1625 POPLAR': 'MOSES',
                        'MEDICAL PARK AT  1625 POPLAR': 'MOSES',
                        'HUTCH TOWER II': 'HUTCHINSON CENTER', 'MEDICAL ARTS PAVILION': 'MOSES',
                        'MEDICAL PARK AT 1500': 'MOSES',
                        'MOSES HOSPITAL': 'MOSES', 'NEUROSCIENCE CENTER': 'MOSES',
                        'WAKEFIELD HOSPITAL': 'WAKEFIELD',
                        'WEILER HOSPITAL': 'EINSTEIN', 'WESTCHESTER SQUARE HOSPITAL': 'WESTCHESTER SQUARE'}

    # create a dictionary to map the month components of the new datetime column to month description strings
    convert_month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
                     8: 'August', 9: 'September',
                     10: 'October', 11: 'November', 12: 'December'}

    department = [department for department in asu_service['Department']]
    service = [asu for asu in asu_service['ASU SERVICE']]

    # zip the plan and payor classes into a dictionary to map the two
    convert_asu = dict(zip(department, service))



import_files()
create_dicts()
reconfigure_dataframes(amsurg_rev)













