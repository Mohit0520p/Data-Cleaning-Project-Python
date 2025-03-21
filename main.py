
#import dependencies 
import pandas as pd
import numpy as np
import time
import os
import openpyxl
import xlrd
import random

# data_path='Sales.xlsx'
# data_name = 'Jan_Sales'
def data_cleaning_master(data_path,data_name):

    print('Thank you for sharing the details ')
    sec=random.randint(1,4) # generating random number 
    #print delay message . 
    print(f'Please wait for {sec} seconds! . Checking Path.')
    time.sleep(sec)

    if  not os.path.exists(data_path):
        print('Path does not exist , enter correct path. ')
        return

    else:
        if data_path.endswith('.csv'):
            print('Type of File Entered : .csv ')
            data = pd.read_csv(data_path,encoding_errors='ignore')
        elif data_path.endswith('.xlsx'):
            print('Type of File Entered : .xlsx ')
            data = pd.read_excel(data_path)
        else:
            print('Unknown File Type')
            return
        
    print(f'Please wait for {sec} seconds! . Checking total columns and rows.')
    time.sleep(sec)

    # printing the number of rows and columns of the dataset . 
    print(f"Dataset has :{data.shape[0]}  rows \n Dataset has :{data.shape[1]}  columns .")

    # Data Cleaning 
    duplicates = data.duplicated()
    total_dupes = data.duplicated().sum()

    print(f'Dataset has total :{total_dupes} duplicates. ')
    if total_dupes > 0 :
    #removing and saving the duplicates . 
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f'{data_name}_duplicated_records.csv',index=False)

    df = data.drop_duplicates()

    #handling missing values 
    missingv_percolumn = df.isnull().sum()
    total_missing = df.isnull().sum().sum()

    print(f'Total Missing Values are :{total_missing}')
    print('\n')
    print(f'Missing Values per column are \n:{missingv_percolumn}')

    #dealing with missing values 

    columns = df.columns

    for col in columns :
        #filling mean for numeric columns .
        if df[col].dtype in (int , float):
            df[col].fillna(df[col].mean(),inplace = True)
        else:
            #dropping all rows with missing values for non number columns .
            df.dropna(subset = col,inplace = True)

    #data is cleaned .
    print('Congratulations ! Dataset is cleaned \n.')
    print(f'Number of Rows:{df.shape[0]} \n Number of Columns {df.shape[1]} .')

    #exporting the cleaned dataset .
    df.to_csv(f'{data_name}_Cleaned_Data.csv',index=False)

    print('Dataset is saved !.')

    if __name__ == "__main__":

        print('Main fucntion calling')

        print('Welcome to data cleaning master . ')
        #ask path and file name 
        data_path=input('Please enter dataset path : ')
        data_name=input('Please enter dataset name : ')

        #calling the function 
        data_cleaning_master(data_path,data_name)

        

