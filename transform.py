import pandas as pd
import numpy as np

def transform_orginal(df):
    '''
    '''

    df['YEAR'] = df['Sown \nDate'].apply(lambda x: x.year)
    df['Sow Month'] = df['Sown \nDate'].apply(lambda x: x.month)

    return df

def merge_transform(df, rainfall_df, altitude_df):
    '''
    '''

    rain_org_df = pd.merge(df, rainfall_df, on=['Location', 'YEAR'])

    rain_org_df['Rainfall'] = rain_org_df.apply(lambda x:
                                            (x[str(x['Sow Month'])] +
                                             x[str(x['Sow Month'] + 1)] +
                                             x[str(x['Sow Month'] + 2)])
                                            if x['Sow Month'] < 11 else
                                            (x[str(x['Sow Month'])] + x[str(x['Sow Month'] + 1)])
                                            if x['Sow Month'] < 12 else
                                            x[str(x['Sow Month'])], axis=1)
                                            
    final_df = pd.merge(rain_org_df, altitude_df, on=['Location'])

    return final_df
