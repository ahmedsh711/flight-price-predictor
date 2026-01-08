import pandas as pd
import numpy as np
from src.utils import parse_duration

def clean_data(df):
    df = df.copy()
    df['Total_Stops'] = df['Total_Stops'].replace({'non-stop': 0, '1 stop': 1, '2 stops': 2, '3 stops': 3, '4 stops': 4})
    
    df['Date_of_Journey'] = pd.to_datetime(df['Date_of_Journey'], format='%d/%m/%Y')
    df['Departure_DateTime'] = pd.to_datetime(df['Date_of_Journey'].astype(str) + ' ' + df['Dep_Time'].astype(str))
    
    df['Duration_td'] = df['Duration'].apply(parse_duration)
    df['Arrival_DateTime'] = df['Departure_DateTime'] + df['Duration_td']
    df['Arrives_Next_Day'] = (df['Arrival_DateTime'].dt.date > df['Date_of_Journey'].dt.date).astype(int)
    
    df['Flight_Hour'] = df['Departure_DateTime'].dt.hour
    df['Arrival_Hour'] = df['Arrival_DateTime'].dt.hour
    df['Duration_Minutes'] = df['Duration_td'].dt.total_seconds() / 60
    df['Is_Night_Flight'] = ((df['Flight_Hour'] >= 22) | (df['Flight_Hour'] <= 6)).astype(int)
    
    df['Destination'] = df['Destination'].replace('New Delhi', 'Delhi')
    
    df = df.drop(['Dep_Time', 'Arrival_Time', 'Route', 'Additional_Info'], axis=1, errors='ignore')
    return df

def engineer_features(df):
    df = df.copy()
    df['Day_of_Week'] = df['Date_of_Journey'].dt.dayofweek
    df['Is_Weekend'] = (df['Day_of_Week'] >= 5).astype(int)
    df['Journey_Month_Num'] = df['Date_of_Journey'].dt.month
    df['Journey_Day_Num'] = df['Date_of_Journey'].dt.day
    
    df['Day_sin'] = np.sin(2 * np.pi * df['Day_of_Week'] / 7)
    df['Day_cos'] = np.cos(2 * np.pi * df['Day_of_Week'] / 7)
    df['Month_sin'] = np.sin(2 * np.pi * df['Journey_Month_Num'] / 12)
    df['Month_cos'] = np.cos(2 * np.pi * df['Journey_Month_Num'] / 12)
    
    df['Departure_Period'] = pd.cut(df['Flight_Hour'], bins=[-1, 6, 12, 18, 24],
                                     labels=['EarlyMorning', 'Morning', 'Afternoon', 'Evening'], include_lowest=True)
    
    df['Duration_Category'] = pd.cut(df['Duration_Minutes'], bins=[0, 120, 240, 480, 10000],
                                      labels=['Short', 'Medium', 'Long', 'VeryLong'], include_lowest=True)
    
    df['Is_Direct'] = (df['Total_Stops'] == 0).astype(int)
    
    if 'Total_Stops' in df.columns:
        df['Total_Stops'] = df['Total_Stops'].fillna(df['Total_Stops'].median())
        
    df = df.drop(['Date_of_Journey', 'Departure_DateTime', 'Arrival_DateTime', 'Duration_td'], axis=1, errors='ignore')
    return df