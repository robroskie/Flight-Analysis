import pandas as pd
import numpy as np

def load_and_process_path(path):
    df = pd.read_csv(path)
   
    #Filter for date and remove time from first and last seen categories
    df['firstseen'] = df['firstseen'].str.slice(stop=10)
    df['lastseen'] = df['lastseen'].str.slice(stop=10)
    
    #Create datetime formatted column
    df['date'] = pd.to_datetime(df['firstseen'], format = '%Y-%m-%d')
    
    return df

def load_and_process_df(df):

    #Filter for date and remove time from first and last seen categories
    df['firstseen'] = df['firstseen'].str.slice(stop=10)
    #df['lastseen'] = df['lastseen'].str.slice(stop=10)
    
    #Create datetime formatted column
    df['date'] = pd.to_datetime(df['firstseen'], format = '%Y-%m-%d')
    
    return df